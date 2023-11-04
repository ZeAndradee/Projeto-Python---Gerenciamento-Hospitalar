class equipamentos:
    def __init__(
        self, nome, numero_serie, data_aquisicao, data, tipo_manutencao, intervencao
    ):
        self.nome = nome
        self.numero_serie = numero_serie
        self.data_aquisicao = data_aquisicao
        self.data = data
        self.tipo_manutencao = tipo_manutencao
        self.intervencao = intervencao


# Equipamentos iniciais
equipamento1 = equipamentos(
    "Respirador",
    "2art323",
    "20/08/2001",
    "23/12/2001",
    "Correção no funcionamento",
    "1",
)
equipamento2 = equipamentos(
    "Monitor cardiaco",
    "tti342h",
    "10/01/2000",
    "22/09/2003",
    "Correção no monitor",
    "2",
)
equipamento3 = equipamentos(
    "Esfigmomanômetro",
    "781asnf",
    "12/04/2015",
    "Sem manutenção",
    "",
    ""
)
equipamento4 = equipamentos(
                "Desfribrilador",
                "abnc123",
                "19/07/2005",
                "23/12/2010",
                "Correção no funcionamento",
                "3"
)


equipamentos_UTI = [equipamento1, equipamento2, equipamento3, equipamento4]
manutencao_nome = []
auxiliar = []

manutecoes_agendadas = {}

manutencao_nome.append(equipamento1.nome)
manutencao_nome.append(equipamento2.nome)
manutencao_nome.append(equipamento3.nome)
manutencao_nome.append(equipamento4.nome)

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
    if dia_aquisicao > 31 and mes_aquisicao > 12:
        print("data inválida!")
        novo_equipamento()

    data = f"{dia_aquisicao}/{mes_aquisicao}/{ano_aquisicao}"

    Novo_equipamento = equipamentos(nome_equipamento, numero_serie, data, "Equipamento Novo", "", "")
    equipamentos_UTI.append(Novo_equipamento)
    auxiliar.append(Novo_equipamento)
    manutencao_nome.append(nome_equipamento.capitalize())
    with open("novoequipamento.txt", "a") as arquivo:
        for equipamento in auxiliar:
            arquivo.write((f"\n\nNome: {equipamento.nome}\nNumero de serie: {equipamento.numero_serie}\nData de aquisicao: {equipamento.data_aquisicao}\nData de manutencao: {equipamento.data}\nTipo de manutencao: {equipamento.tipo_manutencao}\nQuantidade de intervencoes: {equipamento.intervencao}\n"))
    auxiliar.remove(Novo_equipamento)
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
        if escolha_dia > 31 and escolha_mes > 12:
            print("data inválida!")
            agendar_manutencao()

        data_manutencao = f"{escolha_dia}/{escolha_mes}"
        manutecoes_agendadas[escolha_manutecao] = data_manutencao
        Menu()

    else:
        print("Escolha inválida")
        agendar_manutencao()


def equipamento_registrados():
    # for equipamento in equipamentos_UTI:
    #     print(f"Nome: {equipamento.nome}\nNúmero de série: {equipamento.numero_serie}\nData de aquisição: {equipamento.data_aquisicao}\nData de manutenção: {equipamento.data}\nTipo de manutenção: {equipamento.tipo_manutencao}\nQuantidade de intervenções: {equipamento.intervencao}\n")
    with open("novoequipamento.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(f"{conteudo}")
    Menu()


def manutencao_agendada():
    print("Manutenções agendadas\n")
    for equipamento, data in manutecoes_agendadas.items():
        print(f"{equipamento} possuí data marcada para a data: {data}\n")
    Menu()


def Menu():
    print("-------- Menu de registro do equipamentos -------- ")
    print("[1] Ver equipamentos registrados")
    print("[2] Adicionar novos equipamentos")
    print("[3] Agendar uma nova manutenção")
    print("[4] Ver manutenções anteriores")
    print("[5] Encerrar serviço\n")
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
            manutencao_agendada()
        case 5:
            pass
        case _:
            print("opção inválida")
            Menu()


Menu()
