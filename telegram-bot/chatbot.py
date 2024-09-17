from bot_config import TELEGRAM_TOKEN
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Função que envia a mensagem do usuário para o nlp_service e recebe a resposta do GPT
def get_gpt_response(user_message):
    try:
        response = requests.post(
            "http://nlp-service:5001/process",
            json={"text": user_message},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            return response.json().get("response")
        else:
            return "Desculpe, não consegui processar sua solicitação no momento."
    except Exception as e:
        return f"Ocorreu um erro ao tentar se conectar ao serviço: {e}"

# Função que envia a mensagem do usuário para o recommendation_service
def get_recommendation(user_message):
    try:
        response = requests.post(
            "http://recommendation-service:5003/recommendation",
            json={"text": user_message},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"message": "Desculpe, não consegui processar sua solicitação no momento."}
    except Exception as e:
        return {"message": f"Ocorreu um erro ao tentar se conectar ao serviço: {e}"}

# Função que inicia o bot
def start(update, context):
    update.message.reply_text('Olá! Eu sou seu assistente virtual. Se não tiver o que perguntar, gostaria de receber uma recomendação sobre oq pesquisar? (Responda com "sim" ou "não")')
    context.user_data['recommending'] = True  # Indicador para verificar se estamos no modo recomendação

# Função que lida com as mensagens dos usuários
def handle_message(update, context):
    user_message = update.message.text.lower()

    # Se estamos no modo recomendação, o usuário decide se quer uma recomendação ou não
    if context.user_data.get('recommending'):
        if user_message == 'sim':
            update.message.reply_text("Qual tipo de recomendação você gostaria de receber? Escolha entre: piada, curiosidade, computação, filmes, música.")
            context.user_data['recommending'] = False
            context.user_data['choosing_main_topic'] = True  # Agora esperamos a escolha do tópico principal
        else:
            update.message.reply_text("Ok! Sinta-se à vontade para me perguntar qualquer outra coisa.")
            context.user_data['recommending'] = False

    # Se o usuário está escolhendo um tópico principal (piada, curiosidade, etc.)
    elif context.user_data.get('choosing_main_topic'):
        main_topic = user_message
        recommendation = get_recommendation(main_topic)
        if 'descricao' in recommendation:
            update.message.reply_text(recommendation['descricao'])
            update.message.reply_text(f"Você pode escolher entre: {', '.join(recommendation['opcoes'])}")
            context.user_data['choosing_main_topic'] = False
            context.user_data['choosing_sub_topic'] = main_topic  # Agora estamos esperando a escolha da subcategoria
        else:
            update.message.reply_text("Desculpe, não entendi esse tópico. Tente novamente.")
            context.user_data['choosing_main_topic'] = True  # Mantemos o estado para o usuário tentar novamente

    # Se o usuário está escolhendo uma subcategoria
    elif context.user_data.get('choosing_sub_topic'):
        sub_topic = user_message
        main_topic = context.user_data['choosing_sub_topic']  # Recupera o tópico principal escolhido antes
        bot_response = get_gpt_response(f"Conte-me algo sobre {sub_topic} dentro de {main_topic}")
        update.message.reply_text(bot_response)
        context.user_data['choosing_sub_topic'] = False  # Finaliza o processo de escolha de subcategoria

    else:
        # Se não estamos em modo recomendação, responde via GPT normalmente
        bot_response = get_gpt_response(user_message)
        update.message.reply_text(bot_response)



# Função para enviar uma mensagem de finalização caso o bot tenha que ser encerrado
def send_end_message(chat_id, context):
    try:
        context.bot.send_message(chat_id=chat_id, text="O bot está sendo finalizado. Obrigado por usar nosso serviço!")
    except Exception as e:
        print(f"Erro ao enviar mensagem de finalização: {e}")

# Função para enviar a mensagem de início
def send_start_message(chat_id):
    try:
        requests.post(
            f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage',
            data={'chat_id': chat_id, 'text': '/start'}
        )
    except Exception as e:
        print(f"Erro ao enviar mensagem de início: {e}")

# Configuração do bot
def main():
    try:
        updater = Updater(TELEGRAM_TOKEN, use_context=True)

        # Adiciona os handlers para comandos e mensagens
        updater.dispatcher.add_handler(CommandHandler("start", start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

        # Inicia o bot
        updater.start_polling()
        updater.idle()

    except Exception as e:
        print(f"Erro durante a execução do bot: {e}")
        # Aqui você precisa de um chat_id específico para enviar a mensagem de finalização
        chat_id = '123456789'  # Ajuste para o chat_id correto
        send_end_message(chat_id, updater.bot)  # Envia mensagem de finalização

if __name__ == '__main__':
    main()
