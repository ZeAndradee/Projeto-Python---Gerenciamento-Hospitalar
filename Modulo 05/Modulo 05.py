class paciente:
    def __init__(self, nome, idade, sexo, historico, contato, gravidade, ingresso, horario, id_paciente, limiteVisitantes, condicao_diagnostico ):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.historico = historico
        self.contato = contato
        self.gravidade = gravidade
        self.ingresso = ingresso
        self.id_paciente = id_paciente
        self.limiteVisitantes = limiteVisitantes 
        self.condicao_diagnostico = condicao_diagnostico
        self.horario = horario
def cria_arquivo_txt(nome_arquivo, conteudo):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(conteudo)

def imprimir_dados_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        counteudo = arquivo.read()
        print(counteudo)
def adiciona_no_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, "a")as arquivo:
        arquivo.write(conteudo)

def cria_paciente():
    print("Informe os seguintes dados abaixo")
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        historico = input("Historico: ")
        contato = input("Contato de emergencia: ")
        gravidade = input("Gravidade do paciente: ")
        ingresso = input("Data de ingresso ao hospital: ")
        horario = input("Horario: ")
        id_paciente = input("Id do paciente: ")
        limiteVisitantes = input("Quantidade limite de visitantes: ")
        condicao_diagnostico = input("Condição do paciente: ")
        novo_paciente = paciente(nome, idade, sexo, historico, contato, gravidade,ingresso, horario, id_paciente, limiteVisitantes, condicao_diagnostico)
        pacientes.append(novo_paciente)
        nomes_pacientes[nome] = id_paciente
        dados_paciente = f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}\nHistorico: {historico}\nContato: {contato}\nData de ingresso: {ingresso}\nHorario: {horario}\nID: {id_paciente}\nLimite de visitantes: {limiteVisitantes}\nCondicao do paciente: {condicao_diagnostico} \n\n"
        nome = nome + id_paciente + ".txt"
        cria_arquivo_txt(nome, dados_paciente)
        Menu_diagnostico()
    except ValueError:
        print("Dado inválido, por favor tente novamente")
        cria_paciente()
        



paciente1 = paciente("Pedro", 20, "M", "Nenhum", "123456789", "Grave", "01/01/2021", "15:20", "1", 2, "Estavel")
paciente2 = paciente("Ana", 20, "F", "Nenhum", "123456789", "Grave", "01/01/2021", "13:00", "2", 0, "Isolamento")
paciente3 = paciente("Vinicius", 20, "M", "Nenhum", "123456789", "Grave", "01/01/2021", "12:30", "3", 3, "Estavel")
paciente4 = paciente("João", 20, "M", "Nenhum", "123456789", "Grave", "01/01/2021", "14:00", "4", 2, "Estavel")
paciente5 = paciente("Maria", 20, "F", "Nenhum", "123456789", "Grave", "01/01/2021", "09:00", "5", 0, "Isolamento")

pacientes = []
nomes_pacientes = {}

diagnosticos = []
#adiciona os nomes dos pacientes na lista

nomes_pacientes[paciente1.nome] = paciente1.id_paciente
nomes_pacientes[paciente2.nome] = paciente2.id_paciente
nomes_pacientes[paciente3.nome] = paciente3.id_paciente
nomes_pacientes[paciente4.nome] = paciente4.id_paciente
nomes_pacientes[paciente5.nome] = paciente5.id_paciente

#adiciona os dados dos pacientes na lista
pacientes.append(paciente1)
pacientes.append(paciente2)
pacientes.append(paciente3)
pacientes.append(paciente4)
pacientes.append(paciente5)
#parte do diagnostico serve para anotar informações de como o paciente está se sentindo

def Registro_diagnostico():
    print("Informe os dados abaixo para realizar o diagnostico do paciente")
    for nomes, id in nomes_pacientes.items():
        print(f"Nome: {nomes}\nID: {id}\n\n ")
    escolha_paciente = input("Digite o nome do paciente: ")
    if escolha_paciente in nomes_pacientes:
        try:  
            condicao_diagnostico = input("Informe o diagnostico do paciente: ")
            dia_diagnostico = int(input("Dia em que está sendo feito o diagnostico: "))
            mes_diagnostico = int(input("Mês do do diagnostico: "))
        except ValueError:
            print("data inválida!\n")
            Registro_diagnostico()
        if dia_diagnostico > 31 and mes_diagnostico > 12:
            Registro_diagnostico()
        data = f"{dia_diagnostico}/{mes_diagnostico}"
        tratamento_diagnostico = input("Tratamento recomendado: ")
        dados_diagnostico = (f"Condicao: {condicao_diagnostico}\nData: {data}\nTratamento recomendado: {tratamento_diagnostico}\n\n")
        escolha_paciente = escolha_paciente + nomes_pacientes[escolha_paciente] + ".txt"
        adiciona_no_arquivo(escolha_paciente, dados_diagnostico)
        Menu_diagnostico()
    else:
        print("Nome não encontrado, por favor tente novamente")
        Registro_diagnostico()
#parte do acompanhamento serve para determinar os medicamentos, procedimentos e terapias, ou seja está parte funciona como um complemento
#para o diagnostico

def acompanhamento():
    for nomes, id in nomes_pacientes.items():
        print(f"Nome: {nomes}\nID: {id}\n\n ")
    escolha_paciente = input("Digite o nome do paciente: ")
    if escolha_paciente.capitalize() in nomes_pacientes.keys():
        medicamento_diagnostico = input("Informe o medicamento que deve ser recomendado: ")
        try:
            quantidade_medicamento = int(input("QUantidade(mg): "))
        except ValueError:
            print("Quantidade inválida, tente novamente\n")
            acompanhamento()
        procedimento = input("Qual procedimento deverá ser aplicado no paciente: ")
        terapia = input("Qual metodo de terapia será aplicado ao paciente:")
        dados_acompanhamento = f"Medicamentos: {medicamento_diagnostico}\nQuantidade do medicamento: {quantidade_medicamento}\nProcedimento: {procedimento}\nTerapia:{terapia}\n \n"
        escolha_paciente = escolha_paciente.capitalize() +nomes_pacientes[escolha_paciente] + ".txt"
        adiciona_no_arquivo(escolha_paciente, dados_acompanhamento)
        Menu_diagnostico()
    else:
        print("Paciente não encontrado")
#serve para imprimir no terminal as informações dos diagnosticos(arquivos) dos pacientes

def ver_diagnosticos_registrados():
    for nomes, id in nomes_pacientes.items():
        print(f"Nome: {nomes}\nID: {id}\n\n ")
    escolha_paciente_registrados = input("Escolha um paciente para acessar seu diagnostico: ")
    if escolha_paciente_registrados.capitalize() in nomes_pacientes.keys():
            escolha_paciente_registrados = escolha_paciente_registrados +nomes_pacientes[escolha_paciente_registrados]+ ".txt"
            try: 
                imprimir_dados_arquivo(escolha_paciente_registrados)
            
            except FileNotFoundError:
                print("O paciente escolhido não possui diagnostico registrado!")
                Menu_diagnostico()
    else:
            print("Paciente não encontrado, por favor tente novamente\n")
            ver_diagnosticos_registrados()

def evolucao_clinica():
    print("Nessa etapa voce deve informar caso o paciente apresente alguma evolução em seus exames, mudança em sua saúde ou outra observação importante\n")
    for nomes, id in nomes_pacientes.items():
        print(f"Nome: {nomes}\nID: {id}\n ")
    escolha_paciente_evolucao = input("Escolha um paciente: ")
    if escolha_paciente_evolucao in nomes_pacientes.keys():
        evolucao_paciente = input("Informe quais evolucoes o paciente apresentou durante o periodo do tratamento: ")
        escolha_paciente_evolucao = escolha_paciente_evolucao + nomes_pacientes[escolha_paciente_evolucao] + ".txt"
        with open(escolha_paciente_evolucao, "a")as arquivo:
            arquivo.write(f"Atualizacao do caso do paciente:\n{evolucao_paciente}")
            Menu_diagnostico()
    else:
        print("Paciente não encontrado, tente novamente")
        evolucao_clinica()


def Menu_diagnostico():
    print("\n\nBem vindo ao menu do prontuario eletronico")
    print("[1] Cadastrar um paciente")
    print("[2] Registrar diagnostico")
    print("[3] Acompanhamento do diagnostico")
    print("[4] Exibir dados dos diagnosticos anteriores")
    print("[5] Anotar evolução no tratamento")
    print("[6] sair")



    escolha_menu_diagnostico = int(input("\nEscolha uma opção: "))
    
    match escolha_menu_diagnostico:

        case 1:
            cria_paciente()
        case 2:
            Registro_diagnostico()
        case 3:
            acompanhamento()
        case 4:
            ver_diagnosticos_registrados()
        case 5:
            evolucao_clinica()
        case 6:
            print("Menu encerrado")
            pass
        case _:
            print("Opção inválida")
            Menu_diagnostico()

Menu_diagnostico()

    







