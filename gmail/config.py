import email.message
import emoji
import smtplib


def config_email():

    emojis = emoji.emojize(':v: :wink:', use_aliases=True)

    corpo_email = f"""
    <p>Testando inteligência artifical para envio de emails automático feito em Python</p>
    <p>Abs,</p>
    <p>Guilherme {emojis}</p>
    """

     # Configurações do email
    msg = email.message.Message()
    msg['Subject'] = 'E-mail Automático'
    msg['From'] = input(str('De: '))
    msg['To'] = input(str('Para: '))
    password = input(str('Senha: '))
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Credenciais de login para envio do email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
