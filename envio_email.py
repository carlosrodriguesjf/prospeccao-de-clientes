# SCRIPT PARA ENVIO DE E-MAILS

import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


# função para envio dos e-mails
def enviar_email(EMAIL, SENHA_EMAIL, nome_empresa, email_empresa):

    # Criar e enviar um email
    mail = EmailMessage()
    mail['Subject'] = 'Transforme seus dados em resultados e ganhe tempo com automação'
    mail['From'] = EMAIL
    mail['To'] = email_empresa

    mensagem = f'''
    <html>
    <body>
            <p>Olá {nome_empresa},</p>

            <p>Tudo bem?</p>

            <p>Nós somos a Nero Flow Tech e atuamos com soluções em Data Science e Automatização de Processos.
            Temos ajudado empresas a otimizar rotinas, reduzir erros manuais e tomar decisões mais inteligentes
            a partir dos seus próprios dados.</p>

            <p>Se sua equipe busca mais eficiência e insights estratégicos, posso apresentar ideias práticas que
            já geraram ótimos resultados em outros negócios.</p>

            <p>Que tal marcarmos uma conversa rápida para explorar como posso ajudar sua empresa?</p>

            <p>Estamos à disposição!</p>

            <p>Abraços,<br>
            Carlos Rodrigues<br>
            Cientista de Dados e Engenheiro de Automação de Processos<br></p>
            carlosrodriguesjfprojetos@gmail.com
        </body>
    </html>
    '''

    mail.add_alternative(mensagem, subtype='html')


    # Enviar o email
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL,SENHA_EMAIL)
        smtp.send_message(mail)

    print('E-mail encaminhado com sucesso')