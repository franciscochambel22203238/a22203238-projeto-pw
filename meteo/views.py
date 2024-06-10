import requests
from django.shortcuts import render
from datetime import datetime, timedelta, date
from django.http import JsonResponse, Http404
from .models import Cidade, Previsao, PrevisaoProximos5Dias

def previsao_lisboa(request):
    # Endpoint
    previsao_url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"  # 1110600 é o ID de Lisboa
    tipo_tempo_url = "https://api.ipma.pt/open-data/weather-type-classe.json"

    previsao_response = requests.get(previsao_url)
    previsao_data = previsao_response.json()  # dicionário

    tipo_tempo_response = requests.get(tipo_tempo_url)
    tipo_tempo_data = tipo_tempo_response.json()

    hoje_previsao = previsao_data['data'][0]

    nome_cidade = "Lisboa"
    temp_min = hoje_previsao['tMin']
    temp_max = hoje_previsao['tMax']
    data_previsao = datetime.strptime(hoje_previsao['forecastDate'], "%Y-%m-%d").strftime("%d/%m/%Y")
    id_weather_type = hoje_previsao['idWeatherType']

    print(tipo_tempo_data['data'][0].keys())

    descricao_tempo = next(item['descWeatherTypePT'] for item in tipo_tempo_data['data'] if item['idWeatherType'] == id_weather_type)

    icone_animated = f'meteo/w_ic_d_{id_weather_type:02d}anim.svg'

    context = {
        'nome_cidade': nome_cidade,
        'temp_min': temp_min,
        'temp_max': temp_max,
        'data_previsao': data_previsao,
        'descricao_tempo': descricao_tempo,
        'icone_animated': icone_animated,
    }

    return render(request, 'meteo/previsao_lisboa.html', context)

def previsao_tempo(request):
    return render(request, 'meteo/previsao_tempo.html')

def lista_cidades(request):
    cidades = Cidade.objects.all().values('nome')
    return JsonResponse(list(cidades), safe=False)

def previsao_hoje(request, cidade_nome):
    try:
        cidade = Cidade.objects.get(nome=cidade_nome)
    except Cidade.DoesNotExist:
        raise Http404("Cidade não encontrada")

    previsao = Previsao.objects.filter(cidade=cidade).first()
    if previsao:
        response = {
            "cidade": cidade.nome,
            "data": previsao.data,
            "temp_min": previsao.temp_min,
            "temp_max": previsao.temp_max,
            "descricao_tempo": previsao.descricao_tempo,
            "precipitacao": previsao.precipitacao,
        }
    else:
        response = {"Erro": "Previsão não encontrada para hoje"}

    return JsonResponse(response)

def previsao_proximos_5_dias(request, cidade_nome):
    try:
        cidade = Cidade.objects.get(nome=cidade_nome)
    except Cidade.DoesNotExist:
        raise Http404("Cidade não encontrada")

    previsoes = PrevisaoProximos5Dias.objects.filter(cidade=cidade)

    if previsoes.exists():
        previsoes_list = [
            {
                "data": previsao.data,
                "temp_min": previsao.temp_min,
                "temp_max": previsao.temp_max,
                "descricao_tempo": previsao.descricao_tempo,
                "precipitacao": previsao.precipitacao,
            }
            for previsao in previsoes
        ]

        response = {
            "cidade": cidade.nome,
            "previsoes": previsoes_list
        }
    else:
        response = {"Erro": "Previsões não encontradas para os próximos 5 dias"}

    return JsonResponse(response)