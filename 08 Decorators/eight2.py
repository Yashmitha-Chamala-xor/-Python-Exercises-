def make_counter(start=0, step=1):
    count = start - step
 
    def counter():
        nonlocal count
        count += step
        return count
 
    return counter
 
 
def make_multiplier(n):
    def multiply(x):
        return x * n
 
    return multiply
 
 
def build_multipliers(factors):
    result = []
    for factor in factors:
        result.append(make_multiplier(factor))
    return result
 
 
c1 = make_counter()
c2 = make_counter(start=10, step=5)
print(c1(), c1(), c1())
print(c2(), c2())
 
double = make_multiplier(2)
print(double(21))
print([f(10) for f in build_multipliers([2, 3, 4])])
print(double.__closure__[0].cell_contents)
 
broken = [lambda x: x * factor for factor in [2, 3, 4]]
print([f(10) for f in broken])