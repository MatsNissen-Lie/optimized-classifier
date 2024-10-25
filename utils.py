import numpy as np


def calculate_error_rate(y_pred, y, test_type=""):
    num_errors = np.sum(y_pred != y)
    n = y_pred.shape[0]
    error_rate = (num_errors / n) * 100
    print(f"{test_type} error rate: {error_rate:.2f}%")
