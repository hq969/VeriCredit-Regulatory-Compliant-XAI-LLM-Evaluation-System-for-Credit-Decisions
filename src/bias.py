from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric
import pandas as pd

def bias_deviation(df):
    dataset = BinaryLabelDataset(
        df=df,
        label_names=["approved"],
        protected_attribute_names=["gender"]
    )

    metric = BinaryLabelDatasetMetric(
        dataset,
        privileged_groups=[{"gender": "M"}],
        unprivileged_groups=[{"gender": "F"}]
    )

    return round(abs(metric.disparate_impact() - 1), 2)
