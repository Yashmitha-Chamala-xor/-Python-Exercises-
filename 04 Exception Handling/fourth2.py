from pathlib import Path
 
def parse_readings(lines):
    values = []
    bad = []
 
    for number, line in enumerate(lines, start=1):
        text = line.strip()
        try:
            value = float(text)
        except ValueError:
            bad.append((number, text))
        else:
            values.append(value)
 
    return values, bad
 
path = Path("readings.txt")
lines = path.read_text(encoding="utf-8").splitlines()
values, bad = parse_readings(lines)
 
print("Lines:", len(lines))
print("Valid:", len(values))
 
invalid_numbers = []
for number, text in bad:
    invalid_numbers.append(number)
 
print("Invalid lines:", invalid_numbers)
 
for number, text in bad:
    print(f"  line {number}: {text!r}")
 
if values:
    average = sum(values) / len(values)
    print(f"Average: {average:.2f}")
    print(f"Min: {min(values)}  Max: {max(values)}")
else:
    print("No valid readings")