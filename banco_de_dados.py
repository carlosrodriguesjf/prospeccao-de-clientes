
# Criar banco de dados 
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd


# importando variaveis
load_dotenv()
nome_bd = os.getenv('NOME_BD')
usuario_bd = os.getenv('USUARIO_BD')
senha_bd = os.getenv('SENHA_BD')
porta_bd = os.getenv('PORTA_BD')



# função para conexão com o banco de dados
def criar_conexao(nome_bd, usuario_bd, senha_bd, porta_bd):
    conexao = psycopg2.connect(
        dbname = nome_bd,
        user= usuario_bd,
        password= senha_bd,
        port= porta_bd
    )
    return conexao


# função para criar tabela no banco de dados
def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS empresas (
                id SERIAL PRIMARY KEY,
                razao_social VARCHAR(255) NOT NULL,
                nome_fantasia VARCHAR(255),
                cnpj VARCHAR(30),
                cnae_principal VARCHAR(50),
                endereco VARCHAR(255),
                cidade VARCHAR(50),
                estado VARCHAR(2),
                pais VARCHAR(50),
                email VARCHAR(50),
                telefone VARCHAR(30),
                situacao_cadastral VARCHAR(7)
                );
    ''')
    conexao.commit()
    cursor.close()




# função para criar tabela no banco de dados
def preencher_tabela(conexao):
    # importando planilha
    tabela = pd.read_csv(r'C:\projetos\prospeccao-de-clientes\dados\empresas.csv')
    # criando o cursor
    cursor = conexao.cursor()

    # inserir os dados
    for registro in tabela.values:
        id, razao_social, nome_fantasia, cnpj, cnae_principal, endereco, cidade, estado, pais, email, telefone, situacao_cadastral = registro
        cursor.execute(
            "INSERT INTO empresas (id, razao_social, nome_fantasia, cnpj, cnae_principal, endereco, cidade, estado, pais, email, telefone, situacao_cadastral) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (id, razao_social, nome_fantasia, cnpj, cnae_principal, endereco, cidade, estado, pais, email, telefone, situacao_cadastral)
        )
    conexao.commit()
    cursor.close()



# consultando a tabela
def consulta_tabela(conexao):
    # criando o cursor
    cursor = conexao.cursor()
    funcionarios = pd.read_sql_query("SELECT * FROM empresas LIMIT 100", con = conexao)
    conexao.close()

    return funcionarios




conexao = criar_conexao(nome_bd, usuario_bd, senha_bd, porta_bd)




