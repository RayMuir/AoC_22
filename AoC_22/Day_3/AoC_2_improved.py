import string
text = open("Day_3/input.txt", "r").read().split("\n")
letters = list(string.ascii_lowercase + string.ascii_uppercase)
sum = 0

def foo(first, second, third):
    d = set(first) & set(second) & set(third)
    return letters.index(next(iter(d))) + 1

i = 0
while i < len(text):
    sum = sum + foo(text[i], text[i+1], text[i+2])
    i += 3

print(sum)