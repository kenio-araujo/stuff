import random
import streamlit as st

st.title("Jogo de Adivinhação")

if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 20)

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

if "fim" not in st.session_state:
    st.session_state.fim = False

if "mensagem" not in st.session_state:
    st.session_state.mensagem = ""

st.write("Tente adivinhar um número entre 1 e 20.")
st.write("Você tem 5 tentativas.")

palpite = st.number_input("Digite seu palpite:", min_value=1, max_value=20, step=1)

if st.button("Tentar") and not st.session_state.fim:
    st.session_state.tentativas += 1

    if palpite == st.session_state.numero_secreto:
        st.session_state.mensagem = "Parabéns, você acertou!"
        st.session_state.fim = True
    elif palpite < st.session_state.numero_secreto:
        st.session_state.mensagem = "Muito baixo"
    else:
        st.session_state.mensagem = "Muito alto"

    if st.session_state.tentativas >= 5 and palpite != st.session_state.numero_secreto:
        st.session_state.mensagem = "Fim de jogo"
        st.session_state.fim = True

st.write(f"Tentativa {st.session_state.tentativas} de 5")

if st.session_state.mensagem:
    st.write(st.session_state.mensagem)

if st.session_state.fim:
    st.write(f"O número secreto era: {st.session_state.numero_secreto}")

if st.button("Jogar novamente"):
    st.session_state.numero_secreto = random.randint(1, 20)
    st.session_state.tentativas = 0
    st.session_state.fim = False
    st.session_state.mensagem = ""