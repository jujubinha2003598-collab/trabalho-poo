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
    