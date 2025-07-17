import numpy as np

def fibonacci(n):
    if n == 0:
        return 0
    F = np.array([[1, 1], [1, 0]], dtype=object)
    result = np.linalg.matrix_power(F, n - 1)
    return result[0][0]

n = 10
print(f"F({n}) = {fibonacci(n)}")