import re
from collections import deque
text = open("Day_5/input.txt", "r").read().split('\n')
arr = []
for q in range(9):
    arr.append(deque([]))

for x in text:
    if x[0] == '[' or x[0] == ' ':
        i = 1
        arri = 0
        while i < len(x):
            if x[i] != ' ':
                arr[arri].append(x[i])      
            arri = arri + 1
            i = i + 4
    else: 
        foo = re.findall('\d+', x )
        temp = deque([])
        for index in range(int(foo[0])):           
            
            temp.appendleft(arr[int(foo[1])-1].popleft())
        for index in range(int(foo[0])):  
            arr[int(foo[2])-1].appendleft(temp.popleft())    
            

for y in arr:
    print(y.popleft(), end="")
           
            

