import pytest
from ticket_pricing import get_ticket_tier

# ---------- Equivalence Partitioning ----------

def test_valid_partition_early_bird():
    assert get_ticket_tier(60) == "Early Bird"


def test_valid_partition_regular():
    assert get_ticket_tier(20) == "Regular"


def test_valid_partition_late():
    assert get_ticket_tier(5) == "Late"


def test_valid_partition_last_minute():
    assert get_ticket_tier(1) == "Last Minute"


def test_invalid_partition_below_range():
    with pytest.raises(ValueError):
        get_ticket_tier(-10)


def test_invalid_partition_above_range():
    with pytest.raises(ValueError):
        get_ticket_tier(400)
