input_number = int(input('Введите число '))
print('Ваша пирамида:')

for i in range(input_number):
    for j in range(i+1):
        print(j+1, end='')
    for j in range(i+1, -1, -1):
        print(j+1, end='')
    print('')