from typing import Any, Optional
from dataclasses import dataclass
from datetime import date


# Training row
@dataclass
class FeatureRow:
    symbol: str
    date: date

    features: dict[str, float]

    target: float

# Prediction
@dataclass
class PredictionResult:
    symbol: str
    prediction_date: date

    mean_prediction: float

    std_prediction: float

    lower_95: float

    upper_95: float

# Experiment
@dataclass
class PredictionResult:
    symbol: str
    prediction_date: date

    mean_prediction: float

    std_prediction: float

    lower_95: float

    upper_95: float

# Dataset
@dataclass
class DatasetMetadata:
    dataset_name: str

    symbols: list[str]

    start_date: date

    end_date: date

    num_rows: int

    num_features: int