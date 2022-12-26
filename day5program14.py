def count_consonant(s):
    consonant=0
    for i in s:
        if i in 'BCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz':
            consonant+=1
    return consonant
str1=input()
a=count_consonant(str1)
print("No of Consonants in:'",str1,"' is",a)

