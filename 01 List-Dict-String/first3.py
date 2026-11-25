def mask_card(number):
    return "*" * (len(number)-4) + number[-4:]

def reverse_words(sentence):
    word=sentence.split()
    return " ".join(word[::-1])

def middle(text):
    mid=len(text)//2
    if len(text)%2==1:
        return text[mid]
    return text[mid-1:mid+1]

def every_other(text):
    return text[::2]

print(mask_card("4111111111111111"))
print(reverse_words("learning python is fun"))
print(middle("python"), middle("slicing"))
print(every_other("abcdefghij"))
print("Programming"[::-1])
