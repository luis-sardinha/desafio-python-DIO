    # Desenvolver um sistema bancario com as seguintes funcoes: deposito, saque e extrato.

#DEPOSITO: 
# Não será aceito deposito de valores negativos, todos os depositos feitos deveram ser armazenados e exibidos no extrato
#SAQUE: Não sera possivel deixar a conta negativa,3 Saques diarios com limite de 500 por saque. Caso nao haja saldo, exibir mensagem. todos os saques deveram ser amazenados e exibidos na operaçao extrato.
#EXTRATO: Listar todos os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta formato (R$ xxx.xx ) 1500.45 = R$ 1500.45

saldo = 0
depositos_realizados = []
saques_realizados = []
numero_de_saques = 0
limite_saque = 500
LIMITE_SAQUE = 3



while True:

    def menu_principal():

        menu = """ 
            Digite a Opção desejada
        ---------------------------------
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        ---------------------------------
        """
        print(menu)
    menu_principal()
    opcao = input()

    if opcao == "d":
        deposito = float(input("Opcao depósito selecionada, quanto deseja depositar na conta?: "))
        if deposito < 0:
            print("O Valor do deposito nao pode ser menor que zero")
        
        saldo += deposito
        depositos_realizados.append(deposito)
        retornar_menu = input("Deposito realizado com sucesso!!, pressione qualquer tecla para voltar ao menu")
    
    elif opcao == "s":

        saque = float(input("Digite quanto deseja sacar: ?\n"))
        if saque > saldo:
            print("Saldo insuficiente")
        elif saque == 0 or saque < 0:
            print("Saque nao realizado, valor digitado foi 0 ou insuficiente")
        elif numero_de_saques >= LIMITE_SAQUE:
            print("Não foi possivel realizar a operação, limite de numero de saques atingido")
        elif saque > limite_saque:
            print(f"Não foi possivel sacar, valor maximo de saque é de: R$ {float(limite_saque)} por saque")
        else:
            saldo -= saque
            saques_realizados.append(saque)
            numero_de_saques += 1
            retornar_menu = input("Saque realizado com sucesso!! Pressione qualque tecla para voltar ao menu")

    elif opcao == "e":

        print("""
        ---------- Extrato ----------""")
        for deposito in depositos_realizados:
            print("Depositos realizados: ", "R$ " + (str(deposito)))
        for saque in saques_realizados:
            print("Saques realizados: ", "R$" + (str(saque)))
        print("O Saldo da conta é: R$", (float(saldo)))
        
        retornar_menu = input("\nTecle enter para retornar ao menu inicial")
            
    elif opcao == "q":

        print("Obrigado por utilizar nossos serviços!\n")
        break 

    else:
        print("Operação incorreta, digite a opcao desejada: ")       



