import pytest

from fentongc.fentongc import calc_zscore


def test_calc_zscore_value_errors():
    with pytest.raises(ValueError, match=".*fake_metric.*"):
        calc_zscore("fake_metric", "m", 177, 2400.2)
    with pytest.raises(ValueError, match=".*fake_sex.*"):
        calc_zscore("weight", "fake_sex", 177, 2400.2)
    with pytest.raises(ValueError, match=".*164.*"):
        calc_zscore("length", "m", 164, 24.2)
    with pytest.raises(ValueError, match=".351.*"):
        calc_zscore("hc", "f", 351, 24.2)


def test_calc_zscore_good_params():
    assert calc_zscore("weight", "f", 171, 2400) == 1.2
    assert calc_zscore("wEIGHt", "F", 171.0, 2400) == 1.2