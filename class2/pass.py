import secrets
import string
password=''
pass_wrd =int(input('Digit of words/num required for password gen '))
if pass_wrd >=5:
  for dec in range(pass_wrd):
        password = password+str(secrets.choice(string.ascii_letters + string.digits + string.punctuation))
else:
      print('minimam 4 digits required.')
print(password)

