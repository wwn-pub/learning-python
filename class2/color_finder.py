# output : repeated clor should not appear in list
list1 =['red','black','orange','green']
list2 =['pink','white','blue','green']
list =[]
for color in list1:
    if color not in list2:
      list.append(color)
    else:
        print(f'this {color} color found in list two')
print(list)

          
