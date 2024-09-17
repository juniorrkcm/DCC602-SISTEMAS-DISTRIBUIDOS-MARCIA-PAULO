# Use uma imagem Python base
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos para o container
COPY requirements.txt requirements.txt

# Instale as dependências Python no container
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do diretório atual para o diretório de trabalho do container
COPY . .

# Exponha a porta que será usada pelo Flask
EXPOSE 5003

# Defina o comando padrão para executar o bot quando o container iniciar
CMD ["python", "chatbot.py"]
