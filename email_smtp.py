# import the smtplib module. It should be included in Python by default
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


def montar_email():
    pass

def enviar_email(srvmail, login, destinatarios, assunto, corpo_email, lista_anexos, confirmar):
    qtd_dest = destinatarios.count('@')
    # Se há destinatários, envia o e-mail para cada um deles
    if qtd_dest > 0:
        lst_dest = destinatarios.split(',')
        idx = 0
        while idx < qtd_dest:
            # Cria o documento com várias partes
            msg = MIMEMultipart()
            msg["From"] = login
            destinatario = lst_dest[idx]
            msg["To"] = destinatario
            msg["Subject"] = assunto
            if confirmar == 'Sim':
                msg['Disposition-Notification-To'] = login
            imgFilename = ''
            for anexo in lista_anexos:
                file_ext = os.path.splitext(anexo)[1].lower()
                # Anexa a imagem
                imgFilename = anexo # + '_anexo' # Repare que é diferente do nome do arquivo local!
                try:
                    with open(anexo, 'rb') as f:
                        if file_ext in ['.jpeg', '.jpg']:
                            msgImg = MIMEImage(f.read(), name=imgFilename, _subtype='jpeg')
                        elif file_ext == '.png':
                            msgImg = MIMEImage(f.read(), name=imgFilename, _subtype='png')
                        elif file_ext == '.gif':
                            msgImg = MIMEImage(f.read(), name=imgFilename, _subtype='gif')
                        elif file_ext == '.pdf':
                            msgImg = MIMEApplication(f.read(), name=imgFilename, _subtype='pdf')
                        else:
                            raise IOError("Formato de arquivo não suportado")
                except IOError:
                    msgImg = '** Não foi possível anexar a imagem da minuta do empenho'
                msg.attach(msgImg)
            # Anexa o corpo do texto
            #msgText = MIMEText('<b>{}</b><br><img src="cid:{}"><br>'.format(corpo_email, imgFilename), 'html')
            #msg.attach(msgText, 'html')
            msg.attach(MIMEText(corpo_email, 'html'))
            # Login Credentials for sending the mail
            srvmail.sendmail(login, destinatario, msg.as_string())
            idx = idx + 1
    status = 'Email enviado'
    return status

def criar_servidor_email(smtpsrv, login, senha):
    srvmail = smtplib.SMTP(smtpsrv)
    srvmail.starttls()
    srvmail.login(login, senha)
    return srvmail


