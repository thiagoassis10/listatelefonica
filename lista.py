import time, os
lista = {
    19874563: "Fulano",
    21234569: "Ciclano",
    31234565: "Beutrano",
    46547893: "João"
}


def Menu():
    WaitClear(1)
    opcao = 0
    while opcao != 4:
        opcao = int(input(''' 1 - Listar Números 
 2 - Adicionar Número 
 3 - Remover Número 
 4 - Sair
 Escolha uma Opção :'''))

        if opcao == 1:
            ListAll()
        elif opcao == 2:
            AddNumber()
        elif opcao == 3:
            RemoveNumber()
        elif opcao == 4:
            Exit()
        else:
            print("PENNNN!!! opção invalida")

    WaitClear(3)

def ListAll():
    i = 0
    for p, v in lista.items():
        print(str(i) + " - " + str(v) + " -> " + str(p))
        i += 1

def AddNumber():
    nam = input("Digite o Nome:")
    num = int(input("Digite o Número:"))

    lista.update({num: nam})
    ListAll()

def RemoveNumber():
    ListAll()
    r = int(input("Digite o número paraa ser removido :"))
    lista.pop(r)
    print("Removido com sucesso!!")

def Exit():
    print("Saindo do programa")


def WaitClear(tempo):
    time.sleep(tempo)
    os.system("cls")


Menu()