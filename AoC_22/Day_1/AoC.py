x = open("input.txt", "r")
data = x.read()
data_into_list = data.split("\n")
final = 0
sum_digit = 0
l = []
for x in data_into_list:
    if x.isdigit() == True:
        z = int(x)
        sum_digit = sum_digit + z
        
    else:
        l.append(sum_digit)
        if sum_digit > final:
            final = sum_digit 
        sum_digit = 0
l.sort(reverse=True)
print(l)
print(sum(l[0:3]))
