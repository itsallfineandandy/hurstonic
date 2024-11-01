import numpy as np
from hurstonic_package.hurst import hurst_exponent

def rolling_hurst(time_series, window_size):
    """Calculate the rolling Hurst exponent with a specified window size."""
    n = len(time_series)
    result = np.empty(n - window_size + 1)
    for i in range(n - window_size + 1):
        window = time_series[i:i + window_size]
        result[i] = hurst_exponent(window)
    return result

