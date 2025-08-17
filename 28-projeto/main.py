def row(size = 30):
    print('-' * size)

def menu(msg):
    row()
    print(f'{msg:^30}')
    row()

menu('Sistemas de notas de alunos') 

def student_grading_system(student, note):
    name_student = {"name": ''}
    media_student = []
    name_student['name'] += student
    media_student.append(note)
    for n in name_student.items():
        print(f'Nome: {n}')
    
    for i in media_student:
        print(f'Nota: {i}')
while True:
    student = str(input('Insira o nome do aluno: ')).strip().title()
    if not student:
        print('ERRO: Nenhum nome fornecido!')
        break
    try:
        average = float(input('Insira a nota do aluno: '))
    except ValueError:
        print('ERRO: Valor inserido não é númerico')
        break
    advance = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if advance == 'S':
        continue
    elif advance == 'N':
        print('Resultados...')
        student_grading_system(student, average)
    else:
        print('Insira apenas [S/N]!')


