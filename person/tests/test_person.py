import pytest
from person import Person

def test_person_name():
    p1 = Person("John", 140, 30, 20)
    assert p1.name == "John"

def test_person_weight():
    p1 = Person("John", 140, 30, 20)
    assert p1.weight == 140

def test_person_hunger():
    p1 = Person("John", 140, 30, 20)
    assert p1.hunger == 30

def test_person_energy():
    p1 = Person("John", 140, 30, 20)
    assert p1.energy == 20

def test_person_hunger_below_0_sad():
    with pytest.raises(Exception) as ex:
        p1 = Person("John", 140, -1, 20)
    assert str(ex.value) == "Hunger must be between 0 and 100"

def test_person_hunger_above_100_sad():
    with pytest.raises(Exception) as ex:
        p1 = Person("John", 140, 101, 20)
    assert str(ex.value) == "Hunger must be between 0 and 100"

def test_person_hunger_is_0_boundary():
    p1 = Person("John", 140, 0, 20)
    assert p1.hunger == 0

def test_person_hunger_is_100_boundary():
    p1 = Person("John", 140, 100, 20)
    assert p1.hunger == 100