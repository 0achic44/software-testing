def ticket_fare(age=None, student=False):
    ticket_fare = 4
    if age and (age < 3 or age >= 65):
        return 0
    elif student and age < 19:
        return ticket_fare / 2
    return ticket_fare