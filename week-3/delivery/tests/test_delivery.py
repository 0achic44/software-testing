import pytest
import delivery_price

def test_delivery_up_to_10_miles_and_over_100():
    assert delivery_price.delivery(10, 101) == 0

def test_delivery_up_to_10_miles_and_less_than_100():
    assert delivery_price.delivery(10, 99) == 5