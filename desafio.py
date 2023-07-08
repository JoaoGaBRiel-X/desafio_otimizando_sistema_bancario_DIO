import string

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[i] Lista Clientes
[t] Cadastrar Conta
[r] Lista Contas
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_clientes = []
lista_contas = []

def saque(*, valor, numero_saques, saldo, limite, extrato):
    if valor <= 0:
        print("Valor inválido!")
        print("Por favor, refaça a operação")
    else:
        if numero_saques < LIMITE_SAQUES:
            if valor <= saldo:
                if valor <= limite:
                    extrato += f"\nSaque de R$ {valor:.2f}"
                    saldo -= valor
                    numero_saques += 1
                    print(f"Saque de R$ {valor:.2f} realizado com Sucesso!")
                    return saldo, extrato, numero_saques
                else:
                    print("OPERAÇÃO CANCELADA!")
                    print(f"Valor de R$ {valor:.2f} excede o limite liberado de R$ {limite:.2f} por operação.")
            else:
                print("OPERAÇÃO CANCELADA!")
                print(f"Saldo insuficiente para realizar operação.")
                print(f"Saldo atual é de R$ {saldo:.2f}")
        else:
            print("OPERAÇÃO CANCELADA!")
            print(f"Limite diário de {LIMITE_SAQUES} saques foi atingido!")

def deposito(valor, saldo, extrato, /):
    if valor_deposito <= 0:
        print("Valor inválido!")
        print("Por favor, refaça a operação")
    else:
        extrato += f"\nDepósito de R$ {valor_deposito:.2f}"
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com Sucesso!")
        return saldo, extrato

def movimentacao(valor, funcao):
    global numero_saques
    global saldo
    global limite
    global extrato

    if funcao == saque:
        ret_operacao = saque(valor=valor, numero_saques=numero_saques, saldo=saldo, limite=limite, extrato=extrato)
        
    if funcao == deposito:
        ret_operacao = deposito(valor, saldo, extrato)

    if ret_operacao != None:
            saldo = ret_operacao[0]
            extrato = ret_operacao[1]
            if funcao == saque: numero_saques = ret_operacao[2]

def extrato_conta(saldo, /, *, extrato):
    print("*************** EXTRATO ***************")
    print("Sem movimentação." if not extrato else extrato)
    print(f"\nSALDO ATUAL R$ {saldo:.2f}")
    print("***************************************")

def cadastra_cliente(*,cpf, lista):
    cpf = cpf.translate(str.maketrans('','',string.punctuation))
    encontrados = [c for c in lista_clientes if c["cpf"] == cpf]
    if(encontrados == []):
        nome_cliente = input("Digite seu nome completo: ")
        data_nascimento = input("Digite sua data de nascimento (Ex: dd/mm/aaaa): ")
        endereco = input("Digite seu endereço completo (Ex: logradouro, nro - bairro - cidade/sigla estado): ")
        lista.append({"cliente": nome_cliente, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print(f"Cliente {nome_cliente} cadastrado com Sucesso!")
    else:
        print("OPERAÇÃO CANCELADA!")
        print(f"Já existe um cliente com CPF {cpf} cadastrado no sistema.")

def criar_conta(*, cpf_cliente, lista_contas, lista_clientes):
    cpf_cliente = cpf.translate(str.maketrans('','',string.punctuation))
    encontrados = [c for c in lista_clientes if c["cpf"] == cpf]
    if(encontrados == []):
        print("OPERAÇÃO CANCELADA!")
        print(f"Não há cadastro de cliente com CPF: {cpf}.")
    else:
        numero_conta = len(lista_contas) + 1
        lista_contas.append({"agencia": "0001", "conta": numero_conta, "cliente": cpf_cliente})
        print(f"Conta {numero_conta} cadastrada com sucesso para o cliente com CPF: {cpf_cliente}")

while True:

    opcao = input(menu)
    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        movimentacao(valor_deposito, deposito)


    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: "))
        movimentacao(valor_saque, saque)        

    elif opcao == "e":
        extrato_conta(saldo, extrato=extrato)

    elif opcao == "c":
        cpf = input("Digite seu CPF: ")
        cadastra_cliente(cpf=cpf, lista=lista_clientes) 

    elif opcao == "i":
        print("================= Clientes Cadastrados =================")
        for c in lista_clientes:
            print(c)
    
    elif opcao == "t":
        cpf = input("Digite o CPF do cliente que deseja cadastrar uma nova conta: ")
        criar_conta(cpf_cliente=cpf, lista_contas=lista_contas, lista_clientes=lista_clientes)
    
    elif opcao == "r":
        print("================= Contas Cadastradas =================")
        for c in lista_contas:
            print(c)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")