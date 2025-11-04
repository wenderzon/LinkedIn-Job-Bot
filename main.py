import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ====== CONFIGURAÇÕES DO USUÁRIO ======
seu_email = "seuemail@gmail.com"
senha_app = "SENHA_DE_APP_AQUI"
destinatario = "seuemail@gmail.com"  # pode mandar pra você mesmo
# ======================================

# Entradas do usuário
nome_vaga = input('Digite o nome da Vaga: ')
nome_cidade = input('Digite a Cidade: ')
nome_estado = input('Digite o Estado: ')
nome_pais = input('Digite o País: ')
numero_paginas = int(input('Quantas páginas quer buscar? '))

# Tratar strings para URL
vaga_tratada = quote(nome_vaga)
cidade_tratada = quote(nome_cidade)
estado_tratado = quote(nome_estado)
pais_tratado = quote(nome_pais)

# Configurar o navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

dados = []

for page in range(numero_paginas):
    start = page * 25
    url = f'https://www.linkedin.com/jobs/search?keywords={vaga_tratada}&location={cidade_tratada}%2C%20{estado_tratado}%2C%20{pais_tratado}&start={start}'
    
    driver.get(url)
    sleep(3)
    
    vagas = driver.find_elements(By.CLASS_NAME, 'base-card__full-link')
    empresas = driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')
    locais = driver.find_elements(By.CLASS_NAME, 'job-search-card__location')

    for i in range(len(vagas)):
        titulo = vagas[i].text.strip()
        link = vagas[i].get_attribute('href')
        empresa = empresas[i].text.strip() if i < len(empresas) else ''
        local = locais[i].text.strip() if i < len(locais) else ''
        dados.append({'Título': titulo, 'Empresa': empresa, 'Local': local, 'Link': link})
    
    print(f'✅ Página {page+1} coletada ({len(vagas)} vagas)')

driver.quit()

# Criar DataFrame
df = pd.DataFrame(dados)
csv_path = 'vagas_linkedin.csv'
df.to_csv(csv_path, index=False, encoding='utf-8')
print(f'\n📁 {len(dados)} vagas salvas em "{csv_path}"!')

# ====== ENVIAR EMAIL ======
mensagem_html = "<h2>Vagas encontradas:</h2><ul>"
for i, linha in df.iterrows():
    mensagem_html += f"<li><b>{linha['Título']}</b> - {linha['Empresa']} ({linha['Local']})<br><a href='{linha['Link']}'>Ver vaga</a></li>"
mensagem_html += "</ul>"

msg = MIMEMultipart()
msg['From'] = seu_email
msg['To'] = destinatario
msg['Subject'] = f"Vagas encontradas: {nome_vaga} em {nome_cidade}"

msg.attach(MIMEText(mensagem_html, 'html'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(seu_email, senha_app)
    server.send_message(msg)
    server.quit()
    print("📧 E-mail enviado com sucesso!")
except Exception as e:
    print("❌ Erro ao enviar e-mail:", e)

'''
⚙️ 2. Configurar Gmail
🧠 Importante:

Você não pode usar sua senha normal do Gmail.

O Google exige uma “Senha de app” para scripts como este:

Acesse: https://myaccount.google.com/security

Ative a verificação em duas etapas (se ainda não estiver ativada).

Vá em Senhas de app.

Escolha o app “Outro (nome personalizado)” → digite “LinkedIn Bot”.

Copie a senha gerada (16 caracteres, tipo abcd efgh ijkl mnop).

Guarde-a — é a que você vai usar no script.

'''