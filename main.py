balance = 0
depositos = []
saques = []
quantidades_saques = 0
def deposito():
    global balance
    global depositos
    print("Depósito selecionado. \n")

    valor = int(input('Insira o valor do depósito: '))
    balance += valor
    depositos.append(valor)
    options()

def saque():
    global quantidades_saques
    global saques
    global balance

    valor = int(input("Insira o valor do saque : "))
    if valor <= 500:
        if quantidades_saques < 3:
            if balance >= valor:
                balance -= valor
                saques.append(valor)
                quantidades_saques += 1
                options()
            else:

                print('Saldo da conta não é suficiente para este valor de saque')
                escolha =  input('Deseja realizar outra operação ? S/N')
                if escolha.upper() == 'S':
                    options()
                else:
                    pass
        else:
            print("Limite de saques diários atingido")
            escolha =  input('Deseja realizar outra operação ? S/N')
            if escolha.upper() == 'S':
                options()
            else:
                pass
    else:
        print("Limite de saque é de R$500,00")
        escolha =  input('Deseja realizar outra operação ? S/N')
        if escolha.upper() == 'S':
            options()
        else:
            pass



def extrato():

    if len(depositos) or len(saques) > 0:

        print('Depósitos efetuados: ')

        for i in range(len(depositos)):
            print(f'{i+1} - {depositos[i]}')
        print(f"Total depositado: R${sum(depositos)}")

        print('Saques Efetuados: ')

        for i in range(len(saques)):
            print(f'{i+1} - {saques[i]}')
        print(f"Total sacado: R${sum(saques)}")
        print(f"Balanço da conta: R${balance}")


    else:
        print("Não foram realizadas transações")


    escolha =  input('Deseja realizar outra operação ? S/N')

    while escolha.upper() != 'S' or escolha.upper() != 'N':
        escolha = input("Escolha inválida, escolha uma opção entre S/N")
        if escolha.upper() == 'S':
            options()
        else:
            pass

    if escolha.upper() == 'S':
            options()
    else:
        pass



def options():
    options_list = ['Depósito', 'Saque', 'Extrato', 'Sair']
    values = [1,2,3,4]
    for i, option in zip(values,options_list):
        print(f'{i} - ',option)

    print('\n')

    x = int(input("Escolha uma das opções acima : "))


    while x not in values :

        print("Opção inválida, escolha uma das opções abaixo.")

        for i, option in zip(values,options_list):
            print(f'{i} - ',option)

        x = int(input("Escolha uma das opções acima : "))

    if x == 1:
        deposito()
    elif x == 2:
        saque()
    elif x == 3:
        extrato()
    else:
        pass



options()

