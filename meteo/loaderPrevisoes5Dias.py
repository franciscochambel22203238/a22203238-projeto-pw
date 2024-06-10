import os
import json
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1pw.settings')
django.setup()

from meteo.models import Cidade, PrevisaoProximos5Dias

PrevisaoProximos5Dias.objects.all().delete()

with open(os.path.join('meteo', 'json', 'previsoes_5dias.json'), 'r') as f:
    previsoes = json.load(f)

    for cidade, previsoes_cidade in previsoes['previsoes'].items():
        cidade_obj = Cidade.objects.get(nome=cidade)

        for previsao_dados in previsoes_cidade:
            data = datetime.strptime(previsao_dados['data'], '%Y-%m-%d').date()

            PrevisaoProximos5Dias.objects.create(
                cidade=cidade_obj,
                data=data,
                temp_min=previsao_dados['temp_min'],
                temp_max=previsao_dados['temp_max'],
                descricao_tempo=previsao_dados['descricao_tempo'],
                precipitacao=previsao_dados['precipitacao']
            )

print("Previsões para os próximos 5 dias carregadas com sucesso.")
