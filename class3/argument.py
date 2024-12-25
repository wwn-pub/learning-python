import sys
# print(sys.argv)
# total = 0
# for tea in sys.argv:
#     print(tea)
# print (len(sys.argv))  
# for add in sys.argv[1:]:
#     total =  total + int(add)
# print(total)
# print(sys.argv[2])
# replace value
# sys.argv[1] = 'sonam'
# print(sys.argv)

l = sys.argv
# print(l)
# for num in l:
#     print(num)
# print individual items from list
try:
    print(l[2])
    l[5] ='shiv'
except:
    print('List only has index up to 4.')    


    