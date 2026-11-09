# iniciar: python -m streamlit run main.py

import streamlit as st

from generator import gerar_senha
from security import avaliar_senha

st.title("Gerador de Senhas")

st.sidebar.write("Customização da senha:")

tipos_de_senha = ["Números", "Simbolos", "Letras minúsculas", "Letras maiúsculas"]

selecionados = st.sidebar.multiselect("Selecione os tipos de caracteres:", tipos_de_senha)

tamanho = st.sidebar.slider(
    "Escolha o tamanho da senha:",
    min_value=8,
    max_value=64,
    value=16
)

quantas_senhas = st.sidebar.slider(
    "Escolha quantas senhas deve ser geradas:",
    min_value=1,
    max_value=10,
    value=4
)

if st.sidebar.button("Gerar senha"):
    if selecionados:
        st.subheader("Senhas Geradas:")

        for i in range(quantas_senhas):
            senha = gerar_senha(selecionados, tamanho)
            pontos = avaliar_senha(senha)

            with st.container(border=True):
                st.write(f"Senha: {i + 1}")
                st.code(senha, language=None)

                st.progress(
                pontos,
                text=f"Pontuação: {pontos}/100"
                )

                if pontos < 25:
                    st.error("Segurança: Fraca 🔴")
                elif pontos < 50:
                    st.warning("Segurança: Regular 🟡")
                elif pontos < 75:
                    st.info("Segurança: Boa 🔵")
                else:
                    st.success("Segurança: Forte 🟢")

    else:
        st.warning("Selecione pelo menos um tipo de caractere!")
