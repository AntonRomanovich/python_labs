input_number = int(input('Введите число '))
print('Ваша пирамида:')

for i in range(input_number):
    print(str(i+1) * (i+1))