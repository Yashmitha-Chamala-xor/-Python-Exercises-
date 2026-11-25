def c_to_f(c):
    return c*9/5+32
def c_to_k(c):
    return c+273.15
print(f"{'C':>5}{'F':>9}{'K':>9}")

for c in range(-20,41,10):
    f=c_to_f(c)
    k=c_to_k(c)
    print(f"{c:>5}{f:>9.1f}{k:>9.2f}")