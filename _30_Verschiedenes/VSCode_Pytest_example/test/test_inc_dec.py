
# Test der Funktionen increment und decrement aus src\inc_dec.py

from src import inc_dec


def test_increment():
    # Testfall 1: Überprüfen, ob die Inkrementierung korrekt ist
    assert inc_dec.increment(3) == 4


def test_decrement():
    # Testfall 1: Überprüfen, ob die Dekrementierung korrekt ist
    assert inc_dec.decrement(3) == 2


def test_decrement2():
    #
    # todo: hier könnte was schief laufen
    assert inc_dec.decrement(4) == 2

    # Korrektur:
    #assert inc_dec.decrement(4) == 3
