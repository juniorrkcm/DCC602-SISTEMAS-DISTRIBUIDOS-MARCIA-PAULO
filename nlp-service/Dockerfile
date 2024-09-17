# Use a imagem base Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do microsserviço
COPY . .

# Exponha a porta que será usada pelo Flask
EXPOSE 5001

# Comando para rodar o aplicativo Flask
CMD ["python", "nlp_service.py"]
