
import numpy as np


def function_MSE_Paket1(y, y_pred):
    RMSE = np.mean((y-y_pred)**2)
    return RMSE