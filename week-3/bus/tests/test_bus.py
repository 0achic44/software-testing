import pytest
import bus_ticket

def test_normal_ticket():
    assert bus_ticket.ticket_fare() == 4

def test_child_under_3_ticket():
    assert bus_ticket.ticket_fare(age=2) == 0

def test_student_under_19_ticket():
    assert bus_ticket.ticket_fare(age=18, student=True) == 2

def test_65_and_over_ticket():
    assert bus_ticket.ticket_fare(age=65) == 0