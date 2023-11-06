import csv
import pandas as pd

arquivo_csv = 'escalas_de_trabalho.csv'
excel_file = 'horario.xlsx'


dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
horarios = ["00:00 - 12:00","04:00 - 16:00","06:00 - 18:00",
            "08:00 - 20:00","10:00 - 22:00","12:00 - 00:00"]



class Profissional:
    def __init__(self, nome, cargo, experiencia, contato,status):
        self.nome = nome
        self.cargo = cargo
        self.experiencia = experiencia
        self.contato = contato
        self.turnos_agendados = []
        self.status = "Disponivel"

    def alocar_turno(self, turno):
        # Adicione o turno à lista de turnos agendados do profissional
        self.turnos_agendados.append((turno.data,turno.horario))

    def solicitar_troca(self,turno_antigo, novo_turno):
        # Lógica para solicitar uma troca de turno
        pass

class Turno:
    def __init__(self, data, horario, carga_horaria, competencias):
        self.data = data
        self.horario = horario
        self.carga_horaria = carga_horaria
        self.competencias = competencias
        self.profissional_alocado = None
        self.horas_trabalhadas = None
        self.status = None

    def alocar_profissional(self, profissional):

        # Alocar um profissional ao turno
        self.profissional_alocado = profissional
        self.status = "Ocupado"
        profissional.status = "Ocupado"

    def registrar_horas_trabalhadas(self, inicio, fim, pausas, horas_extras):
        # Lógica para registrar as horas trabalhadas em um turno
        self.horas_trabalhadas = {"Entrada":inicio,"Saida":fim,"Pausas":pausas,"Horas Extras":horas_extras}


# Agora, você pode criar instâncias de enfermeiros, técnicos e turnos:

enfermeiro1 = Profissional("Enfermeiro 1", "Enfermeiro", "5 anos", "contato1","Disponivel")
enfermeiro2 = Profissional("Enfermeiro 2", "Enfermeiro", "5 anos", "contato1","Disponivel")
tecnico1 = Profissional("Técnico 1", "Técnico", "3 anos", "contato2","Disponivel")

turno1 = Turno(dias_da_semana[0], horarios[0], "12 horas", ["competencia1"])
turno2 = Turno(dias_da_semana[0], horarios[1], "12 horas", ["competencia1"])
turno3 = Turno(dias_da_semana[1], horarios[2], "12 horas", ["competencia2"])
turno4 = Turno(dias_da_semana[2], horarios[3], "12 horas", ["competencia2"])

# Alocar profissionais em turnos
turno1.registrar_horas_trabalhadas(3,5,"n","0h")
turno1.alocar_profissional(enfermeiro1)
turno2.alocar_profissional(tecnico1)
turno4.alocar_profissional(enfermeiro2)

if turno1.profissional_alocado:
    print('ok')

# Exportar dados para um arquivo CSV

with open('escalas_de_trabalho.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for turno in [turno1, turno2,turno3,turno4]:
        writer.writerow([turno.data, turno.horario, turno.profissional_alocado.nome if turno.profissional_alocado else "Não alocado", turno.carga_horaria, ", ".join(turno.competencias),turno.horas_trabalhadas,turno.profissional_alocado.status if turno.profissional_alocado else "Disponivel"])

tabela_de_escala = pd.read_csv(arquivo_csv, header=None, names=["Data", "Horário", "Profissional Alocado", "Carga Horária", "Competências","Registro","Status"],encoding='latin1')
tabela_de_escala.to_excel(excel_file, index=False)

