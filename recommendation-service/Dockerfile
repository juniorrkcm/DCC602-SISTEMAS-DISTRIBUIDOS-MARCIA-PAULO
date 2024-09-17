# Usar a imagem oficial do Python
FROM python:3.9-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar os requisitos
COPY requirements.txt requirements.txt

# Instalar os pacotes necessários
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Expor a porta que o Flask vai rodar
EXPOSE 5003

# Comando para rodar o app
CMD ["python", "recommendation_service.py"]
