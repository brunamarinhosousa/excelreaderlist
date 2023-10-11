import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "[get_sid_From_twilio]"
auth_token  = "[get_token_from_twilio]"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes {mes}  alguém bateu a meta. Vendedor:{vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+[insert_your_number]",
            from_="+12293942237",
            body=f'No mes {mes}  alguém bateu a meta. Vendedor:{vendedor}, Vendas: {vendas}')
        print(message.sid)




print(message.sid)

# Para cada arquivo :

# Verificar se algum valor na coluna vendas daquele arqivo é maior de 55.000

# Se for maior do que 55.000 -> Envia um SMS com o nome, o mês e as vendas do vendedor

# Caso não seja maior que 55.000 não quero fazer nada.

