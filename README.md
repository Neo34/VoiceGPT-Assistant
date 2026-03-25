# 🎙️ Voice ChatGPT Assistant

Projeto desenvolvido para integrar tecnologias de Inteligência Artificial com entrada e saída por voz.

## 🚀 Funcionalidades

* 🎤 Conversão de voz para texto (Speech-to-Text) usando Whisper
* 💬 Geração de respostas inteligentes com ChatGPT
* 🔊 Conversão de texto para voz (Text-to-Speech) com gTTS
* 🌍 Suporte a múltiplos idiomas

---

## 🧠 Tecnologias utilizadas

* Python
* OpenAI API (ChatGPT)
* Whisper (Speech-to-Text)
* Google Text-to-Speech (gTTS)

---

## 🔄 Fluxo da aplicação

1. O usuário fornece um áudio (`audio.wav`)
2. O Whisper transcreve o áudio para texto
3. O ChatGPT gera uma resposta
4. O gTTS converte a resposta em áudio (`resposta.mp3`)

---

## 📁 Estrutura do projeto

```
voice-chatgpt/
│
├── app.py
├── speech_to_text.py
├── chatgpt_service.py
├── text_to_speech.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/voice-chatgpt.git
cd voice-chatgpt
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua API Key

No arquivo `config.py`, adicione sua chave da OpenAI:

```python
OPENAI_API_KEY = "sua-chave-aqui"
```

### 5. Execute o projeto

```bash
python app.py
```

---

## 📌 Melhorias futuras

* Interface web (Gradio ou Flask)
* Tradução automática de idiomas
* Histórico de conversas
* Deploy em nuvem (Azure/AWS)

---

## 💼 Objetivo

Projeto desenvolvido para fins educacionais e para compor portfólio profissional, demonstrando integração de IA com aplicações reais.

---

## 👨‍💻 Autor

Desenvolvido por César Constanzo 🚀

