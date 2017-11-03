
from spectra_analysis.regression import fit_params
from spectra_analysis.regression import transform
from numpy.testing import (assert_allclose, assert_array_equal,
                           assert_raises_regex)
from spectra_analysis.preprocessing import *
from os.path import dirname, join
import numpy as np

test_path = dirname(__file__)
datafile = join(test_path, 'data', 'data.csv')
spectra, concentration, molecule = read_spectra(datafile)

X = np.array([[0, 0, 0],
                [0, 0, 0],
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
                [2, 2, 2]])

def test_fit_params():
    assert_allclose(spectra.values, X);
    pass


def test_transform():
    pass