def extractDigit(s):
    digit=''
    for i in s:
        if i in '0123456789':
            digit+=i
    return digit


str1=input()
a=extract_digits(str1)
print("No of digits in:'",str1,"' is",a)
