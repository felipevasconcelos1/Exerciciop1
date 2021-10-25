alunos = {
    'Felipe': [9.0, 5.0, 7.5],
    'Caio': [7.0, 9.5, 5.0],
    'Thiago': [10, 10, 10]
}

media = 0
for v in alunos.values():
    media += v
    print(v)
media_turma = media / (3 * len(alunos))