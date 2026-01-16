# Converter-Excel
import streamlit as st
import pandas as pd
from io import BytesIO
import zipfile
import os

st.set_page_config(page_title="Excel para CSV", layout="centered")

st.title("Converter Excel para CSV")
st.caption("Selecione um ou mais arquivos Excel para converter em CSV.")

uploaded_files = st.file_uploader(
    "Selecione os arquivos Excel",
    type=["xlsx", "xls"],
    accept_multiple_files=True
)

if uploaded_files and len(uploaded_files) > 0:
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in uploaded_files:
            df = pd.read_excel(file)

            nome_csv = os.path.splitext(file.name)[0] + ".csv"
            csv_buffer = BytesIO()
            df.to_csv(csv_buffer, index=False, encoding="utf-8-sig")
            csv_buffer.seek(0)

            zipf.writestr(nome_csv, csv_buffer.read())

    zip_buffer.seek(0)

    st.success("Conversão realizada com sucesso!")

    st.download_button(
        label="Baixar arquivos CSV (ZIP)",
        data=zip_buffer,
        file_name="csv_convertidos.zip",
        mime="application/zip",
        on_click=lambda: st.session_state.clear()
    )
