def lista_tarefas():
    tarefas = []

    while True:
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Exibir tarefas")
        print("4 - Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada.")
        elif opcao == 2:
            tarefa = input("Digite a tarefa a ser removida: ")
            if tarefa in tarefas:
                tarefas.remove(tarefa)
                print("Tarefa removida.")
            else:
                print("Tarefa não encontrada.")
        elif opcao == 3:
            print("Lista de tarefas:")
            for tarefa in tarefas:
                print("-", tarefa)
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")

lista_tarefas()