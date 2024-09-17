
# Chatbot com NLP e Sistema de Recomendações

Este projeto consiste na implementação de um chatbot para o **Telegram** utilizando técnicas de **Processamento de Linguagem Natural (NLP)** e um **sistema de recomendações**, tudo rodando em containers **Docker**. O objetivo do chatbot é interagir de maneira natural com os usuários, respondendo perguntas e sugerindo conteúdos baseados em interesses como piadas, curiosidades, computação, entre outros.

## Funcionalidades

- **Processamento de Linguagem Natural (NLP)** para interpretar e responder perguntas do usuário.
- **Sistema de Recomendação** que sugere tópicos de interesse (ex.: piadas, curiosidades, computação).
- Integração com o **Telegram** para enviar e receber mensagens do usuário.
- Arquitetura modular com microsserviços rodando em containers **Docker**.
- Capacidade de responder tanto perguntas diretas quanto fornecer recomendações sobre tópicos específicos.

## Estrutura do Projeto

O projeto é dividido em três microsserviços principais, cada um rodando em seu próprio container:

1. **NLP Service**: 
   - Envia a resposta gerada para o chatbot baseado na análise de linguagem natural.
   
2. **Recommendation Service**: 
   - Serviço que sugere tópicos de interesse com base nas interações anteriores.
   - Gera sugestões de categorias como piadas, curiosidades, ou computação e suas subcategorias.
   
3. **Telegram Bot Service**: 
   - Interface de comunicação com os usuários do Telegram.
   - Envia as mensagens dos usuários para os serviços de NLP e de recomendações.
   - Recebe e envia as respostas geradas pelos outros serviços.

## Tecnologias Utilizadas

- **Python 3.9**: Linguagem de programação para implementar os serviços.
- **Flask**: Framework utilizado para construir APIs simples e eficientes.
- **Docker**: Utilizado para criar containers isolados para cada serviço.
- **Telegram API**: Para conectar o chatbot ao Telegram.
- **NLP**: Técnica de processamento de linguagem natural para interpretar as mensagens.

## Como Executar o Projeto

### Pré-requisitos

- **Docker** e **Docker Compose** instalados em sua máquina.
- Uma conta de desenvolvedor no **Telegram** e um **Token de API** para o bot.

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/juniorrkcm/DCC602-SISTEMAS-DISTRIBUIDOS-MARCIA-PAULO
   cd seu-repositorio
   ```

2. Atualize o arquivo `bot_config.py` com o seu **Telegram Bot Token**:
   ```python
   TELEGRAM_TOKEN = 'SEU_TELEGRAM_BOT_TOKEN'
   ```

3. Construa e inicie os containers Docker:
   ```bash
   docker-compose up --build
   ```

4. O chatbot estará rodando e conectado ao Telegram. Agora você pode enviar mensagens diretamente para o bot e receber respostas.

### Estrutura do Projeto

```
|-- nlp-service/
|   |-- Dockerfile
|   |-- nlp_service.py
|   |-- requirements.txt
|
|-- recommendation-service/
|   |-- Dockerfile
|   |-- recommendation_service.py
|   |-- requirements.txt
|
|-- telegram-bot/
|   |-- Dockerfile
|   |-- bot_config.py
|   |-- chatbot.py
|   |-- requirements.txt
|
|-- docker-compose.yml
```

### Principais Arquivos

- **nlp-service/nlp_service.py**: Implementa o serviço de NLP.
- **recommendation-service/recommendation_service.py**: Serviço de recomendação de tópicos e subcategorias.
- **telegram-bot/chatbot.py**: Contém a lógica do bot Telegram, que interage com o usuário.
- **docker-compose.yml**: Arquivo de configuração que orquestra os serviços usando Docker.

## Contribuição

Se você quiser contribuir com este projeto, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.

## Licença

Este projeto é licenciado sob os termos da licença **MIT**.
