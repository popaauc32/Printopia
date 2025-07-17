
#Fibonacci n- 1 + n-2

n = 10


f0 = 0
f1 = 1

if n == 0:
    rezultat = f0
elif n == 1:
    rezultat = f1
else:
    for i in range(2, n + 1):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    rezultat = f2


print(f"F({n}) = {rezultat}")