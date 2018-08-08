import os
import subprocess
import pytest
from terraref.laser3d import GeotiffStats, fit_rleafangle_tiff

dire = os.path.join(os.path.dirname(__file__), 'data/')


@pytest.fixture(scope='module')
def read_metadata():
    return dire + 'scanner3DTop_L2_ua-mac_2018-07-08__04-51-55-343_heightmap.tif'


def test_geotiffstats(read_metadata):
    geostatsObject = GeotiffStats(read_metadata)
    assert len(geostatsObject.sample_geotiff()) == 1000
    assert geostatsObject.mean_geotiff() > 2.6
    assert geostatsObject.var_geotiff() < 0.184


def test_fit_leafangle_tiff(read_metadata):
    df = fit_rleafangle_tiff(read_metadata)
    assert df['mean'][1] < 90.


if __name__ == '__main__':
    subprocess.call(['python -m pytest test_laser3d_stats.py -p no:cacheprovider'], shell=True)