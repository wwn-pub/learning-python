alpha = input('write spelling to find number of vowel and consonant ')
print(alpha)
vowel= 0
Consonant =0
for letter in alpha:
    # print(letter)
    if letter in ["a","e","i","o","u"]:
        vowel = vowel+1
    else:
        Consonant = Consonant+1
print(f'vowel = {vowel}, consonant = {Consonant}')        
        
        
        
    