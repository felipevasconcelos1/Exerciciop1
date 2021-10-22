print('Sistema: Nota de Alunos')
print('')
print(50*'-')
alunos = {}


def alfabetica():
    nomes = list(alunos.keys())
    ordem = nomes.sort()
    return ordem


print('Selecione uma opção:')
opcoes = '1. Adicionar Aluno\n2. Adicionar nota\n3. Remover Aluno\n4. Remover nota\n5. Editar nome do aluno\n6. Editar nota do aluno\n7. Buscar aluno por nome\n8. Calcular média da turma\n9. Exibir melhor aluno\n10. Exibir alunos em ordem alfabética\n11. Exibir alunos ordanos por nota\n12. Exibir alunos aprovados por média\n13. Exibir alunos na final\n14. Exibir alunos reprovados\n15. Encerra o programa\nEscolha uma opção de 1 a 15\n'
opcao = int(input(opcoes))


while opcao != 15:
    if opcao == 1:
        print('Adicionando aluno')
        print('IMPORTANTE: Para uma melhor funcionalidade do sistema, recomenda-se a digitação do nome completo')
        nome = input('Digite o nome do(a) aluno(a) a ser adicionado(a): ')
        if nome not in alunos.keys():
            nome = nome.upper()
            alunos[nome] = []
            print(f'Aluno(a) {nome} adicionado(a) com sucesso')
        else:
            print(f'O(A) aluno(a) {nome} já foi cadastrado anteriormente!')
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
    elif opcao == 3:
        print('Removendo Aluno')
        nome = input('Digite o nome do(a) aluno(a) a ser removido(a): ')
        nome = nome.upper()
        if nome in alunos.keys():
            del alunos[nome]
            print(f'Aluno(a) {nome} removido(a) com sucesso!')
        else:
            print(f'Erro! O(A) aluno(a) {nome} não foi cadastrado(a) no sistema!')
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
                remove = int(input('Qual nota deseja remover [1/2]? '))
                while remove not in [1, 2, 3]:
                    print('opção invalida. Você deve digitar 1, 2 ou 3')
                    remove = input('Qual nota deseja remover [1/2]? ')
                alunos[nome].pop(remove - 1)
                print('Nota removida com sucesso!')
            else:
                print('Aluno(a) não possui notas cadastradas.')
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
                    alunos[edit].append(alunos[nome[2]])
                    del alunos[nome]
            else:
                del alunos[nome]
        else:
            print(f'Erro! O(A) Aluno(a) {nome} não foi cadastrado(a).')
        print('Nome editado com sucesso!')
    elif opcao == 6:
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
            if editar == 1:
                nota = float(input('Digite a nova nota: '))
                alunos[nome].pop(0)
                alunos[nome].insert(0, nota)
                print('Nota editada com sucesso!')
            elif editar == 2:
                nota = float(input('Digite a nova nota: '))
                alunos[nome].pop(1)
                alunos[nome].insert(1, nota)
                print('Nota editada com sucesso!')
            elif editar == 3:
                nota = float(input('Digite a nova nota: '))
                alunos[nome].pop(2)
                alunos[nome].append(nota)
                print('Nota editada com sucesso!')
            else:
                print('Erro! Opção inválida. Tente novamente.')
        else:
            print('Aluno(a) não possui notas cadastradas.')
    elif opcao == 7:
        print('Buscando aluno por nome')
        string = ''
        busca = input('Qual aluno(a) desejas buscar? ')
        busca = busca.upper()
    elif opcao == 8:
        print('Calculando média da turma:')
        media = 'MEDIA'
        alunos[media] = []
        for notas in alunos[nome]:
            alunos[media] = sum(alunos[nome]) / 3
        print(alunos)
    elif opcao == 9:
        print('Exibir melhor aluno')
    elif opcao == 10:
        print('Exibir alunos em ordem alfabética')
        print(alfabetica())
    elif opcao == 11:
        print('Exibir alunos ordenados por nota')
    elif opcao == 12:
        print('exibir alunos aprovados por média')
    elif opcao == 13:
        print('Exibir alunos na final')
    elif opcao == 14:
        print('Exibir alunos reprovados')
    else:
        print('Opção inválida')

    opcoes = '1. Adicionar Aluno\n2. Adicionar nota\n3. Remover Aluno\n4. Remover nota\n5. Editar nome do aluno\n6. Editar nota do aluno\n7. Buscar aluno por nome\n8. Calcular média da turma\n9. Exibir melhor aluno\n10. Exibir alunos em ordem alfabética\n11. Exibir alunos ordanos por nota\n12. Exibir alunos aprovados por média\n13. Exibir alunos na final\n14. Exibir alunos reprovados\n15. Encerra o programa\nEscolha uma opção de 1 a 15\n'
    opcao = int(input(opcoes))

print(50*'-')
print('Obrigado por usar nosso sistema. Até mais!!')
print(alunos)
