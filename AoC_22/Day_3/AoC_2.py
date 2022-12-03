import string
text = open("Day_3/input.txt", "r").read().split("\n")
letters = list(string.ascii_lowercase + string.ascii_uppercase)
sum = 0

def foo(first, second, third):
    for y in first:
        for z in second:
            if y == z:
                for a in third:
                    if z == a:
                        return letters.index(a) + 1
i = 0
while i < len(text):
    sum = sum + foo(text[i], text[i+1], text[i+2])
    i += 3

print(sum)