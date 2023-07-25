opcoes = '''
###########################################

    Qual operação deseja realizar?

[d] Para Depositar | [s] Para Sacar
[e] Para ver o extrato | [q] Para Sair

   SISTEMA BANCÁRIO - 2023 - V1.0.1
###########################################
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(opcoes)
    
    if opcao == "d":
        valor = float(input("Quanto deseja depositar?:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Falha na operação! Valor inválido.")
        
    
    elif opcao == "s":
        valor = float(input("Quanto deseja sacar?:")) 
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Falha na operação! Saldo insuficiente.")  
              
        elif excedeu_limite:
            print("Limite atingido!")
            
        elif excedeu_saques:
            print("Limite de saques atingido!")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else: 
            print("Falha na operação! Valor inválido.")
            
    elif opcao == "e":
        print("\n############ SEU EXTRATO ###########")
        print("Não houveram movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("######################################")
    
    elif opcao == "q":
        print("Tenha um bom dia/boa tarde/boa noite!")
        break
    
    else:
        print("Operação inválida, selecione outra opção.")
        
        