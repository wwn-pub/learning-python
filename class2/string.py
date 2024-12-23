items = int(input('How many items do you want to enter '))
list_ofitems = []
for home in range(items):
    item_name = input(f'Enter item {home + 1} ')
    list_ofitems.append(item_name)
print(list_ofitems)
    
    