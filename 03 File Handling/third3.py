from pathlib import Path
 
def append_entry(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(text + "\n")
 
def count_lines(path):
    path = Path(path)
    if not path.exists():
        return 0
    with open(path, encoding="utf-8") as f:
        return sum(1 for _ in f)
 
path = Path("output/journal.txt")
path.unlink(missing_ok=True)
 
print("Lines before:", count_lines(path))
 
append_entry(path, "Started the course")
append_entry(path, "Finished file exercises")
append_entry(path, "Reviewed CSV handling")
print("Lines after first run:", count_lines(path))
 
append_entry(path, "Added one more entry")
print("Lines after append:", count_lines(path))
 
print(path.read_text(encoding="utf-8"), end="")