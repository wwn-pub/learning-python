# list1 = ['sunday','june', 'may','summer','winter','september','rainy']
# # list_b = []
# # for m in list1:
# #     if 'm' not in m:
# #         list_b.append(m)
# # print(list_b)
# list_b = [ words for words in list1 if 'm' not in words ]
# print(list_b)

write = int(input('How many words you want to write '))
# add_list =[]
# for Spell in range(write):
#     learn = input('Write input:')
#     add_list.append(learn)
# print(add_list)
add_list = [input ('Write input') for Spell in range(write) ]
print(add_list)  
    