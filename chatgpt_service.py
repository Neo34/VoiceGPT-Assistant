from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def gerar_resposta(texto):
    """
    Envia texto para o ChatGPT e retorna resposta
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": texto}
        ]
    )

    return response.choices[0].message.content