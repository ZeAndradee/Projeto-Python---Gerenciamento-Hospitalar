class Medicamento:
    def __init__(self, nome,quantidade, principio_ativo,dosagem,administracao,fabricante, lote, datadevalidade):
        self.nome = nome
        self.quantidade = quantidade
        self.principio_ativo = principio_ativo
        self.dosagem = dosagem
        self.administracao = administracao
        self.fabricante = fabricante
        self.lote = lote
        self.datadevalidade = datadevalidade

#Medicamentos Base
medicamento1 = Medicamento("Dorflex", 20, "Dipirona", "500mg", "Oral", "EMS", "N012", "31/01/2024")
medicamento2 = Medicamento("Tylenol", 45, "Parecetamol", "750mg", "Oral", "Janseen", "K123", "31/12/2023")

medicamentos = [
    medicamento1,
    medicamento2
]

def menuInicial():
    try:
        print("\n---- Gerenciamento de Medicamentos ----\n\n1. Cadastro de Medicamentos\n2. Visualizar Estoque\n3. Remover Medicamento\n4. Rastreamento de Lotes\n5. Administrar Medicamento\n")
        escolhaMenu = int(input("\nDigite o numero da opcao desejada: "))

        match escolhaMenu:
            case 1:
                adicionarMedicamento()
            case 2:
                inFuncao = False
                visualizarEstoque(inFuncao)
            case 3:
                removerMedicamento()
            case 4:
                rastrearLote()
            case 5:
                administrarMedicamento()
            case _:
                print("\nOpção inválida, tente novamente!\n")
                menuInicial()  
    
        menuInicial()
    except:
        print("\nOpção inválida, tente novamente!\n")
        menuInicial()
def adicionarMedicamento():
    inFuncao = True
    count = -1
    visualizarEstoque(inFuncao)

    print("\n---- Cadastro de Medicamentos ----\n")

    nomeMedicamento = input("Nome do medicamento: ")
    #Verificando se o medicamento ja existe no estoque
    for medicamento in medicamentos:
        count += 1
        if count == len(medicamentos):
            quantidadeMedicamento = int(input("Quantidade: "))        
            principioAtivo = input("Principio ativo: ")
            dosagem = input("Dosagem: ")
            administracao = input("Administração: ")
            fabricante = input("Fabricante: ")
            lote = input("Lote: ")
            dataDeValidade = input("Data de validade: ")

            medicamentoNovo = Medicamento(nomeMedicamento, quantidadeMedicamento, principioAtivo, dosagem, administracao, fabricante, lote, dataDeValidade)
            medicamentos.append(medicamentoNovo)
            print("\nMedicamento adicionado com sucesso!\n")
            menuInicial()
        else:
            if nomeMedicamento.lower() == medicamento.nome.lower():
                print("\nMedicamento já cadastrado!\n")
                userInput = input("Deseja atualizar a quantidade do medicamento? (S/N): ")
                if userInput.lower() == "s":
                    quantidade = int(input(f"Digite a quantidade que deseja adicionar (QTD Atual: {medicamento.quantidade}): "))
                    medicamento.quantidade += quantidade
                    print("\nQuantidade atualizada com sucesso!\n")
                    menuInicial()
                else:
                    print("\nALERTA!  Operação cancelada!\n")
                    menuInicial()
            

def visualizarEstoque(inFuncao):
    count = 1
    print("\n---- Estoque de Medicamentos ----")
    for medicamento in medicamentos:
        print(f"\nMedicamento {count}:\n\nNome Comercial: {medicamento.nome}\nQuantidade: {medicamento.quantidade}\nPrincipio ativo: {medicamento.principio_ativo}\nDosagem: {medicamento.dosagem}\nAdministração: {medicamento.administracao}\nFabricante: {medicamento.fabricante}\nLote: {medicamento.lote}\nData de validade: {medicamento.datadevalidade}\n")
        count += 1
    if inFuncao == False:
        input("\nPressione qualquer tecla para voltar ao menu inicial ")    
        menuInicial()

def removerMedicamento():
    infuncao = True
    count = -1
    visualizarEstoque(infuncao)

    print("\n---- Remover Medicamento ----\n")
    userInput = input("\nDigite o nome do medicamento que deseja remover: ")

    for medicamento in medicamentos:
        count += 1
        if count == len(medicamentos):
            print("\nMedicamento não encontrado!\n")
            menuInicial()
        elif userInput.lower() == medicamento.nome.lower():
            print(f"\nMedicamento {medicamento.nome} encontrado!\n")
            userInput2 = int(input(f"Qual a quantidade deseja remover do medicamento? (QTD Atual: {medicamento.quantidade}): "))
            if userInput2 >= medicamento.quantidade:
                medicamentos.remove(medicamento)
                print("O medicamento foi excluido do estoque!")
                menuInicial()
            else:
                medicamento.quantidade -= userInput2
                print(f"A quantidade foi atualizada com sucesso! (QTD Atual: {medicamento.quantidade})")
                menuInicial() 
        else:
            print("Valor inválido, tente novamente!")
            removerMedicamento()              
def rastrearLote():
    pass
def administrarMedicamento():
    pass

menuInicial()
    
