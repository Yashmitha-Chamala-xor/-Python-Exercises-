import sys
def divide_line(line):
    try:
        a_text,b_text=line.split()
        a=float(a_text)
        b=float(b_text)
        result=a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Invalid input: expected two numbers"
    else:
        return f"{a:g} / {b:g} = {result:g}"

all_input=sys.stdin.read()
for line in all_input.splitlines():
    if line.strip()=="":
        continue
    print(divide_line(line))

