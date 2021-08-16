import emoji
from config import config_email


def enviar_email():
    envio_email = emoji.emojize('E-mail enviado com sucesso! :wink:', use_aliases=True)

    try:
        config_email()

    except Exception as e:
        print(f'Erro ao chamar a funcao de disparo de emails! {e}')
    else:
        print(f'{envio_email}')

enviar_email()
