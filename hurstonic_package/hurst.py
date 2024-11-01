import numpy as np

def hurst_exponent(time_series):
    """Calculate the Hurst exponent of a time series using R/S analysis."""
    lags = np.arange(2, min(len(time_series) // 2, 100))
    tau = []

    for lag in lags:
        lagged_diff = time_series[lag:] - time_series[:-lag]
        std_dev = np.std(lagged_diff)
        if std_dev > 0:
            tau.append(std_dev)

    if len(tau) < 2:
        return np.nan

    log_lags = np.log(lags[:len(tau)])
    log_tau = np.log(tau)

    poly = np.polyfit(log_lags, log_tau, 1)
    return poly[0] * 2.0