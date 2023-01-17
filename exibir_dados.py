from organizar_dados import OrganizarDados

print("Bem-vindo ao programa")
print("Esse programa analisa um diretório contendo arquivos de vendas e devoluções.\n")

while True:
    EscolherDiretorio = input("Para começar, qual é o nome do diretório que deseja analisar?")
    try:
        dados = OrganizarDados(EscolherDiretorio)
    except FileNotFoundError:
        print("Arquivo não encontrado, tente novamente!")
        continue
    else:
        dados.faturamento_produto()



