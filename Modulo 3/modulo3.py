from datetime import datetime
class Medicamento:
    def __init__(self, nome,quantidade, principio_ativo,dosagem,administracao,fabricante, lote, datadevalidade, qtdInicial):
        self.nome = nome
        self.quantidade = quantidade
        self.principio_ativo = principio_ativo
        self.dosagem = dosagem
        self.administracao = administracao
        self.fabricante = fabricante
        self.lote = lote
        self.datadevalidade = datadevalidade
        self.qtdInicial = qtdInicial

#Medicamentos Base
medicamento1 = Medicamento("Dorflex", 20, "Dipirona", "500mg", "Oral", "EMS", "K123", "31/01/2024", 20)
medicamento2 = Medicamento("Tylenol", 45, "Parecetamol", "750mg", "Oral", "Janseen", "K123", "31/12/2023", 45)

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
    medicamento_encontrado = False
    visualizarEstoque(inFuncao)

    print("\n---- Cadastro de Medicamentos ----\n")
    nomeMedicamento = input("Nome do medicamento: ")

    #Verificando se o medicamento ja existe no estoque
    for medicamento in medicamentos:
        if nomeMedicamento.lower() == medicamento.nome.lower():
            medicamento_encontrado = True
            print("\nMedicamento já cadastrado!\n")
            userInput = input("Deseja atualizar a quantidade do medicamento? (S/N): ")
            if userInput.lower() == "s":
                quantidade = int(input(f"Digite a quantidade que deseja adicionar (Qtd. Atual: {medicamento.quantidade}): "))
                medicamento.quantidade += quantidade
                print("\nQuantidade atualizada com sucesso!\n")
                menuInicial()
            else:
                print("\nALERTA!  Operação cancelada!\n")
                menuInicial()
    if not medicamento_encontrado:
        quantidadeMedicamento = int(input("Quantidade: "))        
        principioAtivo = input("Principio ativo: ")
        dosagem = input("Dosagem: ")
        administracao = input("Administração: ")
        fabricante = input("Fabricante: ")
        lote = input("Lote: ")
        dataDeValidade = input("Data de validade: ")

        medicamentoNovo = Medicamento(nomeMedicamento, quantidadeMedicamento, principioAtivo, dosagem, administracao, fabricante, lote, dataDeValidade)
        medicamentos.append(medicamentoNovo)
        #Adionando aos registros de log
        with open("logAlertas.txt", 'a') as arquivo:
            arquivo.write(f"| NOVO MEDICAMENTO | Medicamento: {medicamentoNovo.nome} - Quantidade: {medicamento.quantidade}\n")
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
    try:
        infuncao = True
        visualizarEstoque(infuncao)

        print("\n---- Remover Medicamento ----\n")
        userInput = input("\nDigite o nome do medicamento que deseja remover: ")
        medicamento_encontrado = False

        for medicamento in medicamentos:
            if userInput.lower() == medicamento.nome.lower():
                medicamento_encontrado = True
                print(f"\nMedicamento {medicamento.nome} encontrado!\n")
                userInput2 = int(input(f"Qual a quantidade deseja remover do medicamento? (Qtd. Atual: {medicamento.quantidade}): "))
                if userInput2 >= medicamento.quantidade:
                    medicamento.quantidade -= medicamento.quantidade
                    print("\nQuantidade maxima retirada!\n")
                    with open("logAlertas.txt", 'a') as arquivo:
                        arquivo.write(f"| MEDICAMENTO RETIRADO | Medicamento: {medicamento.nome} - Quantidade Retirada: {userInput2}\n")
                    menuInicial()     
                else:
                    medicamento.quantidade -= userInput2
                    print(f"A quantidade foi atualizada com sucesso! (Qtd. Atual: {medicamento.quantidade})")
                    with open("logAlertas.txt", 'a') as arquivo:
                        arquivo.write(f"| MEDICAMENTO RETIRADO | Medicamento: {medicamento.nome} - Quantidade Retirada: {userInput2}\n")
                    menuInicial()
        if not medicamento_encontrado:
            print("\nMedicamento não encontrado!\n")
            menuInicial()
    except:
        print("\nOpção inválida, tente novamente!\n")
        removerMedicamento()  


def rastrearLote():
    
    inFuncao = True
    visualizarEstoque(inFuncao)
    medicamento_encontrado = False

    print("\n---- Rastreamento de Lotes ----\n")
    userInput = input("Digite o nome ou lote do medicamento que deseja rastrear: ")
    for medicamento in medicamentos:
        if userInput.lower() == medicamento.nome.lower() or userInput.lower() == medicamento.lote.lower():
            medicamento_encontrado = True
            print(f"\nMedicamento {medicamento.nome} encontrado!\n")
            print(f"Lote: {medicamento.lote}\nData de validade: {medicamento.datadevalidade}\n")

            with open("logAlertas.txt", 'a') as arquivo:
                arquivo.write(f"| Rastreio Lote | Medicamento: {medicamento.nome} - Lote: {medicamento.lote}\n")
    if not medicamento_encontrado:
        print("\nMedicamento ou lote não encontrado!\n")
        menuInicial() 
    menuInicial()


def administrarMedicamento():
    inFuncao = True
    visualizarEstoque(inFuncao)
    print("\n---- Administrar Medicamento ----\n")
    medicamento_encontrado = False
    userInput = input("\nDigite o nome do medicamento que deseja administrar: ")
    for medicamento in medicamentos:
        if userInput.lower() == medicamento.nome.lower():
            medicamento_encontrado = True
            print(f"\nMedicamento {medicamento.nome} encontrado!\n")
            qtdAdm = int(input(f"Qual a quantidade deseja administrar do medicamento? (Qtd. Atual: {medicamento.quantidade}): "))
            dose = float(input("Digite a dosagem administrada (mg): "))
            paciente = "None"
            respAdm = "None"
            if qtdAdm > medicamento.quantidade or qtdAdm <= 0:
                print("\nAlerta!  Quantidade superior ao disponível em estoque, tente novamente!")
                with open("logAlertas.txt", 'a') as arquivo:
                    arquivo.write(f"| QTD SUPERIOR | Medicamento: {medicamento.nome} - Quantidade Requisitada {qtdAdm} - Quantidade Disponivel: {medicamento.quantidade}\n")
                menuInicial()
            else:
                medicamento.quantidade -= qtdAdm
                now = datetime.now()
                horaAtual = now.strftime("%d/%m/%Y %H:%M:%S")

                with open("logAdministracao.txt", 'a') as arquivo:
                    arquivo.write(f"| ADIMINISTRACAO | Medicamento: {medicamento.nome} - Quantidade: {qtdAdm} - Dose Administrada: {dose}mg  - Dose Recomendada: {medicamento.dosagem}- Paciente: {paciente} - Responsavel Administracao: {respAdm} | ( {horaAtual} )\n")
                
                print(f"O medicamento foi administrado com sucesso!")
                alertaEstoque = medicamento.qtdInicial * 0.2
                if medicamento.quantidade <= alertaEstoque:
                    print("\nAlerta!  O estoque do medicamento está baixo!\n")
                    with open("logAlertas.txt", 'a') as arquivo:
                        arquivo.write(f"| ESTOQUE BAIXO | Medicamento: {medicamento.nome} - Quantidade: {medicamento.quantidade} - Quantidade Inicial: {medicamento.qtdInicial}\n")
            break
    if not medicamento_encontrado:
        print("\nMedicamento não encontrado!\n")
        menuInicial()    

with open("logAlertas.txt", 'a') as arquivo:
    arquivo.write("\n\n------ Log de Alertas -----\n")

with open("logAdministracao.txt", 'a') as arquivo:
    arquivo.write("\n\n------ Log de Administracao de Medicamentos -----\n")
menuInicial()
    