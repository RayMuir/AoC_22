text = open("Day_6/input.txt", "r").read().split('\n')[0]
i = 0
while i < len(text):
        if len(set(text[i:i+4])) == 4:
            print(i+4)
            break
        i = i + 1    
            

