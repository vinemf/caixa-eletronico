print("Bem vindo ao caixa eletrônico!")

senha_correta = "1234"
tentativas = 3

while tentativas > 0:
    senha = input("Digite sua senha de acesso: ")
    if senha == senha_correta:
        print("Acesso liberado!")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta! Tentativas restantes: {tentativas}")
else:
    print("Você excedeu o número de tentativas. Tente novamente mais tarde.")
    exit()


saldo = 0
extrato = []
limite = 5000

while True: 
   opcao = input("Escolha uma opção:\n 1 - Consultar saldo \n 2 - Depositar \n 3 - Sacar \n 4 - Ver extrato \n 5- Sair \n")
   
   if opcao == '1':
            consultar = print("Seu saldo atual é R$" + str(round(saldo, 2)))

   elif opcao == '2':
        while True:
             depositar = input("Digite o valor para depósito: ")
             try:
                     valor = float(depositar)
                     if valor>0:
                        saldo += valor
                        extrato.append(f"Depósito: R${round(valor, 2)}")
                        print("Depósito realizado com sucesso!")
                        break
                     elif valor<=0:
                        print("Depósito inválido! Você deve depositar um valor existente. Tente novamente.")
             except:
                    print("Depósito inválido! Digite apenas números.")
   
   elif opcao  == '3': 
          while True:
             sacar = input("Digite o valor para saque: ")
             try:
                     valor = float(sacar)
                     if valor>saldo:
                        print("Saque inválido! Seu saldo é de R$" + round(saldo, 2) + ". Tente novamente.")
                     elif valor<=0:
                          print("Saque inválido! Você deve sacar um valor existente. Tente novamente.")
                     elif valor>limite:
                          print("Saque inválido! O limite de saque é de R$ 5.000,00.")
                     else:
                        saldo -= valor
                        extrato.append(f"Saque: R${round(valor, 2)}")
                        print("Saque realizado com sucesso!")
                        break
                     
             except:
                    print("Saque inválido! Tente novamente.")

   elif opcao == '4':
           print("\n EXTRATO")
           if not extrato:
                print("Nenhuma operação realizada ainda.")
           else:
                for item in extrato:
                     print(item)
                print("Seu saldo atual é R$" + str(round(saldo, 2)))
          
   elif opcao == '5':
           print("Obrigado por usar o caixa eletrônico!")
           break
   
   else: print("Digite uma opção válida.")









