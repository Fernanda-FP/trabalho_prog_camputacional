from funcoes_ambientais import (
    ler_valor,
    exibir_dados,
    relatorio_analise,
    carregar_dados,
    remover_dado,
)

# menu
temperaturas = []
umidades = []
opcao = ""

while opcao != "0":
    print("\n---------- MONITORAMENTO AMBIENTAL ----------")
    print("1 - Inserir dados manualmente")
    print("2 - Carregar dados sinteticos")
    print("3 - Visualizar dados registrados")
    print("4 - Gerar relatorio de analise")
    print("5 - Apagar um dado especifico")
    print("6 - Limpar todos os dados registrados")
    print("0 - Sair")
    print("-----------------------------------------------")
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        quantidade = int(ler_valor("\nQuantos dados deseja registrar? ", 1, 50))
        for i in range(quantidade):
            print(f"\n--- Registro da Medicao {i + 1} ---")
            temp = ler_valor("Temperatura (°C) [-10 a 60]: ", -10.0, 60.0)
            umid = ler_valor("Umidade Relativa (%) [0 a 100]: ", 0.0, 100.0)
            temperaturas.append(temp)
            umidades.append(umid)
        print(f"\nSucesso: {quantidade} dado(s) adicionado(s)!")

    elif opcao == "2":
        print("\nEscolha o cenario para os dados:")
        print("1 - Cenario Normal (condicoes ideais)")
        print("2 - Cenario Critico (calor intenso e baixa umidade)")
        print("3 - Cenario Critico (frio intenso e umidade alta)")
        escolha_sim = input("Escolha uma opcao de cenario: ")

        if escolha_sim == "1" or escolha_sim == "2" or escolha_sim == "3":
            temperaturas, umidades = carregar_dados(escolha_sim)
            print("\nDados carregados com sucesso!")
        else:
            print("\nOpcao invalida")

    elif opcao == "3":
        exibir_dados(temperaturas, umidades)

    elif opcao == "4":
        relatorio_analise(temperaturas, umidades)

    elif opcao == "5":
        remover_dado(temperaturas, umidades)

    elif opcao == "6":
        temperaturas.clear()
        umidades.clear()
        print("\nTodos os dados foram apagados")

    elif opcao == "0":
        print("\nEncerrando o sistema de monitoramento ambiental")

    else:
        print("\nOpcao invalida")