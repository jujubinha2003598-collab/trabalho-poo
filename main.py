from locadora import Locadora
from cliente import Cliente
from carro import Carro 
from moto import Moto
from aluguel import Aluguel 

locadora = Locadora("Alphia Agency")
while True:

    print("\n====== ALPHIA AGENCY ======")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar carro")
    print("3 - Cadastrar moto")
    print("4 - Listar veículos")
    print("5 - Fazer aluguel")
    print("6 - Listar alugueis")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome completo: ")
        cpf = input("CPF:")
        cliente = Cliente(nome, cpf)
         locadora.adicionar_clientes(cliente)
        print("\nCliente cadastrado com sucesso!")
    
    elif  opcao == "2":
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        potencia = int(input("Potência do motor: "))
        portas = int(input("Quantidade de portas: "))
        carro = Carro(placa, modelo, ano, potencia, portas)
        locadora.adicionar_veiculos(carro)
        print("\nCarro cadastrado com sucesso!")
    
     elif opcao == "3":
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        potencia = int(input("Potência do motor: "))
        cilindradas = int(input("Cilindradas: "))
        moto = Moto(placa, modelo, ano, potencia, cilindradas)
        locadora.adicionar_veiculos(moto)
        print("\nMoto cadastrada com sucesso!")
    
    elif opcao == "4":
        print("\n====== VEÍCULOS ======")
        locadora.listar_veiculos()
    
    elif opcao == "5":
        print("\n====== FAZER ALUGUEL ======")
        cpf = input("CPF do cliente: ")
        cliente = locadora.buscar_cliente(cpf)
        if cliente is None:
            print("Cliente não encontrado!")
            continue
        placa = input("Placa do veículo: ")
        veiculo = locadora.buscar_veiculo(placa)
        if veiculo is None:
            print("Veículo não encontrado!")
            continue
        dias = int(input("Quantidade de dias: "))
        aluguel = Aluguel(cliente, veiculo, dias)
        locadora.adicionar_alugueis(aluguel)
        print("\nAluguel realizado com sucesso!")
        print(aluguel.mostrar_info())
    
    elif opcao == "6":
        print("\n====== ALUGUÉIS REALIZADOS ======")
        if len(locadora.alugueis) == 0:
            print("Nenhum aluguel realizado.")
        else:
            for aluguel in locadora.alugueis:
                print("\n" + aluguel.mostrar_info())
                print("----------------------------")
    elif opcao == "0":
        print("\nObrigado por utilizar a Alphia Agency!")
        print("Programa encerrado.")
        break
    else:
        print("\nOpção inválida! Tente novamente.")
