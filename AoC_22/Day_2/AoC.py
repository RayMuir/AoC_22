text = open("Day_2/input.txt", "r").read().split("\n")
def score(foo):
    return {
        'X': 1, #Rock
        'Y': 2, #Paper
        'Z': 3 #Scissors
    }[foo]

def score2(foo):
    return {
        'A': 1, #Rock
        'B': 2, #Paper
        'C': 3 #Scissors
    }[foo]

def rules(foo):

        if foo[0] == 'A' and foo[2] == 'Y': return 8
        elif foo[0] == 'B' and foo[2] == 'Z': return 9
        elif foo[0] == 'C' and foo[2] == 'X': return 7
        elif score2(foo[0]) == score(foo[2]): return score(foo[2]) + 3
        else: return score(foo[2])

y = 0
for x in text:
    y = y + rules(x)
print(y)