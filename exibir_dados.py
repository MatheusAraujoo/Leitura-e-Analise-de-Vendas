from organizar_dados import OrganizarDados
#Apresentação do programa
print("Bem-vindo ao programa")
print("Esse programa analisa um diretório contendo arquivos de vendas e devoluções de todas as unidades.\n")

flag = True
while flag:
    #Pergunta qual o diretório a ser analisado, caso o arquivo não seja encontrado, é perguntado novamente.
    EscolherDiretorio = input("Para começar, qual é o nome do diretório que deseja analisar?")
    try:
        dados = OrganizarDados(EscolherDiretorio.strip().title())
    except FileNotFoundError:
        print("Arquivo não encontrado, tente novamente!")
        continue
    else:
        #exibe as opções e pede para o usuário escolher uma
        print("\n1 - Quantidade de vendas por produto\n"
              "2 - Faturamento por produto\n"
              "3 - Quantidade de vendas por loja\n"
              "4 - Faturamento por loja\n")

        opcao = input("Escolha uma das opções acima: ")

        if opcao == '1':
            dados.quantidade_vendas_produto()
        if opcao == '2':
            dados.faturamento_produto()
        if opcao == '3':
            dados.quantidade_vendas_loja()
        if opcao == '4':
            dados.faturamento_loja()

        #Pergunta se deseja utilizar o programa novamente, caso o resultado seja diferente de 's' ou 'n',
        #é perguntado novamente
        while flag:
            sn = input("Deseja fazer novamente? 's' ou 'n': ")
            if sn == 's':
                break
            elif sn == 'n':
                print("Muito obrigado por utilizar o programa!")
                flag = False
            else:
                print("Entrada inválida. Digite 's' ou 'n'!")
                continue







