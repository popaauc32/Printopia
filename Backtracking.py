def fibonacci_backtracking(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_backtracking(n - 1) + fibonacci_backtracking(n - 2)

# Exemplu de utilizare
n = 10
rezultat = fibonacci_backtracking(n)
print(f"F({n}) = {rezultat}")