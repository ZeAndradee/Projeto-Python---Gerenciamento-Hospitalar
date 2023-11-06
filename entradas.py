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

def alocar_turno(profisisonais):
    
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

    for prof in profisisonais:
        print("-"*50)
        print(f"NOME:{prof.nome}\nCARGO:{prof.cargo}\nSTATUS:{prof.status}")
        print("-"*50)
    escolha = int(input("Escolha o profissional a ser designado para o turno: "))
    
    turno.alocar_profissional(profisisonais[escolha])

    for prof in profisisonais:
        print(f"NOME:{prof.nome}\nCARGO:{prof.cargo}\nSTATUS:{prof.status}")
        print("-"*50)

def main():
    profissionais = []
    
    cadastro(profissionais)
    alocar_turno(profissionais)


if __name__ == "__main__":
    main()