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

def cria_paciente():
    print("Informe os seguintes dados abaixo")
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        historico = input("Historico: ")
        contato = input("Contato: ")
        gravidade = input("Gravidade do paciente: ")
        ingresso = input("Data de ingresso ao hospital")
        horario = input("Horario: ")
        id_paciente = int(input("Id do paciente: "))
        limiteVisitantes = input("Quantidade limite de visitantes: ")
        condicao_diagnostico = input("Condição: ")
        novo_paciente = paciente(nome, idade, sexo, historico, contato, gravidade,ingresso, horario, id_paciente, limiteVisitantes, condicao_diagnostico)
        pacientes.append(novo_paciente)
        nomes_pacientes[nome] = id_paciente
    except ValueError:
        print("Dado inválido, por favor tente novamente")
        cria_paciente()
        Menu_diagnostico()



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

#adiciona os dados dos pacientes na lista
pacientes.append(paciente1)
pacientes.append(paciente2)
pacientes.append(paciente3)
pacientes.append(paciente4)
pacientes.append(paciente5)

def Registro_diagnostico():
    print("Informe os dados abaixo para realizar o diagnostico do paciente")
    for nomes, id in nomes_pacientes.items():
        print(f"Nome: {nomes}\nID: {id}\n\n ")
    escolha_paciente = input("Digite o nome do paciente: ")
    if escolha_paciente in nomes_pacientes:
        try:  
            condicao_diagnostico = input("Condições do paciente: ")
            dia_diagnostico = int(input("Dia em que está sendo feito o diagnostico: "))
            mes_diagnostico = int(input("Mês do do diagnostico: "))
        except ValueError:
            print("data inválida!\n")
            Registro_diagnostico()
        if dia_diagnostico > 31 and mes_diagnostico > 12:
            Registro_diagnostico()
        data = f"{dia_diagnostico}/{mes_diagnostico}"
        tratamento_diagnostico = input("Tratamento recomendado: ")
        diagnosticos.append(f"Nome do paciente: {escolha_paciente}\nCondição: {condicao_diagnostico}\nData: {data}\nTratamento recomendado: {tratamento_diagnostico}\n\n")

        Menu_diagnostico()
    else:
        print("Nome não encontrado, por favor tente novamente")
        Registro_diagnostico()

def acompanhamento():
    for nomes, id in nomes_pacientes.items():
        print(f"Nome: {nomes}\nID: {id}\n\n ")
    escolha_paciente = input("Digite o nome do paciente: ")
    if escolha_paciente in nomes_pacientes:
        medicamento_diagnostico = input("Informe o medicamento que deve ser recomendado: ")
        try:
            quantidade_medicamento = int(input("QUantidade(mg): "))
        except ValueError:
            print("Quantidade inválida, tente novamente\n")
        procedimento = input("Qual procedimento o paciente deverá seguir?: ")
        

def Menu_diagnostico():
    escolha_menu_diagnostico = int(input("\n\nEscolha uma opção abaixo: "))
    match escolha_menu_diagnostico:

        case 1:
            cria_paciente()
        case 2:
            Registro_diagnostico()

Menu_diagnostico()

    







