text = open("input.txt", "r").read().split("\n\n")
text = sorted([sum(map(int, filter(str.isdigit, x.split()))) for x in text], reverse=True)
print(text[0])
print(sum(text[:3]))