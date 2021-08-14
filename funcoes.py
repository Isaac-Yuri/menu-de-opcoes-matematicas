'''Menu opções:
1. Verifique se um número é par ou ímpar
2. Multiplicar dois números
3. Dividir dois números
4. Raiz quadrada de um número
5. Elevar um número a uma potência
6. Sair
'''

def menu():
    '''Cria um menu de opções'''
    print('''1. Verifique se um número é par ou ímpar
2. Multiplicar dois números
3. Dividir dois números
4. Raiz quadrada de um número
5. Elevar um número a uma potência
6. Sair''')

def linha(n_de_linhas=20):
    '''Cria uma linha
    n_de_linhas: informe quantas linhas deseja'''
    print('-='*n_de_linhas)

def continuar():
    cont = input('Deseja continuar? [S/N] ').upper()
    while cont not in 'SN' or cont == '':
        cont = input('Deseja continuar? [S/N] ').upper()
    if cont == 'N':
        return True