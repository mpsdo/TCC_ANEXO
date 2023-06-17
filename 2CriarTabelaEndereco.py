import csv
from faker import Faker

fake = Faker()

def gerar_dados(num_linhas):
    with open('dados_enderecos.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID do Endereço', 'Número de CPF', 'Rua', 'Numero', 'Bairro', 'Cidade', 'Estado', 'CEP'])
        cpfs_gerados = set()  # Conjunto para verificar a unicidade dos CPFs
        endereco_id = 1  # ID do endereço
        while len(cpfs_gerados) < num_linhas:
            cpf = fake.unique.random_number(digits=11)
            if cpf not in cpfs_gerados:
                cpfs_gerados.add(cpf)
                rua = fake.street_name()
                numero = fake.building_number()
                bairro = fake.city_prefix()
                cidade = fake.city()
                estado = fake.state_abbr()
                cep = fake.zipcode()
                writer.writerow([endereco_id, cpf, rua, numero, bairro, cidade, estado, cep])
                endereco_id += 1

# Exemplo de uso para gerar 3 milhões de linhas
gerar_dados(3000000)
