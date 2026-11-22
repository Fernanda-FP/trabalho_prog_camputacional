# leitura do numero digitado e verifica se esta dentro dos limites
def ler_valor(mensagem, minimo, maximo):
    while True:
        valor = float(input(mensagem))
        if valor >= minimo and valor <= maximo:
            return valor
        else:
            print(f"O valor deve estar entre {minimo} e {maximo}.")


# classifica os valores inseridos com base nos intervalos
def classificar_medicao(temperatura, umidade):
    if temperatura > 35.0 or temperatura < 10.0 or umidade < 30.0 or umidade > 90.0:
        return "Alerta Critico"
    elif temperatura > 30.0 or temperatura < 18.0 or umidade < 40.0 or umidade > 70.0:
        return "Atencao"
    else:
        return "Normal"


# calcula media, valor maximo, valor minimo e amplitude
def calcular_estatisticas(lista_dados):
    soma = 0.0
    maior = lista_dados[0]
    menor = lista_dados[0]

    for valor in lista_dados:
        soma = soma + valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    media = soma / len(lista_dados)
    amplitude = maior - menor
    return media, maior, menor, amplitude


# exibe os dados registrados e suas classificacoes
def exibir_dados(temperaturas, umidades):
    if len(temperaturas) == 0:
        print("\nNenhuma medicao registrada ate o momento.")
        return

    print("\n--------------- MEDICOES REGISTRADAS ---------------")
    print("Ponto | Temperatura (°C) | Umidade (%) | Classificacao")
    print("------------------------------------------------------")
    for i in range(len(temperaturas)):
        situacao = classificar_medicao(temperaturas[i], umidades[i])
        print(f"  {i + 1:02d}  |      {temperaturas[i]:6.2f}      |   {umidades[i]:6.2f}    | {situacao}")
    print("------------------------------------------------------")


# pega a saida do classificar_medicao e do calcular_estatisticas e monta um relatorio com base nisso
def relatorio_analise(temperaturas, umidades):
    if len(temperaturas) == 0:
        print("\nDados nao registrados para fazer analise.")
        return

    media_t, max_t, min_t, amp_t = calcular_estatisticas(temperaturas)
    media_u, max_u, min_u, amp_u = calcular_estatisticas(umidades)

    total = len(temperaturas)
    qtd_normal = 0
    qtd_atencao = 0
    qtd_critico = 0

    for i in range(total):
        situacao = classificar_medicao(temperaturas[i], umidades[i])
        if situacao == "Normal":
            qtd_normal = qtd_normal + 1
        elif situacao == "Atencao":
            qtd_atencao = qtd_atencao + 1
        else:
            qtd_critico = qtd_critico + 1

    perc_critico = (qtd_critico / total) * 100

    if qtd_critico > 0:
        situacao_geral = "Ambiente em Alerta Critico"
    elif qtd_atencao > 0:
        situacao_geral = "Ambiente precisa de Atencao"
    else:
        situacao_geral = "Ambiente em condicoes Normais"

    print("\n--------------- RELATORIO DE ANALISE ---------------")
    print(f"Total de medicoes analisadas: {total}")
    print("\n--- Indicadores de Temperatura ---")
    print(f"Media: {media_t:.2f} °C | Maxima: {max_t:.2f} °C | Minima: {min_t:.2f} °C | Amplitude: {amp_t:.2f} °C")

    print("\n--- Indicadores de Umidade Relativa ---")
    print(f"Media: {media_u:.2f} %  | Maxima: {max_u:.2f} %  | Minima: {min_u:.2f} %  | Amplitude: {amp_u:.2f} %")

    print("\n--- Resumo das Classificacoes ---")
    print(f"Normal: {qtd_normal} | Atencao: {qtd_atencao} | Alerta Critico: {qtd_critico} ({perc_critico:.1f}%)")
    print(f"\nSituacao Geral: {situacao_geral}")
    print("------------------------------------------------------")


# dados sinteticos para simulacao de cenarios
def carregar_dados(tipo_cenario):
    if tipo_cenario == "1":
        # Cenario 1: Condicoes ideais
        temps = [23.5, 25.0, 26.8, 27.5, 24.2]
        umids = [58.0, 54.0, 50.0, 48.0, 60.0]
    elif tipo_cenario == "2":
        # Cenario 2: Calor intenso e baixa umidade
        temps = [29.0, 33.5, 36.2, 38.4, 34.0]
        umids = [45.0, 34.0, 25.0, 21.0, 31.0]
    else:
        # Cenario 3: Temperaturas muito frias e umidade alta
        temps = [16.5, 12.0, 8.5, 4.2, 11.0]
        umids = [75.0, 82.0, 92.0, 95.0, 88.0]
    return temps, umids