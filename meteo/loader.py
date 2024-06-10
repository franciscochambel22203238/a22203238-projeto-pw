import zipfile
import os

# Defina o caminho para o arquivo ZIP e o diretório de destino
zip_file_path = os.path.join(os.path.dirname(__file__), 'zip/icons_ipma_weather.zip')
destination_dir = os.path.join(os.path.dirname(__file__), 'static/meteo')

# Imprime o caminho para depuração
print(f'Procurando o arquivo ZIP em: {zip_file_path}')

# Cria o diretório de destino se não existir
os.makedirs(destination_dir, exist_ok=True)

# Verifica se o arquivo ZIP existe
if not os.path.isfile(zip_file_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {zip_file_path}")

# Extrai os arquivos do ZIP para o diretório de destino
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(destination_dir)

print(f'Ícones descompactados para {destination_dir}')