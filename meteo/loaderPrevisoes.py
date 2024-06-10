import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto1pw.settings')
django.setup()

from meteo.models import Cidade, Previsao
from datetime import datetime

Previsao.objects.all().delete()

with open(os.path.join('meteo', 'json', 'previsoes.json'), 'r') as f:
    previsoes = json.load(f)

    for previsao_dados in previsoes['previsoes']:
        cidade = Cidade.objects.get(nome=previsao_dados['cidade'])
        Previsao.objects.create(
            cidade=cidade,
            data=datetime.strptime(previsao_dados['data'], '%Y-%m-%d').date(),
            temp_min=previsao_dados['temp_min'],
            temp_max=previsao_dados['temp_max'],
            descricao_tempo=previsao_dados['descricao_tempo'],
            precipitacao=previsao_dados['precipitacao']
        )

print("Previsões carregadas com sucesso.")
