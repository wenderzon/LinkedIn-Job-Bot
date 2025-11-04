# 🤖 LinkedIn Job Bot

Um bot em Python que busca vagas no LinkedIn de forma automática usando **Selenium** e **pandas**, e envia os resultados por **e-mail** com HTML formatado.

---

## 🚀 Funcionalidades

- Busca vagas no LinkedIn conforme:
  - Nome da vaga
  - Cidade, Estado e País
  - Quantidade de páginas a pesquisar
- Salva os resultados em um arquivo CSV (`vagas_linkedin.csv`)
- Envia por e-mail uma lista formatada com links diretos das vagas

---

## 🛠️ Tecnologias usadas

- **Python 3**
- **Selenium**
- **pandas**
- **webdriver-manager**
- **smtplib** (para envio de e-mails)

---

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/linkedin-job-bot.git

2. Entre na pasta do projeto:

cd linkedin-job-bot

3. Instale as dependências:

python main.py

⚙️ Como usar

Execute o script:

python main.py


Insira as informações solicitadas (vaga, cidade, etc.).

O script criará o arquivo vagas_linkedin.csv e enviará um e-mail com as vagas encontradas.

📧 Configuração do Gmail

Você não pode usar sua senha normal do Gmail.

Para gerar uma senha de app:

Acesse: https://myaccount.google.com/security

Ative a verificação em duas etapas (se ainda não estiver).

Vá em Senhas de app → selecione Outro (nome personalizado) → digite "LinkedIn Bot".

Copie a senha gerada e substitua no código em:

senha_app = "SENHA_DE_APP_AQUI"

🧑‍💻 Autor

Wenderson Eduardo
📫https://www.linkedin.com/in/wendersoneduardo

📜 Licença

Este projeto está sob a licença MIT – veja o arquivo LICENSE
 para mais detalhes.

 
---

### ⚙️ **requirements.txt**
Salve com o nome **`requirements.txt`** na raiz da pasta.

pandas
selenium
webdriver-manager


---

Agora, basta ter essa estrutura final:

linkedin-job-bot/
│
├── main.py
├── README.md
├── requirements.txt
└── vagas_linkedin.csv (gerado pelo script)