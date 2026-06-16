from src import inc_dec


def test_increment():
    assert inc_dec.increment(3) == 4


def test_decrement():
    assert inc_dec.decrement(3) == 2


def test_decrement2():
    # todo: hier könnte was schief laufen
    assert inc_dec.decrement(4) == 2

    # Korrektur:
    #assert inc_dec.decrement(4) == 3
