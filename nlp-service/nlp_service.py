import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Substitua com sua chave de API da OpenAI
openai.api_key = 'Sua chave de API'

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('text', '')

    # Faz uma chamada à API OpenAI (ChatGPT)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Modelo recomendado a partir da nova API -> errado  # Usando o modelo text-davinci-003 (ChatGPT avançado)
        messages=[
            {"role": "system", "content": "Você é um assistente útil, e responda as respostas com no maximo 100 caracteres."},
            {"role": "user", "content": text}
        ],
        max_tokens=100  # Limite de tokens na resposta
    )

    # Retornando a resposta do modelo
    return jsonify({"response": response.choices[0].message.content.strip()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

