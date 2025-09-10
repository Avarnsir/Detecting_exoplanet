import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np

# Search for and download TESS light curve data for TOI-715
search_result = lk.search_lightcurve('TOI 715', mission='TESS')
lc_collection = search_result.download_all()

# Concatenate all sectors into one LightCurve object
lc = lc_collection.stitch().remove_nans().flatten(window_length=401)

# Plot the full processed light curve to spot variability and transit dips
lc.plot(title="TOI-715 TESS Light Curve")

# Use Box Least Squares (BLS) algorithm to search for transit signals
periods = np.linspace(1, 20, 10000) # search 1-20 day periods
bls = lc.to_periodogram(method='bls', period=periods)

# Plot the BLS periodogram to reveal candidate period(s)
bls.plot(title="Box Least Squares Periodogram")

# Identify the most likely period and transit time
period = bls.period_at_max_power
t0 = bls.transit_time_at_max_power

# Phase-fold and plot the light curve
folded_lc = lc.fold(period=period, epoch_time=t0)
folded_lc.scatter(title=f"Phase-Folded Transit for TOI-715 b\nPeriod ≈ {period.value:.4f} days")
plt.show()
