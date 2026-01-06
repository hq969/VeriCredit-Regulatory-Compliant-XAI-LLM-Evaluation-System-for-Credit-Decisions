from aif360.metrics import BinaryLabelDatasetMetric

def stress_test(dataset):
    metrics = BinaryLabelDatasetMetric(
        dataset,
        unprivileged_groups=[{'gender': 0}],
        privileged_groups=[{'gender': 1}]
    )
    return {
        "disparate_impact": metrics.disparate_impact(),
        "stat_parity": metrics.statistical_parity_difference()
    }
