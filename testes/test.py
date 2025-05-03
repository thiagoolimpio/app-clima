import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc
chave = '3c822c66381b52bd6ec6cd7a7cdf9c30'
cidade = 'Machado'
api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,chave)


# chamando a API com o requests
r = requests.get(api_link)

# convertendo a reposta em JSON
dados = r.json()
print(dados)
print('*'*45)

# obtendo dados pela API
país_codigo = dados['sys']['country']
print(país_codigo)

#zona
zona_fuso = pytz.country_timezones[país_codigo]

#---------país
país = pytz.country_names[país_codigo]
#---------data----------
zona = pytz.timezone(zona_fuso[0])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime('%d %m %Y | %H:%M:%S %p')

#---------tempo
tempo = dados['main']['temp']
pressao = dados['main']['pressure']
humidade= dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']


#mudando informacoes
def pais_para_continente(i):
    pais_alpha = pc.country_name_to_country_alpha2(i)
    pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
    pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
    
    return pais_continente_nome

continente = pais_para_continente(país)