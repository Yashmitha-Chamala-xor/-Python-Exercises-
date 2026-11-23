def fizzbuzz(n):
    result=[]
    for number in range(1,n+1):
        if number%3==0 and number%5==0:
            result.append("FizzBuzz")
        elif number%3==0:
            result.append("Fizz")
        elif number%5==0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return result
n=int(input())
for item in fizzbuzz(n):
    print(item)
