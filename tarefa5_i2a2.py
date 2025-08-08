
ninhos_de_tartarugas = [
    {'Região': "Praia norte", 'Quantidade de ovos': 2, 'Status': "Ameaçado", 'Risco': "🟡", 'Dias para eclosão': 30, 'Predadores': False},
    {'Região': "Praia oeste", 'Quantidade de ovos': 53, 'Status': "Danificado", 'Risco': "🔴", 'Dias para eclosão': 5, 'Predadores': True},
    {'Região': "Praia sul", 'Quantidade de ovos': 40, 'Status': "Danificado", 'Risco': "🔴", 'Dias para eclosão': 3, 'Predadores': False},
    {'Região': "Praia leste", 'Quantidade de ovos': 112, 'Status': "Intacto", 'Risco': "🟢", 'Dias para eclosão': 55, 'Predadores': False},
    {'Região': "Praia tartaruga", 'Quantidade de ovos': 89, 'Status': "Intacto", 'Risco': "🟢", 'Dias para eclosão': 48, 'Predadores': False},
    {'Região': "Baía dos corais", 'Quantidade de ovos': 75, 'Status': "Ameaçado", 'Risco': "🟡", 'Dias para eclosão': 25, 'Predadores': True},
    {'Região': "Praia noroeste", 'Quantidade de ovos': 33, 'Status': "Danificado", 'Risco': "🔴", 'Dias para eclosão': 12, 'Predadores': True},
    {'Região': "Baía esperança", 'Quantidade de ovos': 121, 'Status': "Intacto", 'Risco': "🟢", 'Dias para eclosão': 58, 'Predadores': False},
    {'Região': "Praia sudoeste", 'Quantidade de ovos': 62, 'Status': "Ameaçado", 'Risco': "🟡", 'Dias para eclosão': 35, 'Predadores': False},
    {'Região': "Costão rochoso", 'Quantidade de ovos': 45, 'Status': "Ameaçado", 'Risco': "🟡", 'Dias para eclosão': 18, 'Predadores': True},
    {'Região': "Ponta da praia", 'Quantidade de ovos': 15, 'Status': "Danificado", 'Risco': "🔴", 'Dias para eclosão': 7, 'Predadores': True},
    {'Região': "Praia da desova", 'Quantidade de ovos': 95, 'Status': "Intacto", 'Risco': "🟢", 'Dias para eclosão': 42, 'Predadores': False},
    {'Região': "Lagoa azul", 'Quantidade de ovos': 81, 'Status': "Ameaçado", 'Risco': "🟡", 'Dias para eclosão': 22, 'Predadores': False},
    {'Região': "Praia sudeste", 'Quantidade de ovos': 105, 'Status': "Intacto", 'Risco': "🟢", 'Dias para eclosão': 50, 'Predadores': True}
]


def mensagem_saida():
    """
    Aguarda a ação do usuário antes de seguir com o programa.
    Exibe uma mensagem para retorno ao menu principal.
    Utilizada como etapa final em funções que exibem dados ao usuário.

    Retorna:
    função: menu() para reiniciar o processo de navegação.
    """

    input("\nPressione ENTER para voltar ao menu de seleção. \n")
    print("\nVoltando ao menu de seleção \n")
    return menu()


def registro_de_ninhos():
    """
    Apresenta os ninhos registrados em formato tabular.
    Exibe os dados de cada ninho alinhando colunas com o operador de formatação :<15 para manter largura fixa e visual ordenado.
    Facilita a análise e comparação dos dados já inseridos.
    """

    # Contagem total de registros
    total_registros = len(ninhos_de_tartarugas)
    print(f'Total de registros: {total_registros}\n')

    # Cabeçalho para a exibição
    print(f"{'Região':<15} {'Quantidade de ovos':<20} {'Status':<15} {'Risco':<10} {'Dias para eclosão':<20} {'Predadores':<10}")
    print('-' * 80)

    # Exibindo os dados de forma ordenada utilizando operador de formatação :<n (n=número qualquer)
    for ninho in ninhos_de_tartarugas:
        print(f"{ninho['Região']:<15} {ninho['Quantidade de ovos']:<20} {ninho['Status']:<15} {ninho['Risco']:<10} {ninho['Dias para eclosão']:<20} {str(ninho['Predadores']):<10}")

    mensagem_saida()


def registrar_ninho():
    """
    Coleta e valida os dados fornecidos pelo usuário para criar um novo registro.
    Organiza as informações em um dicionário e adiciona à base de ninhos.

    Retorna:
    função: menu() após finalizar ou interromper a inserção.
    """


    # Loop principal para registro de novos ninhos, exibindo título formatado
    while True:
        print('\n',"==== ADICIONANDO NINHO AO REGISTRO ====".center(100))


        # Solicita ao usuário a região do ninho, com normalização do texto
        regiao = input("\nQual é a região da praia do ninho? \n").strip().lower().capitalize()


        # Recebe e valida a quantidade de ovos como número inteiro
        while True:
            try:
                qtd_ovos = int(input("\nQual é a quantidade de ovos no ninho? \n").strip())
                break
            except ValueError:
                print("Por favor, insira um número válido!")


        # Solicita e valida a situação do ninho entre três opções válidas
        while True:
            status = input("\nQual é a situação do ninho? (Intacto, Ameaçado, Danificado)\n").strip().lower().capitalize()
            if status == "Intacto":
                break
            elif status == "Ameaçado":
                break
            elif status == "Danificado":
                break
            else:
                print("Digite um valor válido (Intacto, Ameaçado ou Danificado.)")


        # Menu de seleção de risco com ícones visuais
        print("\nQual é o risco deste ninho?\n")
        print("1 - 🟢 Estável")
        print("2 - 🟡 Sob observação")
        print("3 - 🔴 Crítico")


        # Valida entrada do usuário e associa o emoji correspondente ao risco
        risco = None
        while True:
            selecao = input("\nIdentifique a situação de risco do ninho: \n").strip().lower()
            if selecao == "1":
                risco = "🟢"
                break
            elif selecao == "2":
                risco = "🟡"
                break
            elif selecao == "3":
                risco = "🔴"
                break
            else:
                print("Escolha uma opção válida!")


        # Solicita e valida número de dias para eclosão dos ovos
        while True:
            try:
                dias = int(input("\nQuantos dias estão estimados para a eclosão dos ovos? \n").strip())
                break
            except ValueError:
                print("Insira um número válido!")


        # Recebe informação sobre presença de predadores com validação simples
        while True:
            predadores = input("\nHá predadores por perto? (S/N)\n").strip().lower()
            if predadores == "s":
                predadores = True
                break
            elif predadores == "n":
                predadores = False
                break
            else:
                print("\nInsira uma opção válida!")


        # Monta o dicionário com todos os dados e adiciona ao registro principal
        registro = {
            'Região': regiao,
            'Quantidade de ovos': qtd_ovos,
            'Status': status,
            'Risco': risco,
            'Dias para eclosão': dias,
            'Predadores': predadores
        }

        ninhos_de_tartarugas.append(registro)
        print("\nNinho registrado com sucesso ✅")



        # Confirma se o usuário deseja fazer um novo registro ou voltar ao menu
        while True:
            confirma = input("\nDeseja fazer um novo registro? (S/N)\n").strip().lower()
            if confirma == "s":
                continue
            elif confirma == "n":
                print("\nVoltando ao menu de seleção\n")
                break
        return menu()



def media_ovos_risco_verde():
    """
    Calcula a média de ovos por ninho entre aqueles classificados com risco 'verde'.

    Filtra os dados por classificação de risco, extrai a quantidade de ovos de cada ninho,
    e computa a média aritmética. Útil para análise da fertilidade em áreas seguras.

    Retorno:
        float: Valor médio de ovos por ninho com risco verde.
    """


    # Inicializa acumuladores para cálculo da média
    total_ovos = 0
    quantidade_ninhos = 0

    # Soma os ovos apenas dos ninhos com risco '🟢'
    for ninho in ninhos_de_tartarugas:
        if ninho['Risco'] == '🟢':
            total_ovos += ninho['Quantidade de ovos']
            quantidade_ninhos += 1

    # Verifica se há registros válidos para evitar divisão por zero
    if quantidade_ninhos == 0:
        print("\nNão há ninhos com risco '🟢'.")
        return mensagem_saida()  # Evita divisão por zero se não houver ninhos com risco '🟢'

    print(f'\nA média de ovos com o risco "🟢" é de: {total_ovos / quantidade_ninhos:.2f}')
    mensagem_saida()


def ninhos_prestes_a_eclodir():
    """
    Identifica e lista os ninhos cuja data estimada de eclosão está próxima.

    Verifica a diferença entre a data atual e a estimativa de eclosão, comparando com um limiar pré-definido
    (ex.: próximos 3 dias). Utilizado para acompanhamento de ninhos em estágio final do ciclo.

    Retorno:
        List[dict]: Lista de ninhos prestes a eclodir com seus respectivos identificadores e datas.
    """


    # Conta ninhos com eclosão prevista para 5 dias ou menos
    quantidade_ninhos_eclodindo = 0
    for ninho in ninhos_de_tartarugas:
        if ninho['Dias para eclosão'] <= 5:
            quantidade_ninhos_eclodindo += 1
    print(f'\nA quantidade de ninhos que estão prestes a eclodir é: {quantidade_ninhos_eclodindo}')
    mensagem_saida()



def regiao_com_mais_risco_vermelho():
    """
    Analisa as regiões e retorna aquela com mais ocorrências de risco vermelho.

    Itera pelos ninhos agrupando por região e contabiliza apenas os que possuem risco classificado como 'vermelho'.
    Ideal para orientar decisões estratégicas e alocação de recursos.

    Retorno:
        str: Nome da região com maior número de casos de risco vermelho.
    """


    contagem_riscos_vermelhos = {}

    # Conta o número de riscos '🔴' por região
    for ninho in ninhos_de_tartarugas:
        if ninho['Risco'] == '🔴':
            regiao = ninho['Região']
            if regiao not in contagem_riscos_vermelhos:
                contagem_riscos_vermelhos[regiao] = 1
            else:
                contagem_riscos_vermelhos[regiao] += 1

    # Encontra a região com mais riscos '🔴'
    regiao_mais_risco = None
    max_riscos = 0
    for regiao, quantidade in contagem_riscos_vermelhos.items():
        if quantidade > max_riscos:
            max_riscos = quantidade
            regiao_mais_risco = regiao

    print(f'\nA região com mais risco "🔴" é: {regiao_mais_risco}')
    mensagem_saida()


def ninhos_com_predadores_e_danificados():
    """
    Conta a quantidade de ninhos que estão danificados e possuem presença de predadores.

    Utilizada para identificar situações críticas de risco à sobrevivência dos ovos.

    Retorno:
        int: Número total de ninhos com status 'Danificado' e presença de predadores.
    """

    # Soma ninhos que estão danificados e têm predadores presentes
    quantidade_ninhos_danificados_com_predadores = 0
    for ninho in ninhos_de_tartarugas:
        if ninho['Predadores'] and ninho['Status'] == 'Danificado':
            quantidade_ninhos_danificados_com_predadores += 1
    print(f'\nA quantidade de ninhos danificados com predadores é: {quantidade_ninhos_danificados_com_predadores}')

    mensagem_saida()



def menu():
    """
    Exibe o menu principal de navegação do sistema de monitoramento.

    Apresenta opções numeradas para registrar, consultar e analisar os ninhos.
    Aguarda a entrada do usuário e executa a função correspondente com base na seleção.
    O loop se repete até que o usuário escolha encerrar o sistema explicitamente.

    Retorno:
        None
    """


    # loop do menu de seleção
    while True:
        print("-"*100)
        print("MENU GUARDIÃO DAS TARTARUGAS".center(100))
        print("-"*100)

        print('\n',"1 - Registrar ninho ".center(100), '\n')

        print("2 - Registro de ninhos".center(100), '\n')

        print('3 - Exibir média de ovos com risco "🟢"'.center(100), '\n')

        print("4 - Ninhos prestes a eclodir".center(100), '\n')

        print('5 - Região com ninhos sob risco "🔴"'.center(100), '\n')

        print("6 - Ninhos com presença de predadores e danificados".center(100), '\n')

        print("7 - Encerrar sistema".center(100))

        selecionando = input('\nSelecione uma opção\n').strip().lower()

        # condicionais de chamada de funções
        if selecionando == "1":
            registrar_ninho()

        elif selecionando == "2":
            registro_de_ninhos()

        elif selecionando == "3":
            media_ovos_risco_verde()

        elif selecionando == "4":
            ninhos_prestes_a_eclodir()

        elif selecionando == "5":
            regiao_com_mais_risco_vermelho()

        elif selecionando == "6":
            ninhos_com_predadores_e_danificados()

        # para encerrar é necessário confirmar o encerramento
        elif selecionando == "7":
            confirmar = input("\nPara confirmar o encerramento do sistema digite SAIR.\nPara voltar pressione ENTER.").strip().lower()
            if confirmar == "sair":
                print("\nEncerrando o sistema...\n")
                break
            else:
                print("Não compreendi o que foi escrito. Voltando ao menu de seleção.")
                continue
        else:
            print("Selecione uma opção válida!")


# iniciando sistema
menu()