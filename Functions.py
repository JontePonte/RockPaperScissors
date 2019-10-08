
# testa vinnare den hårda vägen
def test(f, s):
    res = 0
    if f == 1:  # ifall first = rock
        if s == 1:
            res = 0  # second = rock, lika
        elif s == 2:
            res = 2  # second = paper, second vinner
        else:
            res = 1  # annars, first vinner

    elif f == 2:  # ifall first = paper
        if s == 2:
            res = 0  # second = paper, lika
        elif s == 3:
            res = 2  # second = scissors, second vinner
        else:
            res = 1  # annars, first vinner

    elif f == 3:  # ifall first = scissors
        if s == 3:
            res = 0  # second = scissors, lika
        elif s == 1:
            res = 2  # second = rock, second vinner
        else:
            res = 1  # annars, first vinner

    else:  # ifall first = 0
        res = 2  # second vinner

    return res