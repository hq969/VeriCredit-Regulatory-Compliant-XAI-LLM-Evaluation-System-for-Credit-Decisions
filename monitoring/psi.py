import numpy as np

def psi(expected, actual, bins=10):
    breakpoints = np.percentile(expected, np.arange(0, 100, 100/bins))
    psi_value = 0
    for i in range(len(breakpoints)-1):
        e = ((expected >= breakpoints[i]) & (expected < breakpoints[i+1])).mean()
        a = ((actual >= breakpoints[i]) & (actual < breakpoints[i+1])).mean()
        psi_value += (a-e) * np.log(a/e)
    return psi_value
