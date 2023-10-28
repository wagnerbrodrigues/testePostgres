# Use a imagem oficial Python como base
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o código-fonte da aplicação para o diretório de trabalho
COPY . /app

# Instale as dependências da aplicação
RUN pip install psycopg2

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "testePostgres.py"]
