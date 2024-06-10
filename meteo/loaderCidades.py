import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto1pw.settings')
django.setup()

from meteo.models import Cidade

Cidade.objects.all().delete()

with open(os.path.join('meteo', 'json', 'cidades.json'), 'r') as f:
    cities = json.load(f)

    for cidade_dados in cities['cidades']:
        Cidade.objects.create(
            nome = cidade_dados["nome"]
        )

print("Cidades carregadas com sucesso.")