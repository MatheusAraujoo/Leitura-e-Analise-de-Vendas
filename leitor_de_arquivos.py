import os
import pandas as pd
import plotly.express as px

filename = 'Vendas'
lista_de_arquivos = os.listdir(filename)
tabela_total = pd.DataFrame()


for arquivo in lista_de_arquivos:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(filename+'/'+arquivo)
        tabela_total = pd.concat([tabela, tabela_total], ignore_index=True)

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_qtdvendas_produto = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_qtdvendas_produto)

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento_produto = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento_produto)

grafico = px.bar(tabela_qtdvendas_produto, x=tabela_qtdvendas_produto.index, y='Quantidade Vendida')
grafico.show()

grafico = px.bar(tabela_faturamento_produto, x=tabela_faturamento_produto.index, y='Faturamento')
grafico.show()




