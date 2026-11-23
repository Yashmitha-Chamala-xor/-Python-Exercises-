def file_stats(path):
    stats={"lines":0,"words":0,"characters":0,"blank":0}
    with open(path,encoding="utf-8") as f:
        for line in f:
            text=line.rstrip("/n")
            stats["lines"] +=1
            stats["words"] += len(text.split())
            stats["characters"] += len(text)
            if text.strip()=="":
                stats["blank"] += 1
    return stats

path="notes.txt"

with open(path,encoding="utf-8") as f:
    for number,line in enumerate(f,start=1):
        
        if number> 5:
            break
        text=line.rstrip("/n")
        print(f"{number}: {text}")


stats=file_stats(path)
print("Lines:",stats["lines"])
print("Words:",stats["words"])
print("Characters:",stats["characters"])
print("Blank lines:",stats["blank"])



      
