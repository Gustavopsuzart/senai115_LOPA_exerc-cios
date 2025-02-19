contAlunos = 1 # inicializar a contagem de alunos
qtdAlunos = 3 # inserir nessa var a quantidade de alunos
qtdNotas = 2 # inserir a quantidade de notas
qtdAprovados = 0
qtdReprovados = 0
qtdExame = 0
somaMedias = 0

while contAlunos <=qtdAlunos:
    print('\n')
    print('#########################')
    print(f'Aluno {contAlunos}')

    notaUm = int(input('insira a primeira nota do aluno'))
    notaDois = int(input('insira a segunda nota do aluno'))

    media = (notaUm + notaDois)/qtdNotas
    somaMedias += media

    if media < 3:
        print('Reprov')
        qtdReprovados += 1
    elif media >= 3 and media < 7:
        print('Exame')
        qtdExame += 1
    elif media >= 7:
        print('Aprovado')
        qtdAprovados += 1    

    contAlunos += 1 # cotAlunos = contAlunos + 1


mediaClasse = somaMedias/qtdAlunos
print('\n')
print('######################')
print('Resumo classe: ')
print(f'alunos aprovados: {qtdAprovados}')
print(f'alunos reprovados: {qtdReprovados}')
print(f'alunos exame: {qtdExame}')
print(f'a media da classe foi de: {mediaClasse}')