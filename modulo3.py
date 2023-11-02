class medicamentoN:
    def __init__(self, nome,quantidade, principio_ativo,dosagem,administracao,fabricante, lote, datadevalidade):
        self.nome = nome
        self.quantidade = quantidade
        self.principio_ativo = principio_ativo
        self.dosagem = dosagem
        self.administracao = administracao
        self.fabricante = fabricante
        self.lote = lote
        self.datadevalidade = datadevalidade

medicamento1 = medicamentoN("Dorflex", 20, "Dipirona", "500mg", "Oral", "EMS", "123456", "12/02/2023")

medicamentos = [
    medicamento1
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
    except ValueError:
        print("\nOpção inválida, tente novamente!\n")
        menuInicial()

def adicionarMedicamento():
    inFuncao = True
    visualizarEstoque(inFuncao)

    print("\n---- Cadastro de Medicamentos ----\n")

    nomeMedicamento = input("Nome do medicamento: ")
    #Verificando se o medicamento ja existe no estoque
    for medicamento in medicamentos:
        if nomeMedicamento == medicamento.nome:
            print("\nMedicamento já cadastrado!\n")
            userInput = input("Deseja atualizar a quantidade do medicamento? (S/N): ")
            if userInput == "S" or userInput == "s":
                quantidade = int(input("Digite a quantidade que deseja adicionar: "))
                medicamento.quantidade += quantidade
                print("\nQuantidade atualizada com sucesso!\n")
                menuInicial()
        else:
            quantidadeMedicamento = int(input("Quantidade: "))        
            principioAtivo = input("Principio ativo: ")
            dosagem = input("Dosagem: ")
            administracao = input("Administração: ")
            fabricante = input("Fabricante: ")
            lote = input("Lote: ")
            dataDeValidade = input("Data de validade: ")

            medicamentoNovo = medicamentoN(nomeMedicamento, quantidadeMedicamento, principioAtivo, dosagem, administracao, fabricante, lote, dataDeValidade)
            medicamentos.append(medicamentoNovo)
            print("\nMedicamento adicionado com sucesso!\n")
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
    pass
def rastrearLote():
    pass
def administrarMedicamento():
    pass
        
menuInicial()