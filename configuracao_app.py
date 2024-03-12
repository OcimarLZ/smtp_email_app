import configparser

def config_app(cfg):
    # lê o arquivo de configuração
    anexos = cfg.get("Email", "ANEXOS")
    lista_enderecos = cfg.get("Email", "LISTA_ENDERECOS")
    formato_lista = cfg.get("Email", "FORMATO_LISTA")
    texto_email = cfg.get("Email", "CORPO_EMAIL")
    autoria = cfg.get("Email", "AUTORIA")
    assunto = cfg.get("Email", "ASSUNTO")
    tratamento = cfg.get("Email", "TRATAMENTO")
    tipo_exec = cfg.get("Email", "TIPO_EXECUCAO")
    col_contato = cfg.get("Email", "COL_CONTATO")
    col_cargo = cfg.get("Email", "COL_CARGO")
    col_endereco = cfg.get("Email", "COL_ENDERECO")
    col_comando = cfg.get("Email", "COL_COMANDO")
    col_ctrl_envio = cfg.get("Email", "COL_CTRL_ENVIO")
    col_interlocutor = cfg.get("Email", "COL_INTERLOCUTOR")
    parametro = cfg.get("Email", "PARAMETRO")
    confirmar = cfg.get("Email", "CONFIRMAR")
    orgao = cfg.get("Email", "ORGAO")
    return anexos, lista_enderecos, texto_email, autoria, assunto, tratamento, tipo_exec, parametro, col_contato, col_cargo, col_endereco, col_comando, col_interlocutor, col_ctrl_envio, confirmar, orgao, formato_lista

def settings_email(cfg):
    host = cfg.get("Smtp", "SERVIDOR")
    port = cfg.get("Smtp", "PORTA")
    login = cfg.get("Smtp", "CONTA")
    senha = cfg.get("Smtp", "SENHA")
    smtpsrv = f'{host}: {port}'
    return smtpsrv, login, senha

def ler_configuracao():
    cfg = configparser.ConfigParser()
    cfg.read('config.ini', encoding='utf-8')
    return cfg
