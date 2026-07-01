
# src/add.py - das ist die Funktion, die wir testen wollen

#  die print-Anweisung wird beim Importieren der Datei ausgeführt, nicht nur beim direkten Ausführen
print(f"add.py wird ausgeführt  {__name__=}")

def addition(x, y):
    """
    Addiere zwei Zahlen x und y.
    Args:
        x (int or float): Die erste Zahl.
        y (int or float): Die zweite Zahl.
    Returns:
        int or float: Die Summe von x und y.
    """
    return x + y

print("add.py wird verlassen")