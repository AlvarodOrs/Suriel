import os
import numpy as np
import matplotlib.pyplot as plt
from winsound import Beep

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.callbacks import CheckpointCallback

from ..features import indicators
from ..utils.progressBar import TqdmCallback
from ..env.factory import make_env
from .evaluation import evaluate_model

class TradingPipeline:
    def __init__(self, file_path):
        self.file_path = file_path

    # ---------- DATA ----------
    def load_data(self):
        df, feature_cols = indicators.load_and_preprocess_data(self.file_path)

        split_idx = int(len(df) * 0.8)
        self.train_df = df.iloc[:split_idx]
        self.test_df = df.iloc[split_idx:]
        self.feature_cols = feature_cols

    # ---------- ENVS ----------
    def build_envs(self):
        self.train_vec_env = DummyVecEnv([
            lambda: make_env(self.train_df, self.feature_cols, "train")
        ])

        self.train_eval_env = DummyVecEnv([
            lambda: make_env(self.train_df, self.feature_cols, "eval")
        ])

        self.test_eval_env = DummyVecEnv([
            lambda: make_env(self.test_df, self.feature_cols, "eval")
        ])

    # ---------- MODEL ----------
    def build_model(self):
        self.model = PPO(
            "MlpPolicy",
            self.train_vec_env,
            verbose=1,
            tensorboard_log="./logs/tensorboard/"
        )

    # ---------- CHECKPOINTS ----------
    def build_checkpoints(self):
        self.ckpt_dir = "./checkpoints"
        os.makedirs(self.ckpt_dir, exist_ok=True)

        self.checkpoint_callback = CheckpointCallback(
            save_freq=50_000,
            save_path=self.ckpt_dir,
            name_prefix="ppo_eurusd"
        )

    # ---------- TRAIN ----------
    def train(self, total_timesteps=600_000):
        callback = TqdmCallback(total_timesteps)

        try:
            self.model.learn(
                total_timesteps=total_timesteps,
                callback=[self.checkpoint_callback, callback]
            )
        except Exception:
            Beep(400, 200)
            Beep(400, 200)
            Beep(400, 200)
            Beep(400, 200)
            raise

    # ---------- EVAL ----------
    def evaluate_checkpoints(self):
        self.last_equity_curve, self.last_equity = evaluate_model(
            self.model,
            self.test_eval_env
        )

        print(f"[OOS Eval] Last model: {self.last_equity:.2f}")

        best_equity = -np.inf
        best_path = None

        ckpts = sorted(
            [f for f in os.listdir(self.ckpt_dir) if f.endswith(".zip")],
            key=lambda x: os.path.getmtime(os.path.join(self.ckpt_dir, x))
        )

        for ck in ckpts:
            path = os.path.join(self.ckpt_dir, ck)
            m = PPO.load(path, env=self.test_eval_env)

            _, eq = evaluate_model(m, self.test_eval_env)
            print(f"[OOS Eval] {ck} -> {eq:.2f}")

            if eq > best_equity:
                best_equity = eq
                best_path = path

        self.best_equity = best_equity
        self.best_path = best_path

    # ---------- SELECTION ----------
    def select_best_model(self):
        if self.best_path is None or self.last_equity >= self.best_equity:
            self.best_model = self.model
        else:
            self.best_model = PPO.load(self.best_path, env=self.train_vec_env)

        os.makedirs("models", exist_ok=True)
        self.best_model.save("models/model_eurusd_best")

    # ---------- PLOT ----------
    def plot(self):
        train_curve, _ = evaluate_model(self.best_model, self.train_eval_env)
        test_curve, _ = evaluate_model(self.best_model, self.test_eval_env)

        plt.plot(train_curve, label="Train")
        plt.plot(test_curve, label="Test")
        plt.legend()
        plt.show()

    # ---------- RUN ----------
    def run(self):
        self.load_data()
        self.build_envs()
        self.build_model()
        self.build_checkpoints()

        self.train()
        self.evaluate_checkpoints()
        self.select_best_model()
        self.plot()