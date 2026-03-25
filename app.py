from speech_to_text import transcrever_audio
from chatgpt_service import gerar_resposta
from text_to_speech import gerar_audio

def main():
    print("🎤 Assistente de Voz iniciado...\n")

    audio_path = "audio.wav"

    texto = transcrever_audio(audio_path)
    print(f"📝 Você disse: {texto}")

    resposta = gerar_resposta(texto)
    print(f"🤖 Resposta: {resposta}")

    gerar_audio(resposta)
    print("🔊 Áudio gerado com sucesso!")

if __name__ == "__main__":
    main()