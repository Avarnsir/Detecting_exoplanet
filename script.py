import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import scipy import signal, stats
import scipy.optimize import minimize 
import warnings
warnings.filterwarnings('ignore')
import astropy.units as u
from astropy.timeseries import BoxLeastSquares
from astropy import constants as constimport lightkurve as lk

constants = {
    'R_earth' : 6.71e6,
    'R_sun' : 6.96e8,
    'R_jupiter': 7.15e7,
    'au' : 1.496e11,
    'day' : 86400,
    'ppm' : 1e-6
}

class exoplanet_detection:
    """
    TESS exoplanet detection pipeline

    This class handles:
    1.TESS data download and preprocessing
    2.Transit search algorithm (BLS)
    3. Signal validation and chracterization
    4. Planet parameter estimation
    """
    def __init__(self, target_name=None, tic_id=None):
        self.target_name = TOI 715
        #self.tic_id = TIC 
        self.lightcurve = detetector.download_tress_data(sectors='all')
        self.processed_lc = 
        self.transit_results = []
        self.planet_candidates = []

        print(f"Initialized TESS exoplanet detector")
        if target_name:
            print(f"Target: {target_name}")
        if tic_id:
            print(f"TIC ID: {tic_id}")

    def download_tess_data(self, sectors='all', cadence='short'):

