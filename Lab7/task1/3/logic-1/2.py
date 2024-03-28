def caught_speeding(speed, is_birthday):
    res = 0
    if not is_birthday:
        if speed <= 60:
        res = 0
        elif speed >= 61 and speed <= 80:
        res = 1
        elif speed >= 81:
        res = 2
    else:
        if speed <= 65:
        res = 0
        elif speed >= 66 and speed <= 85:
        res = 1
        elif speed >= 86:
        res = 2
    return res 