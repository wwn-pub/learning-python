# purpose: extract r and a from the stirng
dialouge = 'we are going to Malta for New year cleberation'
dialouge_list = dialouge.split(sep=' ')
blank = []
for x in dialouge_list:
    if 'r' in x or 'b' in x:
        continue
    else:
        blank.append(x)
print(blank)
        
    
