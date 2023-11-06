from profissional_hospital import *

def cadastro(profissionais):
    repetir = ''
    cargos = ["Enfermeiro","Técnico","Médico"]

    while repetir != "n":

        nome = input("Digite o nome do funcionario: ")
        cargo = input("Digite o cargo do funcionario: ")
        experiencia = input("Digite a experiencia do funcionario: ")
        contato = input("Digite o contato do funcionario: ")
        status = "Disponivel"
        pessoa = Profissional(nome,cargo,experiencia,contato,status)
        print(pessoa.nome)
        profissionais.append(pessoa)
        
        repetir = input("Deseja repetir?: ")

        while repetir !="s" and repetir !="n":
            print("Caracter n aceito")
            repetir = input("Deseja repetir?: ")

def alocar_turno(profisisonais,turnos):
    
    print("Escolha o dia que deseja alocar o profissional")
    for index, dia in enumerate(dias_da_semana):
        print(index,'-',dia)
    
    data = int(input("Digite o numero desejado:"))
    while data > len(dias_da_semana):
        print("Data invalida")
        data = int(input("Digite o numero desejado:"))
        

    print("-"*50)
    print("Escolha o turno que deseja alocar o profissional")
    for index, horario in enumerate(horarios):
        print(index,'-',horario)
    horario = int(input("Digite o numero desejado:"))

    while horario > len(horarios):
        print("Horario invalido")
        horario = int(input("Digite o numero desejado:"))

    turno = Turno(dias_da_semana[data],horarios[horario],"12 Horas","Competencia")

    for index, prof in enumerate(profisisonais):
        print("-"*50)
        print(index,'.')
        print(f"NOME:{prof.nome}\nCARGO:{prof.cargo}\nSTATUS:{prof.status}\nHORARIO:{prof.turnos_agendados}")
        print("-"*50)

    escolha = int(input("Escolha o profissional a ser designado para o turno: "))
    turnos.append(turno)
    
    print(turno.data)

    
    if len(turnos) > 1 and escolha < len(profisisonais) and profisisonais[escolha].turnos_agendados:
        if profisisonais[escolha].turnos_agendados[0][0] == turno.data and profisisonais[escolha].turnos_agendados[0][1] == turno.horario:
            print("ALOCAÇÃO INVALIDA | DATA E HORA JA OCUPADOS\n")

    else:
        profisisonais[escolha].alocar_turno(turno)
        print(profisisonais[escolha].turnos_agendados[0][0])
        # print(profisisonais[escolha].turnos_agendados[0][1])
        turno.alocar_profissional(profisisonais[escolha])

        for index, turno in enumerate(turnos):
            print(index,'.')
            if turno.profissional_alocado: print(f"NOME:{turno.profissional_alocado.nome}\nCARGO:{turno.profissional_alocado.cargo}\nSTATUS:{turno.profissional_alocado.status}\nDATA:{turno.data}\nHORARIO:{turno.horario}")
            print("-"*50)


def gerar_relatorio(profissionais, turnos):
    with open('escalas_de_trabalho.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for turno in turnos:
            writer.writerow([turno.data, turno.horario, turno.profissional_alocado.nome if turno.profissional_alocado else "Não alocado", turno.carga_horaria, ", ".join(turno.competencias),turno.horas_trabalhadas,turno.profissional_alocado.status if turno.profissional_alocado else "Disponivel"])

    tabela_de_escala = pd.read_csv(arquivo_csv, header=None, names=["Data", "Horário", "Profissional Alocado", "Carga Horária", "Competências","Registro","Status"],encoding='latin1')
    tabela_de_escala.to_excel(excel_file, index=False)


def main():
    profissionais = []
    turnos = []

    while True:
        print("\n-*-*-*-*-*-*- GESTÃO DE EQUIPES -*-*-*-*-*-*-")
        print("[1] - Cadastrar profissional")
        print("[2] - Alocação de plantão")
        print("[3] - Gerar de escala de trabalho")
        
        user_input = input("\nEscolha a opção desejada: ")

        match user_input:
            case '1':
                cadastro(profissionais)
            case '2':
                alocar_turno(profissionais,turnos)
            case '3':
                gerar_relatorio(profissionais,turnos)


if __name__ == "__main__":
    main()