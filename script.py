import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from scipy import signal, stats
from scipy.optimize import minimize 
import warnings
warnings.filterwarnings('ignore')
import astropy.units as u
from astropy.timeseries import BoxLeastSquares
from astropy import constants as const
import lightkurve as lk

constants = {
    'R_earth' : 6.71e6,
    'R_sun' : 6.96e8,
    'R_jupiter': 7.15e7,
    'au' : 1.496e11,
    'day' : 86400,
    'ppm' : 1e-6
}

search_result = lk.search_lightcurve('TOI 715', mission='TESS')
lc_collection = search_result.download_all()

lc = lc_collection.stitch().remove_nans().flatten(window_length=401)

lc.plot(title="TOI-715 TESS Light Curve")

periods = np.linespace(1, 20, 10000)
bls = lc.to_peridogram(method ='bls', period=periods)

bls.plot(title="Box Least Squares Periodogram")
period = bls.period_at_max_power
t0 = bls.transit_time_at_max_power

folded_lc = lc.fold(period=periods, )