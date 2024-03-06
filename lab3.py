def cap(someString):
    if someString.isupper():
        return someString
    else:
        out = someString.capitalize()
        j = 0
        for i in someString:
            if i == " ":
                out = out[:j] + i + someString[j+1:].capitalize()
            j += 1
        return out

str1 = input('Введите первую строку - ')
str2 = input('Введите вторую строку - ')
str3 = input('Введите третью строку - ')

print(cap(str1))
print(cap(str2))
print(cap(str3))