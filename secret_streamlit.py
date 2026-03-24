import random
import streamlit as st


if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 20)

if "tentativa" not in st.session_state:
    st.session_state.tentativa = 0

if "fim" not in st.session_state:
    st.session_state.fim = False

st.write("Jogo de adivinhação.\n")
st.write("Você tem 5 tentativas")

numero_escolhido = st.text_input("Por favor, escolha um número entre 1 e 20: ")

if st.button("Enviar") and st.session_state.fim == False:
    if numero_escolhido == "":
        st.write("Digite um número")
    else:
        numero_escolhido = int(numero_escolhido)
        st.session_state.tentativa += 1

        if numero_escolhido == st.session_state.numero_secreto:
            st.write("Parabéns, você acertou")
            st.session_state.fim = True
        elif numero_escolhido < st.session_state.numero_secreto:
            st.write(f"Você digitou {numero_escolhido}")
            st.write("Muito baixo")
        else:
            st.write(f"Você digitou {numero_escolhido}")
            st.write("Muito alto")

        if st.session_state.tentativa == 5 and st.session_state.fim == False:
            st.write("Fim de jogo")
            st.session_state.fim = True

if st.session_state.fim == True:
    st.write(f"O número secreto foi: {st.session_state.numero_secreto}")

if st.button("Reiniciar jogo"):
    st.session_state.numero_secreto = random.randint(1, 20)
    st.session_state.tentativa = 0
    st.session_state.fim = False
