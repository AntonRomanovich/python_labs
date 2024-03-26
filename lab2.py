input_number = int(input())
#с одним циклом for, так с одним циклом for
for i in range(input_number):
    if i != input_number:
        k = i
        while k < input_number:
            print(" ", end='')
            k += 1
    j = 0
    while j < i:
        print(j+1, end='')
        j += 1
    while j > -1:
        print(j+1, end='')
        j -= 1
    print('')