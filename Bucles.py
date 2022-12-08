# def main():
#     MAXI = 1000
#     i = 1
#     while i <= MAXI:
#         print ('Este es el número: ' + str(i))
#         i = i + 1


# if _name_ == '_main_':
#     main()


def main():
    # print('\t\tESTAS SON LAS TABLAS DE MULTIPLICAR HASTA EL 10\n')
    print('\033[95m' + '\033[4m' + '\t\tESTAS SON LAS TABLAS DE MULTIPLICAR HASTA EL 10\n' + '\033[0m')
    x = 0
    i = 0
    for i in range(1, 11):
        print('\n', end=' ')
        for x in range(1,11):
            resultado = x * i
            # print(str(x) + 'x' + str(i) + '=' + f'{str(resultado):10}', end=' ')
            print('{0:1.5}x{1:2}={2:3}'.format(str(x), str(i), str(resultado)), end=' ')
            # {0} and {1}'.format('spam', 'eggs')


if __name__ == '__main__':
    main()

