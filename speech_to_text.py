import whisper

def transcrever_audio(caminho_audio):
    """
    Converte áudio em texto usando Whisper
    """
    model = whisper.load_model("base")
    resultado = model.transcribe(caminho_audio)
    return resultado["text"]