text = open("Day_2/input.txt", "r").read().split("\n")
def mode(foo):
    return {
        'X': 1, #Lose
        'Y': 2, #Draw
        'Z': 3 #Win
    }[foo]

def score(foo):
    return {
        'A': 1, #Rock
        'B': 2, #Paper
        'C': 3 #Scissors
    }[foo]

def win(foo):
    return {
        'A' : 'B',
        'B' : 'C',
        'C' : 'A'
    }[foo]

def lose(foo):
    return {
        'B' : 'A',
        'C' : 'B',
        'A' : 'C'
    }[foo]

def game(foo):
    match mode(foo[2]):
        case 1: return score(lose(foo[0]))
        case 2: return score(foo[0]) + 3
        case 3: return score(win(foo[0])) + 6

y = 0
for x in text:
    y = y + game(x)
print(y)