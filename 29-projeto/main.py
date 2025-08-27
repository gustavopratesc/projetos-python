# 1. Sistema de Cadastro de Alunos (Listas + Dicionários)
# Crie um programa que:
# Peça o nome de um aluno e suas 3 notas.
# Salve as informações em um dicionário com {"nome": ..., "notas": [...]}.
# Guarde cada aluno em uma lista.
# No final, mostre todos os alunos com suas médias.
# 📌 Desafio extra: mostrar o aluno com a maior média.

def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('CADASTRO DE ALUNOS')

students = []

def show_students(student):
    best_student = None
    max_average = 0
    for student in students:
        average = sum(student["notas"]) / len(student["notas"])
        print(f'Nome: {student["nome"]} | Notas: {student["notas"]} | Media: {average:.2f}')
        if average > max_average:
            max_average = average
            best_student = student["nome"]

    row()
    print(f'Aluno com maior média: {best_student} | {max_average:.2f}')

while True:
    name_student = str(input('Insira o nome do aluno: ')).strip().title()
    if not name_student:
        print('ERRO: Nenhum nome inserido!')
        continue

    notes = []

    try:
        for i in range(3):
            note = float(input(f'Insira a {i + 1}° nota do aluno: '))
            notes.append(note)
    except ValueError:
        print('ERRO: Valor inserido não é númerico')
        continue

    student = {"nome": name_student, "notas": notes}
    students.append(student)

    row()
    advance = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if advance == 'S':
        continue
    elif advance == 'N':
        menu('RESULTADOS')
        show_students(students)
        break
    else:
        print('ERRO: Escolha entre [S/N]!')
        
