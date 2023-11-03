class equipamentos:
    def __init__(self, nome, numero_serie, data_aquisicao, data, tipo_manutencao, intervencao):
        self.nome = nome
        self.numero_serie = numero_serie
        self.data_aquisicao = data_aquisicao
        self.data = data
        self.tipo_manutencao = tipo_manutencao
        self.intervencao = intervencao
        

#Equipamentos iniciais
equipamento1 = equipamentos("Respirador", "2art323", "20/08/2001", "23/12/2001", "Correção no funcionamento", "1")
equipamento2 = equipamentos("Monitor cardiaco", "tti342h", "10/01/2000", "22/09/2003", "Correção no monitor", "2")

def erro(varaivel):
    try:
        dia_aquisicao = int(input("Dia da aquisição"))
        mes_aquisicao = int(input("Mes da aquisição"))
        ano_aquisicao = int(input("Ano da aquisição"))
    except ValueError:
        print("Opção inválida!")



equipamentos_UTI = [
    equipamento1, equipamento2
]
manutencao_nome = []

manutecoes_agendadas = {}

manutencao_nome.append(equipamento1.nome)
manutencao_nome.append(equipamento2.nome)


def novo_equipamento():
    print("\nInforme os seguintes dados abaixo")
    nome_equipamento = input("Nome do equipamento: ")
    numero_serie = input("Número de série: ")

    try:
        dia_aquisicao = int(input("Dia da aquisição: "))
        mes_aquisicao = int(input("Mes da aquisição: "))
        ano_aquisicao = int(input("Ano da aquisição: "))
    except ValueError:
        print("Opção inválida!")
        novo_equipamento()
    if dia_aquisicao > 31 and mes_aquisicao >12:
            print("data inválida!")
            novo_equipamento()
    
    data = f"{dia_aquisicao}/{mes_aquisicao}/{ano_aquisicao}"

    Novo_equipamento = equipamentos(nome_equipamento, numero_serie, data, "Equipamento Novo", "","")
    equipamentos_UTI.append(Novo_equipamento)
    manutencao_nome.append(nome_equipamento.capitalize())

    Menu()

def agendar_manutencao():
    print("escolha um equipamento para agendar uma manutenção:\n")
    for nomes in manutencao_nome:
        print(nomes)
    escolha_manutecao = input("")
    if escolha_manutecao.capitalize() in manutencao_nome:
        try:
            escolha_dia = int(input("Escolha o dia: "))
            escolha_mes = int(input("Escolha o mês: "))
        except ValueError:
            print("data inválida!")
            agendar_manutencao()
        if escolha_dia > 31 and escolha_mes >12:
            print("data inválida!")
            agendar_manutencao()

    
        data_manutencao = f"{escolha_dia}/{escolha_mes}"
        manutecoes_agendadas[escolha_manutecao] = data_manutencao
        Menu()

    else:
        print("Escolha inválida")
        agendar_manutencao()


def equipamento_registrados():
    for equipamento in equipamentos_UTI:
        print(f"Nome: {equipamento.nome}\nNúmero de série: {equipamento.numero_serie}\nData de aquisição: {equipamento.data_aquisicao}\nData de manutenção: {equipamento.data}\nTipo de manutenção: {equipamento.tipo_manutencao}\nQuantidade de intervenções: {equipamento.intervencao}\n")
    Menu()

def manutencao_agendada():
    print("Manutenções agendadas\n")
    for equipamento, data in manutecoes_agendadas.items():
        print(f"{equipamento} possuí data marcada para a data: {data}")
    Menu()



def Menu():
    print("-------- Menu de registro do equipamentos -------- ")
    print("[1] Ver equipamentos registrados")
    print("[2] Adicionar novos equipamentos")
    print("[3] Agendar uma nova manutenção")
    print("[4] Ver manutenções anteriores")
    try:
        escolha_menu = int(input("Escolha um opção: \n"))
    except ValueError:
        print("opção inválida!")
        Menu()
    match escolha_menu:
        case 1:
            equipamento_registrados()
        case 2:
            novo_equipamento()
        case 3:
            agendar_manutencao()
        case 4:
            if manutecoes_agendadas == "":
                print("Nenhuma manutenção está agendada")
                Menu()
            manutencao_agendada()
        case _:
            print("opção inválida")
            Menu()




Menu()