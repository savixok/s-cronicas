import streamlit as st
import os
from PIL import Image

# ========== CONFIGURAÇÃO VISUAL ==========
st.set_page_config(page_title="Só Crônicas", layout="centered")

# ========== CSS BONITO E MODERNO ==========
st.markdown("""
    <style>
    body {
        background-color: #fdfdfd;
        font-family: 'Segoe UI', sans-serif;
        color: #222;
    }

    h1 {
        font-size: 3.5em;
        text-align: center;
        font-family: 'Georgia', serif;
        margin-top: 0.2em;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 2em;
        color: #666;
    }

    .stTextArea textarea {
        font-size: 16px;
        border-radius: 12px;
        padding: 15px;
        background: #fcfcfc;
        border: 1px solid #ddd;
    }

    .stButton>button {
        background-color: #222;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        margin-top: 10px;
    }

    .stButton>button:hover {
        background-color: #444;
    }

    .cronica-card {
        border: 1px solid #ddd;
        background-color: #fefefe;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }

    .video-container {
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .intro-audio {
        text-align: center;
        margin-bottom: 2em;
    }
    </style>
""", unsafe_allow_html=True)

# ========== LOGO ==========
try:
    logo = Image.open("logosocronicas.png")
    st.image(logo, use_container_width=False, width=300)
except:
    st.markdown("<h1>Só Crônicas</h1>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Um acervo literário com alma. Leia, ouça e leve consigo cada palavra.</div>", unsafe_allow_html=True)

# ========== ÁUDIO DE INTRODUÇÃO ==========
intro_path = "introducao.mp3"
if os.path.exists(intro_path):
    st.markdown("### 🎙️ Mensagem do Vovô")
    st.audio(intro_path)
else:
    st.info("🎧 Áudio de introdução ainda não enviado.")

# ========== DIRETÓRIOS ==========
CRONICAS_DIR = "cronicas"
VIDEOS_DIR = "videos"

# ========== FUNÇÃO PARA LISTAR CRÔNICAS ==========
def listar_cronicas():
    if not os.path.exists(CRONICAS_DIR):
        return []
    return sorted([f for f in os.listdir(CRONICAS_DIR) if f.endswith(".txt")])

# ========== EXIBIR CRÔNICAS ==========
cronicas = listar_cronicas()

if not cronicas:
    st.warning("Nenhuma crônica disponível no momento.")
else:
    for i, nome_arquivo in enumerate(cronicas, start=1):
        titulo_formatado = f"Crônica {i}: {nome_arquivo.replace('_', ' ').replace('.txt', '')}"
        
        with st.expander(titulo_formatado):
            st.markdown('<div class="cronica-card">', unsafe_allow_html=True)

            caminho_txt = os.path.join(CRONICAS_DIR, nome_arquivo)
            with open(caminho_txt, "r", encoding="utf-8") as f:
                texto = f.read()

            st.subheader("📜 Texto da Crônica")
            st.text_area("", texto, height=250, disabled=True)

            with open(caminho_txt, "rb") as f:
                st.download_button("📥 Baixar Crônica", f, file_name=nome_arquivo)

            # ========== ÁUDIO DO VOVÔ SOBRE A CRÔNICA ==========
            numero = str(i).zfill(3)
            audio_path = os.path.join(VIDEOS_DIR, f"audio_{numero}.mp3")
            if os.path.exists(audio_path):
                st.markdown('<div class="video-container">', unsafe_allow_html=True)
                st.audio(audio_path)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.info("🔊 Áudio do vovô ainda não disponível.")

            st.markdown('</div>', unsafe_allow_html=True)
