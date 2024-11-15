import pytest
import geo.arccos

# ---------------------------------------------------
# Tests where x=0
# for arccos, rad_to_deg, deg_to_rad
def test_arccos_zero():
    rad = geo.arccos.arccos(0, 10)
    assert rad == pytest.approx(1.570796)

def test_rad_to_deg_zero():
    rad = geo.arccos.arccos(0, 10)
    deg = geo.arccos.rad_to_deg(rad)
    assert deg == pytest.approx(90)

def test_deg_to_rad_zero():
    rad = geo.arccos.arccos(0, 10)
    deg = geo.arccos.rad_to_deg(rad)
    to_rad = geo.arccos.deg_to_rad(deg)
    assert geo.arccos.deg_to_rad(to_rad) == pytest.approx(0.02741556)


# ---------------------------------------------------
# Tests where x>0 and x<1
# for arccos, rad_to_deg, deg_to_rad
def test_arccos_positive():
    rad = geo.arccos.arccos(0.3, 10)
    assert rad == pytest.approx(1.266636)

def test_rad_to_deg_positive():
    rad = geo.arccos.arccos(0.3, 10)
    deg = geo.arccos.rad_to_deg(rad)
    assert deg == pytest.approx(72.5729)

def test_deg_to_rad_positive():
    rad = geo.arccos.arccos(0.3)
    deg = geo.arccos.rad_to_deg(rad)
    to_rad = geo.arccos.deg_to_rad(deg)
    assert to_rad == pytest.approx(1.266636)


# ---------------------------------------------------
# Tests where x>-1 and x<0
# for arccos, rad_to_deg, deg_to_rad
def test_arccos_negative():
    rad = geo.arccos.arccos(-0.6)
    assert rad == pytest.approx(2.197712)

def test_rad_to_deg_negative():
    rad = geo.arccos.arccos(-0.6)
    deg = geo.arccos.rad_to_deg(rad)
    assert deg == pytest.approx(125.9196)

def test_deg_to_rad_negative():
    rad = geo.arccos.arccos(-0.6, 10)
    deg = geo.arccos.rad_to_deg(rad)
    to_rad = geo.arccos.deg_to_rad(deg)
    assert to_rad == pytest.approx(2.197712)


# ---------------------------------------------------
# Tests where x=1
# for arccos, rad_to_deg, deg_to_rad
def test_arccos_one():
    rad = geo.arccos.arccos(1)
    assert rad == pytest.approx(0)

def test_rad_to_deg_one():
    rad = geo.arccos.arccos(1)
    deg = geo.arccos.rad_to_deg(rad)
    assert deg == pytest.approx(0)

def test_deg_to_rad_one():
    rad = geo.arccos.arccos(1)
    deg = geo.arccos.rad_to_deg(rad)
    to_rad = geo.arccos.deg_to_rad(deg)
    assert to_rad == pytest.approx(0)