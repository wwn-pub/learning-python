# country = input('Enter your country ')
# city = input('Enter your city ')
# # print(city ,'is inside', country, '.')
# print(f"{city} is inside {country} .")

try:
    income =int(input('Wanna know your place in society enter your montly income '))
    if income<=5000:
        print('You are poor')
    elif income>5000 and income<=15000:
        print('You belong to middel class.')
    elif income>15000 and income<=25000:
        print('You belong to upper middle class.') 
    else:
        print('your are rich.')
except:
    print("The input should be a valid integer")
