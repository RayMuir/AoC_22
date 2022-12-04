import re
text = open("Day_4/input.txt", "r").read().split('\n')
y = []
for x in text:
    y.append(re.split(',', x))
count = 0
intersection = 0
for x in y:  
    foo = x[0].split("-")
    bar = x[1].split("-")
    foo1 = set(range(int(foo[0]), int(foo[1])+1))
    bar1 = set(range(int(bar[0]), int(bar[1])+1))
    if foo1.issubset(bar1) or bar1.issubset(foo1): count = count + 1
    if len(foo1.intersection(bar1)) > 0:
        intersection = intersection + 1

print(count)
print(intersection)