from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de tópicos e sub-áreas
recommendations = {
    'piada': {
        'descricao': 'Aqui estão algumas categorias de piadas. Escolha uma para ouvir:',
        'opcoes': ['Animais', 'Tecnologia', 'Escola', 'Esportes', 'Profissões']
    },
    'curiosidade': {
        'descricao': 'Aqui estão algumas áreas de curiosidades. Qual delas você gostaria de saber mais?',
        'opcoes': ['Ciência', 'História', 'Tecnologia', 'Espaço', 'Natureza']
    },
    'computação': {
        'descricao': 'Quer aprender mais sobre esses tópicos de computação?',
        'opcoes': ['Programação', 'Inteligência Artificial', 'Segurança Cibernética', 'Redes', 'Banco de Dados']
    },
    'filmes': {
        'descricao': 'Aqui estão algumas categorias de filmes. Qual gênero você gosta mais?',
        'opcoes': ['Ação', 'Comédia', 'Drama', 'Ficção Científica', 'Terror']
    },
    'música': {
        'descricao': 'Que tipo de música você gostaria de ouvir mais?',
        'opcoes': ['Rock', 'Pop', 'Clássica', 'Jazz', 'Eletrônica']
    }
}

@app.route('/recommendation', methods=['POST'])
def recommend_topic():
    data = request.json
    topic = data.get('text', '').lower()

    # Verifica se o tópico principal está disponível
    if topic in recommendations:
        recommendation = recommendations[topic]
        return jsonify(recommendation)
    else:
        return jsonify({
            'descricao': 'Baseado nas suas interações, que tal explorar outros tópicos interessantes?',
            'opcoes': list(recommendations.keys())
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
