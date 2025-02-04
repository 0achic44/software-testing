def delivery(miles, value):
    if miles <= 10 and value >= 100:
        return 0
    elif miles <= 10 and value > 100:
        return 5