from gtts import gTTS

def gerar_audio(texto, idioma="pt"):
    """
    Converte texto em áudio
    """
    tts = gTTS(text=texto, lang=idioma)
    tts.save("resposta.mp3")
    return "resposta.mp3"