import streamlit as st
import pandas as pd
from io import BytesIO
import zipfile
import os

st.set_page_config(page_title="CSV para Excel", layout="centered")

st.title("Converter CSV para Excel")
st.caption("Selecione um ou mais arquivos CSV para converter em arquivos Excel e baixar em ZIP.")

uploaded_files = st.file_uploader(
    "Selecione os arquivos CSV",
    type=["csv"],
    accept_multiple_files=True
)

if uploaded_files and len(uploaded_files) > 0:
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in uploaded_files:
            df = pd.read_csv(file)
            
            # Criar nome do Excel
            nome_excel = os.path.splitext(file.name)[0] + ".xlsx"
            excel_buffer = BytesIO()
            df.to_excel(excel_buffer, index=False, engine="openpyxl")
            excel_buffer.seek(0)

            zipf.writestr(nome_excel, excel_buffer.read())

    zip_buffer.seek(0)

    st.success("Conversão realizada com sucesso!")

    st.download_button(
        label="Baixar arquivos Excel (ZIP)",
        data=zip_buffer,
        file_name="excel_convertidos.zip",
        mime="application/zip",
        on_click=lambda: st.session_state.clear()
    )
