class medicamento:
    def __init__(self, nome, principio_ativo,dosagem,administracao,fabricante, lote, datadevalidade):
        self.nome = nome
        self.principio_ativo = principio_ativo
        self.dosagem = dosagem
        self.administracao = administracao
        self.fabricante = fabricante
        self.lote = lote
        self.datadevalidade = datadevalidade

medicamento1 = medicamento("Dorflex", "Dipirona", "500mg", "Oral", "EMS", "123456", "12/02/2023")

medicamentos = [
    medicamento1
]

def menuInicial():
    try:
        print("\n---- Administração de Medicamentos ----\n\n1. Cadastro de Medicamentos\n2. Visualizar Estoque\n3. Remover Medicamento\n4. Rastreamento de Lotes\n5. Administrar Medicamento\n")
        escolhaMenu = int(input("\nDigite o numero da opcao desejada: "))

        match escolhaMenu:
            case 1:
                adicionarMedicamento()
            case 2:
                visualizarEstoque()
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
        print("\n---- Cadastro de Medicamentos ----\n")
        nomeMedicamento = input("Nome do medicamento: ")
        principioAtivo = input("Principio ativo: ")
        dosagem = input("Dosagem: ")
        administracao = input("Administração: ")
        fabricante = input("Fabricante: ")
        lote = input("Lote: ")
        dataDeValidade = input("Data de validade: ")

        medicamentoNovo = medicamento(nomeMedicamento, principioAtivo, dosagem, administracao, fabricante, lote, dataDeValidade)
        medicamentos.append(medicamentoNovo)
        print("\nMedicamento adicionado com sucesso!\n")
        menuInicial()

    def visualizarEstoque():
        inFuncao = True
        count = 1
        print("\n---- Estoque de Medicamentos ----")
        for medicamento in medicamentos:
            print(f"\nMedicamento {count}: {medicamento.nome}\nPrincipio ativo: {medicamento.principio_ativo}\nDosagem: {medicamento.dosagem}\nAdministração: {medicamento.administracao}\nFabricante: {medicamento.fabricante}\nLote: {medicamento.lote}\nData de validade: {medicamento.datadevalidade}\n")
            count += 1
        if inFuncao == False:
            input("\nPressione qualquer tecla para voltar ao menu inicial")    
            menuInicial()

    def removerMedicamento():
        pass
    def rastrearLote():
        pass
    def administrarMedicamento():
        pass
        
menuInicial()