
from spectra_analysis.preprocessing import read_spectra
from os.path import dirname, join

def test_read_spectra():
    test_path = dirname(__file__)
    # Write here the tests for the normal conditions
    datafile = join(test_path, 'data', 'data.csv')
    spectra, concentration, molecule = read_spectra(datafile)
    
    pass


def test_read_spectra_exceptions():
    # Write here the tests to handle errors
    pass