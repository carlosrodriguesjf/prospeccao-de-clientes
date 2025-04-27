# PROJETO PROSPECÇÃO de CLIENTES

# importações
from banco_de_dados import criar_tabela, preencher_tabela, consulta_tabela, atualizar_tabela
from banco_de_dados import conexao
from envio_email import enviar_email
import pandas as pd
from dotenv import load_dotenv
import os


# importando variaveis
load_dotenv()
EMAIL = os.getenv('EMAIL')
SENHA_EMAIL = os.getenv('SENHA_EMAIL')


## criando tabela no banco de dados
#criar_tabela(conexao)

## preenchendo a tabela
#preencher_tabela(conexao)


# consultando a tabela
funcionarios = consulta_tabela(conexao)


#print(funcionarios)

for i in range(0, len(funcionarios)):
    empresakey = funcionarios['empresakey'][i]
    nome_empresa = funcionarios['razaosocial'][i]
    email_empresa = funcionarios['email'][i]

    enviar_email(EMAIL, SENHA_EMAIL, empresakey, nome_empresa, email_empresa, conexao, atualizar_tabela)
    









