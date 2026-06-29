
import pytest

# Test der Funktion addiere aus src\add.py
from src import add

def test_answer():
    # Testfall 1: Überprüfen, ob die Addition korrekt ist
    assert add.addition(3, 1) == 4


def test_answer2():
    # Testfall 2: Überprüfen, ob die Addition mit negativen Zahlen korrekt ist
    assert add.addition(-1, 1) == 0

# -------
# Testfall mit Parametrisierung
# https://docs.pytest.org/en/7.4.x/parametrize.html 
# mit Fehler: 6 + 9 = 15, nicht 42
# Fehler: @pytest.mark.parametrize("input1,input2,expected", [(3, 5, 8), (2, 4, 6), (6, 9, 42)])
# korrekt: @pytest.mark.parametrize("input1,input2,expected", [(3, 5, 8), (2, 4, 6), (6, 9, 15)])
@pytest.mark.parametrize("input1,input2,expected", [(3, 5, 8), (2, 4, 6), (6, 9, 42)])
def test_answer3(input1, input2, expected):
    assert add.addition(input1, input2) == expected

# Testfall mit langer Liste von Parametern:
list_of_parameters = [
    (3, 5, 8),
    (2, 4, 6),
    (6, 9, 15),
    (-1, 9, 8),
    (-1, -9, -10),
    (0, 0, 0),  
]

@pytest.mark.parametrize("input1,input2,expected", list_of_parameters)
def test_answer4(input1, input2, expected):
    assert add.addition(input1, input2) == expected