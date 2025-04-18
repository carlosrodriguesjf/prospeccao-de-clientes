
# Criar banco de dados 
import psycopg2


# conectando ao banco de dados
conexao = psycopg2.connect(
    dbname ='empresas_cadastradas',
    user='postgres',
    password='TESte1234@',
    port='5432'

)


# Criando a tabela do banco de dados
cursor = conexao.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS empresas (
               id SERIAL PRIMARY KEY,
               razao_social VARCHAR(255) NOT NULL,
               nome_fantasia VARCHAR(255),
               cnpj VARCHAR(20),
               cnae_principal VARCHAR(255),
               endereco VARCHAR(255),
               cidade VARCHAR(20),
               estado VARCHAR(2),
               pais VARCHAR(20),
               email VARCHAR(20),
               telefone VARCHAR(30),
               situacao_cadastral VARCHAR(7)
               );
''')
conexao.commit()



