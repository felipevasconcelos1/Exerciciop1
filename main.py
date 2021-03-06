print('')
print('Sistema: Nota de Alunos')
print(50*'-')
print('')
alunos = {}

def calcula_media(notas):
    media = sum(notas)/3
    return media


def exibe_aluno(pos, nome, notas):
    print('%d. %s. Notas: %s. Média: %.1f' % (pos, nome, str(notas), calcula_media(notas)))

def media_turma(alunos):
    soma_medias = 0
    for aluno in alunos:
        notas = alunos[aluno]
        soma_medias += calcula_media(notas)
    return soma_medias / len(alunos)

# 9
def melhor_aluno() :
    melhor = 0
    best = " "
    for nome in alunos:
        media = sum(alunos[nome]) / 3
        if media > melhor:
            melhor = media
            best = nome
    print(f"{best} - Média: {melhor}")


# 10
def alunos_alfabetica() :
    alfabetica = list(alunos.keys())
    alfabetica.sort()
    pos = 1
    for nome in alfabetica :
        nota = alunos[nome]
        print(f"{pos} {nome}, Notas: {nota}, Media: %.1f" % (sum(nota)/3))
        pos += 1
    

def aprovados():
    for nome in alunos:
        media = sum(alunos[nome]) / 3
        if media >= 7:
            print(nome)


def alunos_final():
    for nome in alunos:
        media = sum(alunos[nome]) / 3
        if media < 7 and media >= 5:
            print(nome)


def alunos_reprovados():
    for nome in alunos:
        media = sum(alunos[nome]) / 3
        if media < 5:
            print(nome)


print('Selecione uma opção:')
opcoes = '1. Adicionar Aluno\n2. Adicionar nota\n3. Remover Aluno\n4. Remover nota\n5. Editar nome do aluno\n6. Editar nota do aluno\n7. Buscar aluno por nome\n8. Calcular média da turma\n9. Exibir melhor aluno\n10. Exibir alunos em ordem alfabética\n11. Exibir alunos aprovados por média\n12. Exibir alunos na final\n13. Exibir alunos reprovados\n14. Encerra o programa\nEscolha uma opção de 1 a 14\n'
opcao = int(input(opcoes))
while opcao != 14:
    if opcao == 1:
        print('Adicionando aluno')
        print('IMPORTANTE: Para uma melhor funcionalidade do sistema, recomenda-se a digitação do nome completo')
        nome = input('Digite o nome do(a) aluno(a) a ser adicionado(a): ')
        nome = nome.upper()
        if nome not in alunos.keys():
            nome = nome.upper()
            alunos[nome] = []
            print(f'Aluno(a) {nome} adicionado(a) com sucesso')
        else:
            print(f'O(A) aluno(a) {nome} já foi cadastrado anteriormente!')
        print(alunos)

    elif opcao == 2:
        print('Adicionando nota')
        nome = input('De qual aluno você deseja adicior nota? ')
        nome = nome.upper()
        if nome in alunos:
            if len(alunos[nome]) < 3:
                nota = float(input('Digite a nota do(a) aluno(a): '))
                while nota < 0 or nota > 10:
                    print('Nota inválida. Insira uma nota entre 0 e 10')
                    nota = float(input('Digite a nota do aluno: '))
                alunos[nome].append(nota)
                print('Nota adicionada com sucesso!')
            else:
                print(f'O(A) aluno(a) {nome} já possui as 3 notas registradas')
        else:
            print('Erro! Aluno(a) inexistente')
        print(alunos)

    elif opcao == 3:
        print('Removendo Aluno')
        nome = input('Digite o nome do(a) aluno(a) a ser removido(a): ')
        nome = nome.upper()
        if nome in alunos.keys():
            del alunos[nome]
            print(f'Aluno(a) {nome} removido(a) com sucesso!')
        else:
            print(f'Erro! O(A) aluno(a) {nome} não foi cadastrado(a) no sistema!')
        print(alunos)

    elif opcao == 4:
        print('Removendo nota')
        nome = input('De qual aluno(a) você deseja remover a nota? ')
        nome = nome.upper()
        if nome not in alunos.keys():
            print(f'Erro! O(A) aluno(a) {nome} não foi cadastrado(a) no sistema!')
        else:
            if len(alunos[nome]) == 1:
                print(f'Aluno(a) possui a nota: {alunos[nome][0]}')
                remove = input('Deseja remove-la? [S (Sim)/ N (Não)] ')
                remove = remove.upper()
                if remove == 'S':
                    alunos[nome].pop()
                    print('Nota removida com sucesso!')
                elif remove == 'N':
                    print('Nota não removida!')
                else:
                    print('Erro. Opção inválida. Tente novamente')
            elif len(alunos[nome]) == 2:
                print(f'Aluno(a) possui as notas\n1 - {alunos[nome][0]}\n2 - {alunos[nome][1]}\n')
                remove = int(input('Qual nota deseja remover [1/2]? '))
                while remove not in [1, 2]:
                    print('opção invalida. Você deve digitar 1 ou 2')
                    remove = int(input('Qual nota deseja remover [1/2]? '))
                alunos[nome].pop(remove - 1)
                print('Nota removida com sucesso!')
            elif len(alunos[nome]) == 3:
                print(f'Aluno(a) possui as notas\n1 - {alunos[nome][0]}\n2 - {alunos[nome][1]}\n3 - {alunos[nome][2]}\n')
                remove = int(input('Qual nota deseja remover [1/2/3]? '))
                while remove not in [1, 2, 3]:
                    print('opção invalida. Você deve digitar 1, 2 ou 3')
                    remove = input('Qual nota deseja remover [1/2]? ')
                alunos[nome].pop(remove - 1)
                print('Nota removida com sucesso!')
            else:
                print('Aluno(a) não possui notas cadastradas.')
        print(alunos)

    elif opcao == 5:
        print('Editando nome do(a) aluno(a)')
        for keys in alunos.keys():
            print(keys)
        nome = input('Qual dos alunos(as) acima você deseja editar? ')
        nome = nome.upper()
        if nome in alunos.keys():
            edit = input('Digite o novo nome do aluno(a): ')
            edit = edit.upper()
            alunos[edit] = []
            if len(alunos[nome]) > 0:
                if len(alunos[nome]) == 1:
                    alunos[edit].append(alunos[nome][0])
                    del alunos[nome]
                elif len(alunos[nome]) == 2:
                    alunos[edit].append(alunos[nome][0])
                    alunos[edit].append(alunos[nome][1])
                    del alunos[nome]
                elif len(alunos[nome]) == 3:
                    alunos[edit].append(alunos[nome][0])
                    alunos[edit].append(alunos[nome][1])
                    alunos[edit].append(alunos[nome][2])
                    del alunos[nome]
            else:
                del alunos[nome]
        else:
            print(f'Erro! O(A) Aluno(a) {nome} não foi cadastrado(a).')
        print('Nome editado com sucesso!')
        print(alunos)

    elif opcao == 6:
        print(alunos)
        nome = input('Qual dos alunos(as) acima você deseja editar a nota? ')
        nome = nome.upper()
        if nome in alunos.keys():
            print('Editando nota do aluno')
            if len(alunos[nome]) == 1:
                print(f'Aluno(a) possui a nota: {alunos[nome][0]}')
                editar = input('Deseja editá-la? [S (Sim)/ N (Não)] ')
                editar = editar.upper()
                if editar == 'S':
                    nota = float(input('Digite a nova nota: '))
                    alunos[nome].pop()
                    alunos[nome].append(nota)
                    print('Nota editada com sucesso!')
                elif remove == 'N':
                    print('Operação cancelada!')
                else:
                    print('Erro. Opção inválida. Tente novamente')
            elif len(alunos[nome]) == 2:
                print(f'Aluno(a) possui as notas\n1 - {alunos[nome][0]}\n2 - {alunos[nome][1]}\n')
                editar = int(input('Qual nota deseja editar [1/2]? '))
                while editar not in [1, 2]:
                    print('Opção invalida. Você deve digitar 1 ou 2')
                    editar = int(input('Qual nota deseja remover [1/2]? '))
                if editar == 1:
                    nota = float(input('Digite a nova nota: '))
                    alunos[nome].pop(0)
                    alunos[nome].insert(0, nota)
                    print('Nota editada com sucesso!')
                elif editar == 2:
                    nota = float(input('Digite a nova nota: '))
                    alunos[nome].pop(1)
                    alunos[nome].append(nota)
                    print('Nota editada com sucesso!')
                else:
                    print('Erro! Opção inválida. Tente novamente.')
            elif len(alunos[nome]) == 3:
                print(f'Aluno(a) possui as notas\n1 - {alunos[nome][0]}\n2 - {alunos[nome][1]}\n3 - {alunos[nome][2]}\n')
                editar = int(input('Qual nota deseja editar [1/2/3]? '))
                while editar not in [1, 2, 3]:
                    print('opção invalida. Você deve digitar 1, 2 ou 3')
                    editar = int(input('Qual nota deseja remover [1/2/3]? '))
                nota = float(input('Digite a nova nota: '))
                alunos[nome].pop(editar-1)
                alunos[nome].insert(editar-1, nota)
                print('Nota editada com sucesso!')
            else:
                print('Aluno(a) não possui notas cadastradas.')
        print(alunos)

    elif opcao == 7:
        print('Buscando aluno por nome')
        busca = input('Qual aluno(a) desejas buscar? ')
        busca = busca.upper()
        pos = 1
        for aluno in alunos:
            if busca in aluno:
                exibe_aluno(pos, aluno, alunos[aluno])
            pos += 1
        print(alunos)

    elif opcao == 8:
        print('Calculando média da turma:')
        print('Media da Turma:', media_turma(alunos))

    elif opcao == 9:
        print('Exibindo melhor aluno(a):')
        print(melhor_aluno())

    elif opcao == 10:
        print('Exibir alunos em ordem alfabética\n')
        print(alunos_alfabetica())

    elif opcao == 11:
        print('exibir alunos aprovados por média')
        print(50*'-')
        print('\nAlunos aprovados por média: ')
        aprovados()
        print('')
    elif opcao == 12:
        print('Exibir alunos na final')
        print(50*'-')
        print('\nAlunos na final:')
        alunos_final()
        print('')
    elif opcao == 13:
        print('Exibir alunos reprovados\n')
        print(50*'-')
        print('\nAlunos reprovados:')
        alunos_reprovados()
        print('')
    else:
        print('Opção inválida')

    opcoes = '1. Adicionar Aluno\n2. Adicionar nota\n3. Remover Aluno\n4. Remover nota\n5. Editar nome do aluno\n6. Editar nota do aluno\n7. Buscar aluno por nome\n8. Calcular média da turma\n9. Exibir melhor aluno\n10. Exibir alunos em ordem alfabética\n11. Exibir alunos aprovados por média\n12. Exibir alunos na final\n13. Exibir alunos reprovados\n14. Encerra o programa\nEscolha uma opção de 1 a 14\n'
    opcao = int(input(opcoes))
print(50*'-')
print('Obrigado por usar nosso sistema. Até mais!!\n')
print(alunos)
