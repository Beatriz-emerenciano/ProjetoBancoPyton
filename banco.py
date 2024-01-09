from datetime import datetime
data_hora = datetime.now()
salvar = data_hora.strftime("%d/%m/%Y %H:%M:%S")
dataPassada = salvar


#função salvar arquivo

def salvarCadastro():
    with open("cadastros.txt","w") as file:
        for cliente in listagemClientes:
            for cpf, dados in cliente.items():
                file.write(f"CPF: {cpf}, ")
                file.write(f"Nome: {dados[0]},")
                file.write(f"Tipo de conta: {dados[1]},")
                file.write(f"saldo: {dados[2]},")
                file.write(f"senha: {dados[3]},")
               

    print("Cadastrado com sucesso")

listaExtrato = [] 
def salvarExtratos():
    with open("extratos.txt", "w") as file:
        for extrato in listaExtrato:
            for cpf, dados in extrato.items():
                file.write(f"CPF: {cpf}, ")
                file.write(", ".join(str(d) for d in dados))
                file.write("\n")  # Add a newline after each extrato
    print("Extratos salvos com sucesso!")

# função cadastrar um novo cliente, a chave do dicionario é o cpf do cliente e os #valores dessa chave é uma lista com o restante dos dados d cliente, esse #dicionário ficará guardado em uma clista geral de clientes
listagemClientes = []
def cadastrarCliente():
    cliente = {}
     
    # essa variável é a chave do dicionário cliente
    cpf = input("Digite seu cpf:")
    
        
          
    nome = input("Digite seu  nome: ")
    conta = input("Digite o tipo de conta: ")
    valor = float(input("digite valor: "))
    senha = input("Digite a senha: ")

    
    cliente = {cpf:[nome,conta,valor,senha]}
    listagemClientes.append(cliente)
       
               

    
    salvarCadastro()
    print(cliente,"  Cliente cadastrado com sucesso!")

def listarCliente():

    for cliente in listagemClientes:
        print(cliente)

def excluirCliente():

     resp = input("Desejar deletar cliente? s/n ")
     if resp.lower() == "s":
        validar = input("Digite o cpf:")
      

        for cliente in listagemClientes:
            if  validar in cliente:
                listagemClientes.remove(cliente)
                print("Cliente removido com Sucesso")
                break
            
        print("Cliente não encontrado!")

def debito():
    
    cpf = input("Digite o cpf:")
    senha = input("Digite a senha: ")
    
    cliente = {}
    for cliente in  listagemClientes:
        if cpf   in cliente and senha == cliente[cpf][3]:
         
            cliente[cpf][2] = float(cliente[cpf][2])
            total = 0
            debitar = float(input("Debite um valor:"))
            
            
            if cliente[cpf][1].lower() == "corrente" and cliente[cpf][2] >= (-1000):
                cliente[cpf][2] -= debitar
                tarifa = 0.05
                desc = cliente[cpf][2] *tarifa 
                total = cliente[cpf][2] - desc
                
                
                print("Débito realizado com sucesso!" )
                print(dataPassada,"cliente : ",cliente[cpf][0],"cpf: ",cpf,"conta: ",cliente[cpf][1], " saldo: %.2f" % total, " - débito")
            
                

               
                
                extrato = {cpf:[dataPassada,"cliente : ",cliente[cpf][0],"cpf: ",cpf,"conta: ",cliente[cpf][1],"saldo: ",total," - debito ",debitar,"tarifa:",tarifa,"- débito"]}

                listaExtrato.append(extrato)

               # break
            elif cliente[cpf][1].lower() == "plus" and cliente[cpf][2] >= (-5000):
                   tarifa = 0.03
                   cliente[cpf][2] -= debitar
                   desc = cliente[cpf][2] *tarifa
                   total = cliente[cpf][2] - desc
                   cliente[cpf][2] = "{:.2f}".format(total)
                   print("Deposito realizado com sucesso!" )
        
                   print(dataPassada,"cliente: ",cliente[cpf][0]," - débito ",deposito," débito")

                   extrato = {cpf:[dataPassada,"cliente : ",cliente[cpf][0],"cpf: ",cpf,"conta: ",cliente[cpf][1],"saldo: ",total," - débito ","tarifa:",tarifa ,"",debitar,"- débito"]}
                   listaExtrato.append(extrato)
            else:
                print("saldo insuficiente")

def deposito():
    
    cpf = input("Digite o cpf:")
    senha = input("Digite a senha: ")
    
    cliente = {}
    for cliente in  listagemClientes:
        if cpf   in cliente and senha == cliente[cpf][3]:
         
            cliente[cpf][2] = float(cliente[cpf][2])
            depositar = float(input("Deposite um valor:"))
            cliente[cpf][2] += depositar
            total = cliente[cpf][2]
            print("Debito realizado com sucesso!" )
            print(dataPassada,"cliente: ",cliente[cpf][0], "cpf: ",cpf, "conta: ",cliente[cpf][1],"saldo %.2f"% total," + depósito:","-",depositar,"Depósito")

            extrato = {cpf:[dataPassada,"cliente:",cliente[cpf][0],"cpf:",cpf,"conta:",cliente[cpf][1]," - depósito -", depositar," depósito"]}
            listaExtrato.append(extrato)


            
        else:
            print("")   



def transferencia():
    cpf = input("Digite o cpf origem:")
    #senha = input("Digite a senha: ")
    
    cliente = {}
    for cliente in  listagemClientes:
        if cpf   in cliente:
         
            cliente[cpf][2] = float(cliente[cpf][2])
            debitar = float(input("transfira um valor:"))
            cliente[cpf][2] -= debitar
            total = cliente[cpf][2]

    cpf2 = input("Digite o cpf destino:")
    #senha = input("Digite a senha: ")
    
    
    for cliente in  listagemClientes:
        if cpf2   in cliente:
        
            cliente[cpf2][2] += debitar 


        
    print(listagemClientes)  
    print("saldo: ",total)

    print(dataPassada,"cliente/cpf:",cpf,"transferido para ",cpf2,"saldo: ",total,"transferencia")       

    
    extrato = {cpf:[dataPassada,"cliente/cpf:",cpf,"conta:""transferência de + ",debitar,"Transferencia"]}              
    
    listaExtrato.append(extrato)

      
               
  
def extrato():
    cpf = input("Digite o cpf:")
    senha = input("Digite a senha: ")
    

    for cliente in  listagemClientes:
    
        if cpf   in cliente  and senha == cliente[cpf][3]:

            for extrato in listaExtrato:
                if cpf in extrato:
                    print("Extrato: " , extrato[cpf])


         


        else:    print("")
        
         

listagemPoupanca = []
def poupanca():
    cpf = input("Digite o cpf:")
    senha = input("Digite a senha: ")
    

    for cliente in  listagemClientes:
    
        if cpf   in cliente  and senha == cliente[cpf][3]:
            poupar = float(input("Digite o valor que queira poupar: "))
            
            cliente[cpf][2] = float(cliente[cpf][2])
             # poupar  é uma porcentagem que se o cliente poupar o dinehiro dele vai render na poupança
            cliente[cpf][2] -= poupar
            total = poupar+0.09

            print("Valor transferido para a poupança")

            poupaCliente = {cpf:[total]}

            listagemPoupanca.append(poupaCliente)
            print(listagemPoupanca)










   
         

    

               
               
           


                       



# menu principal
def menu():
    while True:
        print("bem-vindo ao Banco QuemPoupaTem ! ")
        print("Escolha uma operação bancária : ")
        print("1 - Cadastrar Cliente")
        print("2 - excluir cliente")  
        print("3 - listar cliente") 
        print("4 -  Débito")
        print("5 - Depósito")
        print("6 - Transferência")
        print("7 - Extrato")
        print("8 Poupança")
        print("9 - Sair do Sistema")

        opcao = int(input("Opção: "))

        if  opcao == 1:
            cadastrarCliente()
        elif opcao == 2:
            excluirCliente()
        elif opcao == 3:
            listarCliente()
        elif opcao == 4 :
            debito() 
        elif opcao == 5:
            deposito()  
        elif opcao == 6:
            transferencia()
        elif opcao == 7:
            extrato()   
        elif opcao == 8:
            poupanca()     


        

        elif opcao == 9:
         print("Obrigada por usar o sistema QuemPoupaTem!")
         break    
        else:
            print("erro!")

menu()

    
  

