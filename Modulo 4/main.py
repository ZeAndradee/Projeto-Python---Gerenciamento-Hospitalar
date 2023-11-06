from datetime import datetime

# Dicionário para rastrear as datas e horários disponíveis
disponibilidade = {}

# Dicionário para rastrear as regras de visita
regras_visita = {}

# Dicionário para rastrear os visitantes autorizados
visitantes_autorizados = {}

def verificar_autorizacao_uti(data, nome_visitante):
    if data in visitantes_autorizados:
        for visitante in visitantes_autorizados[data]:
            if visitante["nome"] == nome_visitante:
                return True
    return False

# Função para simular o acesso à UTI
def acesso_uti():
    data = input("Digite a data da visita (formato: YYYY-MM-DD): ")
    nome_visitante = input("Nome do visitante: ")

    if data not in disponibilidade:
        print("Data inválida. Acesso negado.")
        return

    if verificar_autorizacao_uti(data, nome_visitante):
        print("Acesso autorizado à UTI.")
        # Aqui você pode adicionar a lógica de controle de acesso à UTI
    else:
        print("Acesso negado. Visitante não autorizado.")

# Função para mostrar datas disponíveis
def mostrar_datas_disponiveis():
    print("Datas disponíveis para visita:")
    for data in disponibilidade:
        print(data)

# Função para mostrar horários disponíveis em uma data específica
def mostrar_horarios_disponiveis(data):
    if data in disponibilidade:
        print(f"Horários disponíveis para {data}:")
        for horario in disponibilidade[data]:
            print(horario)
    else:
        print("Nenhuma data disponível para visitas nesse dia.")

# Função para agendar uma visita
def agendar_visita():
    data = input("Digite a data da visita (formato: YYYY-MM-DD): ")
    print(disponibilidade[data])
    if data not in disponibilidade:
        print("Data inválida. Escolha uma data disponível.")
        return

    mostrar_horarios_disponiveis(data)

    horario = input("Digite o horário da visita (formato: HH:MM): ")
    if horario in disponibilidade[data]:
        disponibilidade[data].remove(horario)
        print(f"Visita agendada para {data} às {horario}.")

        # Solicitar informações do visitante
        nome_visitante = input("Nome do visitante: ")
        documento_identificacao = input("Documento de identificação: ")
        relacao_paciente = input("Relação com o paciente: ")

        if data in visitantes_autorizados:
            visitantes_autorizados[data].append({
                "nome": nome_visitante,
                "documento_identificacao": documento_identificacao,
                "relacao_paciente": relacao_paciente
            })
        else:
            visitantes_autorizados[data] = [{
                "nome": nome_visitante,
                "documento_identificacao": documento_identificacao,
                "relacao_paciente": relacao_paciente
            }]
        print("Visita agendada com sucesso!")

    else:
        print("Horário indisponível. Escolha um horário válido.")

# Função para definir regras de visita
def definir_regras_visita():
    data = input("Digite a data para definir regras (formato: YYYY-MM-DD): ")
    if data not in disponibilidade:
        print("Data inválida. Escolha uma data disponível.")
        return

    max_visitantes = int(input("Número máximo de visitantes por paciente: "))
    duracao_maxima = int(input("Duração máxima da visita (em minutos): "))
    horarios_permitidos = input("Horários permitidos (separados por espaço): ").split()

    # Adicionar os horários permitidos à disponibilidade
    if data in regras_visita:
        regras_data = regras_visita[data]
        regras_data["horarios_permitidos"] = horarios_permitidos
    else:
        regras_visita[data] = {
            "max_visitantes": max_visitantes,
            "duracao_maxima": duracao_maxima,
            "horarios_permitidos": horarios_permitidos
        }

    print("Regras definidas com sucesso!")
    disponibilidade[data].extend(horarios_permitidos)



# Função para mostrar visitantes autorizados para uma visita específica
def mostrar_visitantes_autorizados(data):
    if data in visitantes_autorizados:
        print(f"Visitantes autorizados para a visita em {data}:")
        for visitante in visitantes_autorizados[data]:
            print("Nome:", visitante["nome"])
            print("Documento de Identificação:", visitante["documento_identificacao"])
            print("Relação com o Paciente:", visitante["relacao_paciente"])
    else:
        print("Nenhum visitante autorizado para essa visita.")

# Inicialização: Definir datas e horários disponíveis
disponibilidade["2023-11-05"] = ["08:00", "10:00", "14:00"]
disponibilidade["2023-11-06"] = ["09:00", "11:00", "15:00"]
disponibilidade["2023-11-07"] = ["10:00", "12:00", "16:00"]

# Função para cancelar uma visita
def cancelar_visita():
    data = input("Digite a data da visita a ser cancelada (formato: YYYY-MM-DD): ")
    nome_visitante = input("Nome do visitante: ")

    if data not in disponibilidade:
        print("Data inválida. Visita não pode ser cancelada.")
        return

    if verificar_autorizacao_uti(data, nome_visitante):
        horario = input("Digite o horário da visita a ser cancelada (formato: HH:MM): ")

        if horario in visitantes_autorizados[data]:
            visitantes_autorizados[data] = [v for v in visitantes_autorizados[data] if v["nome"] != nome_visitante]
            disponibilidade[data].append(horario)
            print(f"Visita cancelada para {data} às {horario}.")

        else:
            print("Horário da visita não encontrado. Visita não pode ser cancelada.")
    else:
        print("Acesso negado. Visitante não autorizado para cancelar a visita.")

# Função para reagendar uma visita
def reagendar_visita():
    data = input("Digite a data da visita a ser reagendada (formato: YYYY-MM-DD): ")
    nome_visitante = input("Nome do visitante: ")

    if data not in disponibilidade:
        print("Data inválida. Visita não pode ser reagendada.")
        return

    if verificar_autorizacao_uti(data, nome_visitante):
        horario_atual = input("Digite o horário atual da visita a ser reagendada (formato: HH:MM): ")

        if horario_atual in visitantes_autorizados[data]:
            horario_novo = input("Digite o novo horário da visita (formato: HH:MM): ")

            if horario_novo in disponibilidade[data]:
                visitantes_autorizados[data] = [v for v in visitantes_autorizados[data] if v["nome"] != nome_visitante]
                disponibilidade[data].remove(horario_novo)
                print(f"Visita reagendada para {data} às {horario_novo}.")

            else:
                print("Horário do novo agendamento já está ocupado. Visita não pode ser reagendada.")
        else:
            print("Horário da visita atual não encontrado. Visita não pode ser reagendada.")
    else:
        print("Acesso negado. Visitante não autorizado para reagendar a visita.")

# Menu principal
while True:
    print("\nMenu:")
    print("1. Mostrar datas disponíveis")
    print("2. Agendar visita")
    print("3. Cancelar visita")
    print("4. Reagendar visita")
    print("5. Definir regras de visita")
    print("6. Mostrar visitantes autorizados")
    print("7. Controle de Acesso à UTI")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        mostrar_datas_disponiveis()
    elif escolha == "2":
        agendar_visita()
    elif escolha == "3":
        cancelar_visita()
    elif escolha == "4":
        reagendar_visita()
    elif escolha == "5":
        definir_regras_visita()
    elif escolha == "6":
        data_visita = input("Digite a data da visita para mostrar visitantes autorizados: ")
        mostrar_visitantes_autorizados(data_visita)
    elif escolha == "7":
        acesso_uti()
    elif escolha == "0":
        print("Saindo do sistema. Obrigado!")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
