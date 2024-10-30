import os
import pytest
import earthaccess
import py4eos
from py4eos import read_hdf4eos

TEST_DIR = os.path.join(os.path.dirname(py4eos.__file__), 'tests')

@pytest.fixture
def granule_mod16a3():
    filename = f'{TEST_DIR}/MOD16A3GF.A2014001.h10v04.061.2022077145846.hdf'
    if not os.path.exists(filename):
        results = earthaccess.search_data(
            short_name = 'MOD16A3GF',
            temporal = ('2014-01-01', '2014-12-31'),
            bounding_box = (-106, 42, -103, 43))
        earthaccess.download(results, TEST_DIR)
        return f'{TEST_DIR}/{results[0]["meta"]["native-id"]}'
    return filename


def test_read_mod16a3(granule_mod16a3):
    '''
    Tests that a MOD16A3 granule can be read and handled.
    '''
    hdf = read_hdf4eos(granule_mod16a3)
    assert hdf.transform.to_gdal() == hdf.geotransform
    assert hdf.transform.to_gdal() == (-8895604.157333, 500.0, 0.0, 5559752.598333, 0.0, -500.0)
