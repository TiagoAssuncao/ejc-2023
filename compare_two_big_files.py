import pandas as pd

def procurar_email_no_arquivo(email, arquivo_b):
    return arquivo_b[arquivo_b['email'] == email]

def procurar_cpf_no_arquivo(cpf, arquivo_b):
    return arquivo_b[arquivo_b['cpf'] == cpf]

# Caminhos para os arquivos CSV
caminho_arquivo_a = 'emarsys.csv'
caminho_arquivo_b = 'hybris.csv'

# Carregar os arquivos CSV em dataframes
arquivo_a = pd.read_csv(caminho_arquivo_a)
arquivo_b = pd.read_csv(caminho_arquivo_b)

# Caso 1: Procurar se o email do arquivo A existe no arquivo B
resultado_caso_1 = pd.merge(arquivo_a, arquivo_b, on='email', how='inner')

# Caso 2: Procurar se o CPF do arquivo A existe no arquivo B
resultado_caso_2 = pd.merge(arquivo_a, arquivo_b, on='cpf', how='inner')

# Salvar os resultados em arquivos CSV
resultado_caso_1.to_csv('email_emarsys_on_hybris.csv', index=False)
resultado_caso_2.to_csv('cpf_emarsys_on_hybris.csv', index=False)
