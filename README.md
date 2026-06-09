CSV to Excel Converter

Aplicação desenvolvida em Python com Streamlit para conversão automática de arquivos CSV em Excel (.xlsx), permitindo upload múltiplo e download consolidado em arquivo ZIP.

Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- OpenPyXL
- ZipFile

Funcionalidades

- Upload de múltiplos arquivos CSV
- Conversão automática para Excel
- Geração de arquivo ZIP para download
- Interface simples e intuitiva

Objetivo

Automatizar a conversão de arquivos CSV para Excel de forma prática e rápida, facilitando processos de tratamento e organização de dados.

Como executar

pip install -r requirements.txt
streamlit run app.py

Estrutura do projeto

📁 csv-to-excel-converter
 ┣ 📄 app.py
 ┣ 📄 requirements.txt
 ┗ 📄 README.md

Demonstração

O usuário pode selecionar um ou mais arquivos CSV e baixar automaticamente os arquivos convertidos em Excel dentro de um arquivo ZIP.
