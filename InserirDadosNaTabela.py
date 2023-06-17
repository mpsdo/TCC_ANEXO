import pyodbc
import csv

# Configurar a conexão com o banco de dados
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=<server_name>;"
    "Database=master;"
    "uid=<username>;"
    "pwd=<password>;"
)

# Criar o banco de dados "tcc" se ele ainda não existir
cursor = conn.cursor()
create_db_query = "IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'tcc') CREATE DATABASE tcc;"
cursor.execute(create_db_query)
conn.commit()

# Fechar a conexão com o banco de dados "master"
conn.close()

# Conectar-se ao banco de dados "tcc"
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=<MP\MSSQLSERVER01>;"
    "Database=tcc;"
    "uid=<sa>;"
    "pwd=<marcos123>;"
)

# Abrir o arquivo CSV e ler os dados
csv_file = r"C:\Users\MP\OneDrive - cefet-rj.br\1Faculdade\9 periodo\TCC\Python base\dados_pessoas.csv"
table_name = 'pessoas'

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Ler o cabeçalho do CSV

    # Criar a tabela no banco de dados
    cursor = conn.cursor()
    create_table_query = f"CREATE TABLE {table_name} (cpf VARCHAR(11) FOREIGN KEY REFERENCES cpf_tabela(cpf), banco VARCHAR(100), nome VARCHAR(100), mae VARCHAR(100), data_nascimento DATE, profissao VARCHAR(100));"
    cursor.execute(create_table_query)
    conn.commit()

    # Inserir os dados do CSV na tabela
    insert_query = f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?);"
    for row in reader:
        cursor.execute(insert_query, row)
    conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
