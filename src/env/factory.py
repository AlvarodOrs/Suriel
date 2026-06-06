from src.test.env import ForexTradingEnv

SL_OPTS = [5, 10, 15, 25, 30, 60, 90, 120]
TP_OPTS = [5, 10, 15, 25, 30, 60, 90, 120]
WIN = 30


def make_env(df, feature_cols, mode="train"):
    common = dict(
        df=df,
        window_size=WIN,
        sl_options=SL_OPTS,
        tp_options=TP_OPTS,
        spread_pips=1.0,
        commission_pips=0.0,
        max_slippage_pips=0.2,
        feature_columns=feature_cols,
    )

    if mode == "train":
        return ForexTradingEnv(
            **common,
            random_start=True,
            min_episode_steps=1000,
            episode_max_steps=2000,
            hold_reward_weight=0.0,
            open_penalty_pips=0.0,
            time_penalty_pips=0.0,
            unrealized_delta_weight=0.0,
        )

    return ForexTradingEnv(
        **common,
        random_start=False,
        episode_max_steps=None,
        hold_reward_weight=0.0,
        open_penalty_pips=0.0,
        time_penalty_pips=0.0,
        unrealized_delta_weight=0.0,
    )