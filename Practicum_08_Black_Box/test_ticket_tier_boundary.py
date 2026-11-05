import pytest
from ticket_pricing import get_ticket_tier

# ---------- Boundary Value Analysis ----------

def test_boundary_0():
    assert get_ticket_tier(0) == "Last Minute"


def test_boundary_2():
    assert get_ticket_tier(2) == "Last Minute"


def test_boundary_3():
    assert get_ticket_tier(3) == "Late"


def test_boundary_14():
    assert get_ticket_tier(14) == "Late"


def test_boundary_15():
    assert get_ticket_tier(15) == "Regular"


def test_boundary_29():
    assert get_ticket_tier(29) == "Regular"


def test_boundary_30():
    assert get_ticket_tier(30) == "Early Bird"


def test_boundary_365():
    assert get_ticket_tier(365) == "Early Bird"


def test_boundary_minus_1():
    with pytest.raises(ValueError):
        get_ticket_tier(-1)


def test_boundary_366():
    with pytest.raises(ValueError):
        get_ticket_tier(366)
