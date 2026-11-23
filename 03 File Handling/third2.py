from pathlib import Path
def write_squares(path, n):
    path=Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path,"w",encoding="utf-8") as f:
        for i in range(1,n+1):
            f.write(f"{i} squared is {i ** 2}\n")
    return n
path=Path("output/squares.txt")
lines=write_squares(path,8)
print("Lines written:" ,lines)
print(path.read_text(encoding="utf-8"),end="")