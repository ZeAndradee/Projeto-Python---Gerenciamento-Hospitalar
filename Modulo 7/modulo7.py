from datetime import datetime

class Visitantes:
    def __init__(self, id, nome,rg,relacaoPaciente,dataAutorizacao, paciente, visitou):
        self.id = id
        self.nome = nome
        self.rg = rg
        self.relacaoPaciente = relacaoPaciente
        self.dataAutorizacao = dataAutorizacao
        self.paciente = paciente
        self.visitou = visitou

class Pacientes:
    def __init__(self, id, nome, limiteVisitantes, condicao):
        self.id = id
        self.nome = nome
        self.limiteVisitantes = limiteVisitantes
        self.condicao = condicao


#Visitantes Base
visitante1 = Visitantes("1","João", "123456789", "Pai", "01/01/2021", "1", False)
visitante2 = Visitantes("2","Maria", "987654321", "Mãe", "01/01/2021", "3", False)
visitante3 = Visitantes("3","José", "123456789", "Tio", "01/01/2021", "3", False)

visitantes = [
    visitante1,
    visitante2,
    visitante3
]

#Pacientes Base
paciente1 = Pacientes("1", "Pedro", 2, "Estavel")
paciente2 = Pacientes("2", "Ana", 0, "Isolamento")
paciente3 = Pacientes("3", "Vinicius", 3, "Estavel")

pacientes = [
    paciente1,
    paciente2,
    paciente3
]

#TODO Registro de entrada e saida de visitantes
#TODO Notificação de visitas pendentes
#TODO Verificar se a data de autorização não está expirada

def menuInicial(): 
     
    print("\n---- Gerenciamento de Visitantes ----\n\n1. Cadastro de Visitantes\n2. Autorizar Visitante\n3. Lista Visitantes\n4. Lista Pacientes\n5. Sair\n")
    escolhaMenu = int(input("\nDigite o numero da opcao desejada: "))

    match escolhaMenu:
        case 1:
            cadastrarVisitante()
        case 2:
            autorizarVisitante()
        case 3:
            inFuncao = False
            listaVisitantes(inFuncao)
        case 4:
            inFuncao = False
            listaPacientes(inFuncao)
        case 5:
            print("Saindo...")
            
        case _:
            print("\nOpção inválida, tente novamente!\n")
            menuInicial()          
    


def cadastrarVisitante():
    print("\n---- Cadastro de Visitantes ----\n")
    idVisitante = input("Id do visitante: ")
    for visitante in visitantes:
        if idVisitante.lower() == visitante.id.lower():
            print("\nId já cadastrado, tente novamente!\n")
            cadastrarVisitante()

    nomeVisitante = input("Nome do visitante: ")
    rgVisitante = input("RG do visitante: ")
    for visitante in visitantes:
        if rgVisitante.lower() == visitante.rg.lower():
            print("\nRG já cadastrado, tente novamente!\n")
            cadastrarVisitante()
    listaPacientes(inFuncao = True)
    escolhaPaciente = input("Id do paciente: ")
    pacienteEncontrado = False
    for paciente in pacientes:
        if escolhaPaciente.lower() == paciente.id.lower():
            pacienteEncontrado = True
            if paciente.limiteVisitantes > 0:
                relacaoPaciente = input("Relação com o paciente: ")
                dataAutorizacao = input("Data de autorização: ")
                visitante = Visitantes(idVisitante, nomeVisitante, rgVisitante, relacaoPaciente, dataAutorizacao,escolhaPaciente, False)
                visitantes.append(visitante)
                print("\nVisitante cadastrado com sucesso!\n")
                menuInicial()
            else:
                print("\nPaciente não pode receber visitas! \n")
                menuInicial()
    if not pacienteEncontrado:
        print("\nPaciente não encontrado, tente novamente!\n")
        menuInicial()    

def autorizarVisitante():
    print("\n---- Autorizar Visitante ----\n")
    listaVisitantes(inFuncao = True)

    idVisitante = input("Id do visitante: ")
    visitanteEncontrado = False
    for visitante in visitantes:
        if idVisitante.lower() == visitante.id.lower():
            visitanteEncontrado = True
            idPacienteEscolhido = visitante.paciente
            for paciente in pacientes:
                if idPacienteEscolhido.lower() == paciente.id.lower():
                    if paciente.limiteVisitantes > 0:
                        paciente.limiteVisitantes -= 1
                        visitanteEncontrado = True
                        print("\nVisitante autorizado com sucesso!\n")

                        now = datetime.now()
                        horaAtual = now.strftime("%d/%m/%Y")
                        with open("entradaSaida.txt", "a") as arquivo:
                            arquivo.write(f"| ENTRADA VISITANTE | - Visitante {visitante.nome} autorizado(a) no dia {horaAtual} para visitar o paciente {paciente.nome}\n")
                        visitante.visitou = True
                        for visitante in visitantes:
                            if visitante.visitou == True:
                                visitantes.remove(visitante)

                        menuInicial()
                    else:
                        print("\nPaciente não pode receber visitas! \n")
                        menuInicial()
    if not visitanteEncontrado:
        print("\nVisitante não encontrado, tente novamente!\n")
        menuInicial()        


def listaVisitantes(inFuncao):
    #TODO Exibir o nome e n o id do paciente
    count = 0
    print("\n---- Lista de Visitantes ----\n")
    for visitante in visitantes:
        count += 1
        print(f"Visitante {count} - \nId: {visitante.id}\nNome: {visitante.nome}\nRG: {visitante.rg}\nRelação com o paciente: {visitante.relacaoPaciente}\nData de autorização: {visitante.dataAutorizacao}\nPaciente Relacionado (id): {visitante.paciente}\n")
    if inFuncao == False:
        input("\nPressione qualquer tecla para voltar ao menu inicial ")
        menuInicial()


def listaPacientes(inFuncao):
    count = 0
    print("\n---- Lista de Pacientes ----\n")
    for paciente in pacientes:
        count += 1
        print(f"Paciente {count} - \nId: {paciente.id} \nNome: {paciente.nome}\nCondição: {paciente.condicao}\nLimite de visitantes: {paciente.limiteVisitantes}\n")
    if inFuncao == False:
        input("\nPressione qualquer tecla para voltar ao menu inicial ")
        menuInicial()


with open("entradaSaida.txt", "a") as arquivo:
    arquivo.write("---- Log Entrada e Saida de Visitantes ----\n")

with open("visitasPendentes.txt", "a") as arquivo:
    arquivo.write("---- Log Visitas Pendentes ----\n")            
menuInicial()        