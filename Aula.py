import streamlit as st
import speech_recognition as sr

def principal():
    st.title("Trancrição de audio: ")
    upload = st.file_uploader("Faça upload do arquivo de audio", type=["Wav"])
    if upload is not None:
        trancrever(upload)

def trancrever(upload):
    recognizer = sr.Recognizer()
    with sr.AudioFile(upload) as source:
        st.write("Processando...")
        audio = recognizer.record(source)
        texto = recognizer.recognize_google(audio,language="pt-BR")
        st.write("Texto: ", texto)
principal()
