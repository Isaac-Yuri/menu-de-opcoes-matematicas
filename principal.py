from funcoes import menu, linha, continuar
from math import sqrt

while True:
    print('== SUAS OPÇOES ==')
    menu()
    linha(23)
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        while True:
            num = int(input('Digite um número para checar se é par ou ìmpar: '))
            linha()
            print(f'O número {num} é ', end='')
            if num % 2 == 0:
                print('PAR!')
            else:
                print('ÍMPAR!')
            if continuar():
                break

    elif opcao == 2:
        while True:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite outro número: '))
            linha()
            print(f'{num1} multiplicado por {num2} é {num1*num2}.')
            if continuar():
                break
        
    elif opcao == 3:
        while True:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite outro número: '))
            linha()
            print(f'{num1} divido por {num2} é {num1/num2}.')
            if continuar():
                break

    elif opcao == 4:
        while True:
            num = int(input('Digite um número para ver sua raiz quadrada: '))
            linha()
            print(f'A raiz quadrada de {num} é {sqrt(num)}.')
            if continuar():
                break

    elif opcao == 5:
        while True:
            num = int(input('Digite um número: '))
            potencia = int(input('A qual potência deseja que seu número seja elevado? '))
            print(f'{num} elevado a {potencia} é igual a {num**potencia}.')
            if continuar():
                break

    elif opcao == 6:
        break

    else:
        print('Digite uma opção válida!')
    
    linha()
