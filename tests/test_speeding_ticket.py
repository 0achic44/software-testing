import pytest
import speeding_ticket

def test_speeding_by_more_than_10():
    assert speeding_ticket.speeding(41) == (True, True)

def test_speeding_by_10_or_less():
    assert speeding_ticket.speeding(40) == (True, False)

def test_not_speeding():
    assert speeding_ticket.speeding(30) == (False, False)