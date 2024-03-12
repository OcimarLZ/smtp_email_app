# App para enviar e-mails personalizados para uma lista de contatos

Este projeto, se destina a usar uma conta do gmail para enviar uma série de emails, a partir de uma lista de contatos
personalizando o email com os dados do contato. O corpo do email vem de um arquivo em formato Html ou Txt (ainda não 
implementado o formato txt) e utiliza as configurações do CONFIG.INI para os trabalhos, sendo possível enviar e-mais para:
* para os contatos ainda não enviados
* para os contatos que já foram enviados (reenviando)
* para os contatos marcados (coluna específica na planilha)
* para os contatos apontados para um "interlocutor" que ainda não foram enviados os e-mails
* para os contatos apontados para um "interlocutor" que já foram enviados o e-mails (reenviar) 

# Instalação
Crie um projeto e instale as bibliotecas a partir do arquivo requirements.txt utilizando o terminal do python

pip install -r requirements.txt

# Crie a lista de contatos (atualmente funciona apenas para planilhas no formato XLSX)
Esta lista, deve ter ao menos as seguintes colunas:
* nome ou contato: utilizado como nome completo do contato e será utilizado para personalizar o texto do email;
* cargo: utilizado para personalizar o texto do email;
* endereco de email: será o endereço de email a ser enviado;
* interlocutor: utilizado para informar quem enviou o email (ver config.ini) pois na teoria, diversas pessoas pode estar utilizando a mesma lista
* comando: coluna que pode ser utilizada para marcar as linhas que a aplicação deve tratar (ver config.ini)
* controle de envio: para indicar se o email foi enviado

* Coloque o arquivo da lista de e-mails na pasta do projeto

# Crie o texto padrão do e-mail, ou seja, o texto do corpo do e-mail
Neste texto, há algumas palavras reservadas que ao enviar o e-mail, serão substituidas. Estas palavras reservadas serão reconhecidas quando estiverem dentro de chaves {}. Mas note, não invente palavras reservadas. Elas são apenas as criadas no código da aplicaçao. Atualmente as palavras reservadas são:
* {tratamento} : Para indicar como o contato será chamado. Ex: Excelentíssimo, Alteza, etc
* {cargo} : Para indicar qual o cargo do contato
* {contato} : Para indicar onde deverá ser utilizado o nome completo do contato
* {orgao} : Para indicar onde deverá ser utilizado o orgão de quem envia o contato

Coloque o arquivo do texto padrão na pasta do projeto

# Configure o comportamento do aplicativo no arquivo "config.ini"
Inicialmente configure a conta que será utilizada para enviar os emails. Para esta configuração, assista o video contido em https://youtu.be/N97q96BygUg?feature=shared a partir do minuto 5:00)

[Smtp]

SERVIDOR=smtp.gmail.com

PORTA=587

CONTA=endereco@gmail.com

SENHA=senha_gerada_pelo_autorizador_do_gmail

# Configure a chave de comportamento 
[Email]
### Indica se o email será com confirmação de leitura ou não
CONFIRMAR=Sim
### Informe o tipo de execução, ou seja, para que contatos serão enviados os emails
* N: Para todos ainda não enviados,
* R=Para todos já enviados,
* M=Para apenas os com a coluna marcado,
* IT=Todos de um interlocutor,
* IN=Todos de um interlocutor ainda não enviados,

TIPO_EXECUCAO=IN
### Se tipo de execucao for IN, informe aqui qual o interlocutor (quem envia o email, pois este aplicativo pode estar sendo utilizado por mais pessoas)
PARAMETRO=Ocimar - UFFS
### Formato na lista de contatos (Excel ou Google Sheet)
FORMATO_LISTA=Excel
### Planilha formato XLSX ou Google Sheet que contém a lista de contatos
LISTA_ENDERECOS=PlanilhaParlamentaresEmenda 28.xlsx
### Informe a posição das colunas onde serão capturadas as informações (se vc mudar a estrutura da planilha, precisa ajustar aqui
* COL_CONTATO=2
* COL_CARGO=4
* COL_ENDERECO=8
* COL_INTERLOCUTOR=9
* COL_COMANDO=10
* COL_CTRL_ENVIO=11
### Formato do e-mail e por consequência, do arquivo do corpo do e-mail (html ou txt)
FORMATO=html
### Subject do e-mail (título)
ASSUNTO=Apoio à EMENDA 28 - MPV 1203/2023 - Reestruturação nos planos de cargos e carreiras especializadas – Tecnologia da Informação PCCTAE/MEC
### Arquivo  do corpo do e-amil
CORPO_EMAIL=OficioParlamentar.html
### Relação de arquivos que precisam ser anexados ao e-mail (separe por vírgula). Caso não tenha anexos, deixar em branco
ANEXOS=OficioParlamentar.png, NotaTecnica-NivelSuperior.pdf
### Informe aqui a autoria do e-mail (será acrescentado ao final do corpo do email)
AUTORIA=GT - Analista de Tecnologia da Informação do PCCTAE
### Tratamento a ser dado para o contato ao ser criado o texto do e-mail
TRATAMENTO=Excelentísso
### Orgão que será substituido no texto em todo lugar que contiver {ORGAO}
ORGAO=Universidade Federal da Fronteira Sul# Arquivo de Configuracao de Automacoes em Python


# EXECUÇÃO
Execute o main.py