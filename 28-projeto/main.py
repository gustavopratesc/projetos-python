def row(size=30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('Sistemas de notas de alunos') 

# Lista para armazenar todos os alunos
students = []

def student_grading_system():
    row()
    print("Resultados Finais".center(30))
    row()
    for student in students:
        print(f"Nome: {student['name']}")
        print(f"Nota: {student['note']}")
        if student['note'] >= 7:
            print('Situação: Aprovado')
        elif student['note'] > 5 and student <= 6:
            print('Situação: Recuperação')
        else:
            print('Situação: Reprovado')
        print("-" * 30)

# Loop principal
while True:
    student = input('Insira o nome do aluno: ').strip().title()
    if not student:
        print('ERRO: Nenhum nome fornecido!')
        break

    try:
        note = float(input('Insira a nota do aluno: '))
    except ValueError:
        print('ERRO: Valor inserido não é numérico')
        break

    # Guarda os dados em dicionário
    students.append({"name": student, "note": note})

    advance = input('Quer continuar? [S/N]: ').strip().upper()
    if advance == 'S':
        continue
    elif advance == 'N':
        student_grading_system()
        break
    else:
        print('Insira apenas [S/N]!')
