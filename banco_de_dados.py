## SCRIPT PARA CONTROLE DE BANCO DE DADOS

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
                empresaKey VARCHAR(14) PRIMARY KEY,
                razaoSocial VARCHAR(255) NOT NULL,
                nomeFantasia VARCHAR(255),
                cnpj VARCHAR(30),
                cnae VARCHAR(50),
                endereco VARCHAR(255),
                cidade VARCHAR(50),
                estado VARCHAR(2),
                pais VARCHAR(50),
                email VARCHAR(50),
                telefone VARCHAR(30),
                situacaoCadastral VARCHAR(7),
                status VARCHAR(12)
                );
    ''')
    conexao.commit()
    cursor.close()




# função para criar tabela no banco de dados
def preencher_tabela(conexao):

    # importando planilha
    tabela = pd.read_csv(r'C:\projetos\prospeccao-de-clientes\dados\empresas.csv', sep = ',')

    # para teste, preencheremos a base com as 20 primeiras linhas
    tabela = tabela.head(20)

    # preenchendo a chave primaria a partir do campo cnpj
    tabela['CNPJ'].astype('str')
    tabela['Nº'] = tabela['CNPJ'].apply(lambda x: x.replace('.','').replace('/','').replace('-',''))

    # criando o cursor
    cursor = conexao.cursor()

    # inserir os dados
    for registro in tabela.values:
        
        # adiciona None para o campo "status"
        dados = list(registro) + [None]  

        cursor.execute(
            "INSERT INTO empresas (empresaKey, razaoSocial, nomeFantasia, cnpj, cnae, endereco, cidade, estado, pais, email, telefone, " \
                                    "situacaoCadastral, status) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            dados
        )

    conexao.commit()
    cursor.close()




# consultando a tabela
def consulta_tabela(conexao):
    # criando o cursor
    cursor = conexao.cursor()
    funcionarios = pd.read_sql_query("SELECT * FROM empresas LIMIT 100", con = conexao)
    #conexao.close()

    return funcionarios




# função para criar tabela no banco de dados
def atualizar_tabela(conexao, empresakey):
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE empresas SET status = %s WHERE empresakey = %s",
        ('Contatada', empresakey)
    )
    conexao.commit()
    cursor.close()



# criando a variavel conexao
conexao = criar_conexao(nome_bd, usuario_bd, senha_bd, porta_bd)



