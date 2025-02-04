def speeding(speed):
    speed_limit = 30
    if speed - speed_limit > 10:
        return (True, True)
    elif speed - speed_limit > 0:
        return (True, False)
    else:
        return (False, False)