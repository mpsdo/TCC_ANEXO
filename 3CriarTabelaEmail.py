import csv
from faker import Faker

fake = Faker()

def gerar_dados(num_linhas):
    with open('dados_contas_email.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID da Conta de Email', 'Número de CPF', 'Email', 'Provedor de Email'])
        cpfs_gerados = set()  # Conjunto para verificar a unicidade dos CPFs
        email_id = 1  # ID da conta de e-mail
        while len(cpfs_gerados) < num_linhas:
            cpf = fake.unique.random_number(digits=11)
            if cpf not in cpfs_gerados:
                cpfs_gerados.add(cpf)
                email = fake.email()
                provedor_email = email.split('@')[1]  # Obtém o provedor de e-mail a partir do endereço completo
                writer.writerow([email_id, cpf, email, provedor_email])
                email_id += 1

# Exemplo de uso para gerar 3 milhões de linhas
gerar_dados(3000000)
