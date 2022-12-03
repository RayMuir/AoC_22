import string
text = open("Day_3/input.txt", "r").read().split("\n")
letters = list(string.ascii_lowercase + string.ascii_uppercase)
sum = 0

def foo(x):
    first, second = x[:len(x)//2], x[len(x)//2:]
    for y in first:
        for z in second:
            if y == z:
                return letters.index(z) + 1
                
for x in text:
    sum = sum + foo(x)

print(sum)