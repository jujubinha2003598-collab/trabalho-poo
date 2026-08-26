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
     locadora.adicionar_cliente(cliente)
    print("\nCliente cadastrado com sucesso!")
elif  opcao == "2":
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    portas = int(input("Quantidade de portas: "))
    potencia = int(input("Potência do motor: "))
    carro = Carro(placa, modelo, ano, portas, potencia)
    locadora.adicionar_veiculo(carro)
    print("\nCarro cadastrado com sucesso!")
 elif opcao == "3":
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    potencia = int(input("Potência do motor: "))
    cilindradas = int(input("Cilindradas: "))
    moto = Moto(placa, modelo, ano, potencia, cilindradas)
    locadora.adicionar_veiculo(moto)
    print("\nMoto cadastrada com sucesso!")
elif opcao == "4":
    print("\n====== VEÍCULOS ======")
    locadora.listar_veiculos()