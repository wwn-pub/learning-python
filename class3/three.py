words = int(input('How many words you want to enter? '))
list_w = []
list_b = []
list_all =[]
for let in range (words):
    in_words = input(f'{let+1}: ')
    list_all.append(in_words)
    if 'b' not in in_words:
        list_w.append(in_words)
    else:    
        list_b.append(in_words)
print(list_w)
print(list_b)
print(list_all)
