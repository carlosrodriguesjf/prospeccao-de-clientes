# PROJETO AUTOMAÇÃO DA PROSPECÇÃO DE CLIENTES VIA E-MAIL

## 👤 Autor e Contato
- **Nome**: Carlos Rodrigues
- **E-mail**: carlosrodriguesjf@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/carlosrodriguesjf
- **GitHub**: https://github.com/carlosrodriguesjf


## 📌 Descrição e Objetivos
Demanda: Desenvolver um projeto backend em Python para prospecção de novos clientes via e-mail.

1. Importação de Dados:
O projeto deve incluir a criação de um banco de dados PostgreSQL e um script em Python para importar esses dados automaticamente.

2. Automação do Envio de E-mails:
Com os dados armazenados no PostgreSQL, será necessário desenvolver um sistema de envio automatizado de e-mails, 
utilizando Python. O envio deve ser baseado em um template pré-definido, no qual algumas informações, como o 
nome da empresa, serão personalizadas para cada destinatário.

3. Controle de Envios:
Para evitar o reenvio de e-mails para os mesmos contatos, o sistema deve registrar o status de cada envio no 
banco de dados. Isso será feito por meio de uma coluna que indique se o e-mail já foi enviado com sucesso.



## 📂 Estrutura do Projeto
```
📁 analise_cancelamento
│── 📂 dados                  # Conjunto de dados brutos e processados
│── 📂 testes                 # Arquivos e conjuntos de dados para testes
│── requirements.txt          # Dependências do projeto
│── app.py                    # Script principal
│── banco_de_dados.py         # Script de controle do banco de dados
│── envio_email.py            # Script para envio de e-mail
│── README.md                 # Arquivos de informações
```


## 📊 Dados Utilizados
Os dados possuem as seguintes colunas principais:
- **Nº**: Número de sequência de empresas
- **Razão Social**: Nome jurídico da empresa, utilizado oficialmente em contratos e documentos legais. Representa a identidade formal da organização.
- **Nome Fantasia**: Nome comercial pelo qual a empresa é conhecida no mercado. Pode ser diferente da razão social e é utilizado para facilitar o reconhecimento público.
- **CNPJ**: Cadastro Nacional da Pessoa Jurídica.
- **CNAE Principal**: Código Nacional de Atividades Econômicas. Indica a principal atividade exercida pela empresa, de acordo com a classificação oficial do IBGE.
- **Endereço**: Localização física da empresa. 
- **Cidade**: Município onde a empresa está sediada. Complementa as informações de endereço.
- **Estado**: Unidade federativa correspondente ao endereço da empresa. Normalmente coletado junto ao endereço completo
- **País**:País de localização da empresa, geralmente "Brasil", mas pode variar em casos de filiais ou sedes internacionais.
- **Email**: Endereço eletrônico de contato da empresa.
- **Telefone**: Número de contato telefônico
- **Situação Cadastral**: Indica se a empresa está ativa, inativa, suspensa ou baixada perante a Receita Federal ou órgãos reguladores.



## 🛠️ Tecnologias e Ferramentas
- **Python**
- **Pandas**
- **Banco de dados PostegreSQL**



## 🚀 Como Executar o Projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/carlosrodriguesjf/prospeccao-de-clientes.git
   cd prospeccao-de-clientes
   ```
2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Execute os notebooks ou scripts:
   ```bash
   jupyter notebook
   ```
4. Para executar a automação via Selenium:
   ```bash
   python app.py
   ```


## 🔮 Objetivos Futuros
- **Banco de dados**: Criar um banco de dados na nuvem
- **Interface**: Criar uma interface gráfica para facilitar as ações

