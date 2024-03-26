def cap(someString):
    out = someString.capitalize()
    j = 0
    for i in someString:
        if i == " ":
            out = out[:j] + i + someString[j+1:].capitalize()
        j += 1
    return out

str1 = input('Введите первую строку - ')
print("AFTER:")
str2 = input('Введите вторую строку - ')

print(cap(str1))
print("AFTER:")
print(cap(str2))