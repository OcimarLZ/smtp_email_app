import pandas as pd
from configuracao_app import config_app, ler_configuracao, settings_email
from email_smtp import criar_servidor_email, enviar_email
from log import logger
# Transformar a relação de anexos numa lista contendo o nome do anexo em cada index
def string_para_lista(anexos):
    # Dividindo a string onde houver vírgulas e removendo espaços em branco extras
    lista_anexos = anexos.split(',')
    lista_anexos = [nome.strip() for nome in lista_anexos]
    return lista_anexos

def disparar_email(srvmail, login, senha, destinatarios, conteudo_html, lista_anexos, tratamento, cargo, contato, orgao, confirmar):
    conteudo = conteudo_html
    conteudo = conteudo.replace('{tratamento}', tratamento)
    conteudo = conteudo.replace('{cargo}',cargo)
    conteudo = conteudo.replace('{contato}', contato)
    teudo = conteudo.replace('{orgao}', orgao)
    corpo_email = conteudo
    corpo_email = corpo_email + autoria
    subject = f'{assunto}-{cargo}-{contato}'
    # Envia e-mail inicial indicando as planilhas que tem para serem automatizadas# criar o servidor de e-mail
    status = enviar_email(srvmail, login, destinatarios, subject, corpo_email, lista_anexos, confirmar)
    logger('I', f'Email enviado por {login} para o {cargo} - {contato} - {status}')

def carregar_lista_contatos(formato_lista, lista_enderecos):
    # Se é em formato excel, lê a planilha
    if formato_lista == 'Excel':
        # Ler a tabela de parlamentares
        aux_df = pd.read_excel(lista_enderecos)
        contatos_df = aux_df.fillna(value='')
    # Se a planilha estiver no google drive lê pela API
    elif formato_lista == 'Google Sheet':
        # executar a rotina que acessa o google drive e le os dados e transforma a lista em dataframe
        # Ainda não implementada
        lista = []
        contatos_df = pd.DataFrame(lista)
    return contatos_df

# ler a relação de deputados e senadores
# Cria objeto de leitura do config.ini
cfg = ler_configuracao()
# Recuperam as cfg do e-mail
smtpsrv, login, senha = settings_email(cfg)
srvmail = criar_servidor_email(smtpsrv, login, senha)
# Recupera informações do que comporá o e-amail
anexos, lista_enderecos, texto_email, autoria, assunto, tratamento, tipo_exec, parametro, col_contato, col_cargo, col_endereco, col_comando, col_interlocutor, col_ctrl_envio, confirmar, orgao, formato_lista = config_app(cfg)
# diminiu 1 pos nmo python começa com zeros
col_contato = int(col_contato) -1
col_cargo = int(col_cargo) -1
col_endereco = int(col_endereco) -1
col_interlocutor = int(col_interlocutor) -1
col_comando = int(col_comando) - 1
col_ctrl_envio = int(col_ctrl_envio) - 1
# recupera a lista de endereços
contatos_df = carregar_lista_contatos(formato_lista, lista_enderecos)
# Transforma a lista de anexos em uma lista
lista_anexos = string_para_lista(anexos)
# Ler a corpo do e-mail
# Defina o caminho para o arquivo HTML
caminho_do_arquivo = texto_email
# Use o comando with open para abrir o arquivo
with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
    conteudo_html = arquivo.read()
# Agora você pode usar a variável conteudo_html
# Por exemplo, imprimir o conteúdo

for i, dados in contatos_df.iterrows():
    # Recupera os dados da linha da planilha
    interlocutor = dados[col_interlocutor]
    contato = dados[col_contato]
    cargo = dados[col_cargo]
    destinatarios = dados[col_endereco]
    marcado = dados[col_comando]
    ctrl_envio = dados[col_ctrl_envio]
    # Avalia o comando principal
    if tipo_exec == 'N':
        # Envia para os contatos que ainda não foram enviados
        if interlocutor == '':
            status = disparar_email(srvmail, login, senha, destinatarios, conteudo_html, lista_anexos, tratamento, cargo, contato, orgao, confirmar)
    if tipo_exec == 'R':
        # Envia para os contatos que já foram enviados
        if interlocutor != '':
            status = disparar_email(srvmail, login, senha, destinatarios, conteudo_html, lista_anexos, tratamento, cargo, contato, orgao, confirmar)
    if tipo_exec == 'M':
        # Envia para os contatos marcados na coluna COMANDO
        if marcado != '':
            status = disparar_email(srvmail, login, senha, destinatarios, conteudo_html, lista_anexos, tratamento, cargo, contato, orgao, confirmar)
    if tipo_exec == 'IN':
        # Envia para os contatos de um determinado interlocutor que ainda foi foi enviado
        if interlocutor == parametro and ctrl_envio == '':
            status = disparar_email(srvmail, login, senha, destinatarios, conteudo_html, lista_anexos, tratamento, cargo, contato, orgao, confirmar)
    if tipo_exec == 'IT':
        # Envia para os contatos de um determinado interlocutor que ainda foi foi enviado
        if interlocutor == parametro:
            status = disparar_email(srvmail, login, senha, destinatarios, conteudo_html, lista_anexos, tratamento, cargo, contato, orgao, confirmar)

# Fechar o servidor de e-mail
srvmail.quit()