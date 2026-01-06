import numpy as np

def psi(expected, actual, buckets=10):
    breakpoints = np.percentile(expected, np.arange(0, 100, 100 / buckets))
    breakpoints = np.append(breakpoints, np.inf)

    expected_counts = np.histogram(expected, breakpoints)[0]
    actual_counts = np.histogram(actual, breakpoints)[0]

    expected_perc = expected_counts / len(expected)
    actual_perc = actual_counts / len(actual)

    psi_value = np.sum(
        (actual_perc - expected_perc) *
        np.log((actual_perc + 1e-6) / (expected_perc + 1e-6))
    )
    return round(psi_value, 3)
