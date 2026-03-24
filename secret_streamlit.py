import random
import streamlit as st

st.title("Jogo de Adivinhação")
st.write("Tente adivinhar o número secreto entre 1 e 20.")
st.write("Você tem 5 tentativas.")

# Criar variáveis de estado
if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 20)

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

if "fim_de_jogo" not in st.session_state:
    st.session_state.fim_de_jogo = False

if "mensagem" not in st.session_state:
    st.session_state.mensagem = ""

if "historico" not in st.session_state:
    st.session_state.historico = []

# Entrada do usuário
numero_escolhido = st.number_input(
    "Por favor, escolha um número entre 1 e 20:",
    min_value=1,
    max_value=20,
    step=1
)

# Botão para tentar
if st.button("Enviar palpite") and not st.session_state.fim_de_jogo:
    st.session_state.tentativas += 1
    st.session_state.historico.append(numero_escolhido)

    if numero_escolhido == st.session_state.numero_secreto:
        st.session_state.mensagem = "Parabéns, você acertou!"
        st.session_state.fim_de_jogo = True
    elif numero_escolhido < st.session_state.numero_secreto:
        st.session_state.mensagem = f"Você digitou {numero_escolhido}. Muito baixo."
    else:
        st.session_state.mensagem = f"Você digitou {numero_escolhido}. Muito alto."

    if st.session_state.tentativas >= 5 and not st.session_state.fim_de_jogo:
        st.session_state.mensagem = "Fim de jogo."
        st.session_state.fim_de_jogo = True

# Exibir mensagem
if st.session_state.mensagem:
    st.write(st.session_state.mensagem)

# Mostrar tentativas restantes
if not st.session_state.fim_de_jogo:
    st.write(f"Tentativa {st.session_state.tentativas} de 5")
else:
    st.write(f"O número secreto foi: {st.session_state.numero_secreto}")

# Mostrar histórico
if st.session_state.historico:
    st.write("Seus palpites:", st.session_state.historico)

# Botão para reiniciar
if st.button("Reiniciar jogo"):
    st.session_state.numero_secreto = random.randint(1, 20)
    st.session_state.tentativas = 0
    st.session_state.fim_de_jogo = False
    st.session_state.mensagem = ""
    st.session_state.historico = []
