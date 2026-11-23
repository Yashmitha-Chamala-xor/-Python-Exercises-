import json
 
sample = {
    "name": "Asha",
    "age": 30,
    "married": False,
    "scores": (90, 85),
    "nickname": None,
    "height": 1.68,
}
 
def roundtrip(obj):
    text = json.dumps(obj)
    return json.loads(text)
 
print("compact:", json.dumps(sample))
print("indented:")
print(json.dumps(sample, indent=2, sort_keys=True))
 
result = roundtrip(sample)
 
print("scores type before:", type(sample["scores"]).__name__,
      "| after:", type(result["scores"]).__name__)
print("married after:", result["married"],
      "| nickname after:", result["nickname"])
print("equal after round trip:", sample == result)
print("int keys:", roundtrip({1: "a", 2: "b"}))
 
try:
    json.dumps({"numbers": {1, 2, 3}})
except TypeError as error:
    print("TypeError:", error)