import random
import streamlit as st

st.title("JOGO DA ADIVINHANÇÃO")
st.write("Você tem 5 tentativas para acertar o número secreto")

if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 20)

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 5

if "fim_de_jogo" not in st.session_state:
    st.session_state.fim_de_jogo = False

if "mensagem" not in st.session_state:
    st.session_state.mensagem = ""

if "ultimo_numero" not in st.session_state:
    st.session_state.ultimo_numero = None

st.write(f"Resta(m): {st.session_state.tentativas} tentativa(s)")

with st.form("form_palpite", clear_on_submit=True):
    numero_escolhido = st.text_input("Por favor, escolha um número entre 1 e 20:")
    enviar = st.form_submit_button("Enviar")

if enviar and not st.session_state.fim_de_jogo:
    if numero_escolhido.strip() == "":
        st.session_state.mensagem = "Digite um número."
    elif not numero_escolhido.strip().isdigit():
        st.session_state.mensagem = "Digite apenas números inteiros."
    else:
        numero_escolhido = int(numero_escolhido)

        if numero_escolhido < 1 or numero_escolhido > 20:
            st.session_state.mensagem = "Digite um número entre 1 e 20."
        else:
            st.session_state.ultimo_numero = numero_escolhido

            if numero_escolhido == st.session_state.numero_secreto:
                st.session_state.mensagem = "Parabéns, você acertou"
                st.session_state.fim_de_jogo = True
            elif numero_escolhido < st.session_state.numero_secreto:
                st.session_state.mensagem = f"Você digitou {numero_escolhido}\n\nMuito baixo"
                st.session_state.tentativas -= 1
            else:
                st.session_state.mensagem = f"Você digitou {numero_escolhido}\n\nMuito alto"
                st.session_state.tentativas -= 1

            if st.session_state.tentativas == 0 and not st.session_state.fim_de_jogo:
                st.session_state.mensagem = "Fim de jogo"
                st.session_state.fim_de_jogo = True

if st.session_state.mensagem:
    st.write(st.session_state.mensagem)

if st.session_state.fim_de_jogo:
    st.write(f"O número secreto foi: {st.session_state.numero_secreto}")

    if st.button("Jogar novamente"):
        st.session_state.numero_secreto = random.randint(1, 20)
        st.session_state.tentativas = 5
        st.session_state.fim_de_jogo = False
        st.session_state.mensagem = ""
        st.session_state.ultimo_numero = None
        st.rerun()
