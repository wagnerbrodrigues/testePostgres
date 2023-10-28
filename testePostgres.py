import psycopg2

# Conecte ao banco de dados PostgreSQL
conexao = psycopg2.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

if conexao:
    print("Conexão ao banco de dados PostgreSQL estabelecida.")

# Crie um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Crie uma tabela (caso ela ainda não exista)
cursor.execute("CREATE TABLE IF NOT EXISTS exemplo (id SERIAL PRIMARY KEY, dado VARCHAR(255))")

# Insira uma informação na tabela
cursor.execute("INSERT INTO exemplo (dado) VALUES ('Informação de exemplo')")
conexao.commit()

# Recupere a informação da tabela
cursor.execute("SELECT dado FROM exemplo")
resultado = cursor.fetchone()
if resultado:
    print("Informação recuperada do banco de dados: " + resultado[0])
else:
    print("Nenhum dado encontrado.")

# Feche o cursor e a conexão com o banco de dados
cursor.close()
conexao.close()
