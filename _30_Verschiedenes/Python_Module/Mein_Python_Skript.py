"""

Mein Python Skript welches die Modul1 mit der Funktionen function_RMSE()

2026-06-10 ug V1.0

"""


import numpy as np

from Modul1 import function_RMSE

from Paket2.Modul2 import function_multiplikation, function_division

import Paket2.Modul2 as P2M2

def main():

    # Aufruf der Funktion function_RMSE() aus Modul1
    y = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.1, 1.9, 3.2, 3.8, 5.1])
    RMSE = function_RMSE(y, y_pred)
    print("RMSE:", RMSE)

    # Lesen der globale_variable aus Modul2
    print(P2M2.globale_variable)

    ergebnis1 = P2M2.function_multiplikation(3,4)
    print(f'Ergebnis1: {ergebnis1}')

    ergebnis2 = P2M2.function_division(10,2)
    print(f'Ergebnis2: {ergebnis2}')

if __name__ == "__main__":
    main()