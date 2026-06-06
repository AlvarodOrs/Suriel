from winsound import Beep

from stable_baselines3.common.callbacks import BaseCallback
from tqdm import tqdm


class TqdmCallback(BaseCallback):
    def __init__(self, total_timesteps: int):
        super().__init__()
        self.total_timesteps: int = total_timesteps
        self.pbar = None
        self.next_beep_threshold = 0.1  # 10%
        self.last_beeped = 0

    def _beep(self, count=1, freq=1000, duration=150):
        for _ in range(count): Beep(freq, duration)

    def _on_training_start(self):
        self.pbar = tqdm(total=self.total_timesteps, desc="Training PPO")

    def _on_step(self):
        self.pbar.n = self.num_timesteps
        self.pbar.refresh()

        progress = self.num_timesteps / self.total_timesteps

        if progress >= self.next_beep_threshold:
            self._beep(1)
            self.next_beep_threshold += 0.1

        return True

    def _on_training_end(self):
        self.pbar.n = self.total_timesteps
        self.pbar.refresh()
        self.pbar.close()

        self._beep(2)

    def on_rollout_end(self): return True

    def __del__(self):
        if self.pbar is not None: self.pbar.close()