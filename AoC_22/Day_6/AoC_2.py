text = open("Day_6/input.txt", "r").read().split('\n')[0]
i = 0
while i < len(text):
        if len(set(text[i:i+14])) == 14:
            print(i+14)
            break
        i = i + 1    
            

