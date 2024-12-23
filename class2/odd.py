odd= int(input('Enter number to find how many odd num are '))
list = []
for num in range(odd):
    ran = num+1
    if ran % 2 == 1:
        list.append(ran)
print(list)  