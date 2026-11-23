def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "c"
    elif score >=60:
        return "D"
    else:
        return "F"

tokens=input().split()
valid_scores=[]
for token in tokens:
    if token.isdecimal():
        score=int(token)
        if 0<= score<=100:
            print(str(score) + ": " + grade(score))
            valid_scores.append(score)
        else:
            print(token + ": invalid")
    else:
             print(token + ": invalid")
if(len(valid_scores))>0:
    average=sum(valid_scores)/len(valid_scores)
    print("Average of valid scores: " + format(average, ".1f"))
else:
    print("No valid scores")