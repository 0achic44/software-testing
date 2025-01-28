import pytest
from person import Person

class TestPersonClass:
    
    def test_person_run_happy(self):
        p1 = Person("John", 140, 30, 20)
        assert p1.run(7)
    
    def test_person_run_sad(self):
        p1 = Person("John", 140, 30, 20)
        assert not p1.run(10)
    
    def test_person_run_hunger(self):
        p1 = Person("John", 140, 30, 20)
        p1.run(7)
        assert p1.hunger == 44
    
    def test_person_run_energy(self):
        p1 = Person("John", 140, 30, 20)
        p1.run(7)
        assert p1.energy == 6