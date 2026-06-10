"""

Modul1 mit der Funktionen function_RMSE()

2024-05-28 ug V0.1

"""


import numpy as np


def function_RMSE(y, y_pred):
    RMSE = np.sqrt(np.mean((y-y_pred)**2))
    return RMSE