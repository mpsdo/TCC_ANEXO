import csv
from faker import Faker

fake = Faker()

def gerar_dados(num_linhas):
    with open('dados_pessoas.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Número de CPF', 'Banco Utilizado', 'Nome Completo', 'Nome da Mãe', 'Data de Nascimento', 'Profissão'])
        cpfs_gerados = set()  # Conjunto para verificar a unicidade dos CPFs
        while len(cpfs_gerados) < num_linhas:
            cpf = fake.unique.random_number(digits=11)
            if cpf not in cpfs_gerados:
                cpfs_gerados.add(cpf)
                banco = fake.random_element(['Banco A', 'Banco B', 'Banco C', 'Banco D', 'Banco E'])
                nome = fake.name()
                mae = fake.name_female()
                data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%d/%m/%Y')
                profissao = fake.job()
                writer.writerow([cpf, banco, nome, mae, data_nascimento, profissao])

# Exemplo de uso para gerar 3 milhões de linhas
gerar_dados(3000000)
