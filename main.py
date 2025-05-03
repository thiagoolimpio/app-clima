from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc

################# cor ################
cor1 ='#444466' # preto
cor2 ='#feffff' # branco
cor3 ='#6f9fbd' # azul

bck_dia = '#6cc4cc'
bck_noite = '#484f60'
bck_tarde = '#bfb86d'

fundo = bck_dia

#--------------------janela principal-----------------#

janela = Tk()
janela.title('XsWeather')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, padx=157)

global imagem




# criando os frames
frame_top = Frame(janela, width=320, height=50, bg=cor2, pady=0, padx=0, )
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0, )
frame_corpo.grid(row=2, column=0, sticky=NW)

# estilizaçao
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando frame top:

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

l_cidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 14"))
l_cidade.place(x=10, y=4)

# configurando frame corpo: 

l_data = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_data.place(x=10, y=54)
l_humidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 45 bold"))
l_humidade.place(x=10, y=100)
l_h_simbolo = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10 bold"))
l_h_simbolo.place(x=85, y=110)
l_h_nome = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 8"))
l_h_nome.place(x=85, y=140)
l_pressao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_pressao.place(x=10, y=184)
l_velocidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_velocidade.place(x=10, y=212)

l_descricao = Label(frame_corpo, text='Nublado', anchor='center', bg=fundo, fg=cor1, font=("Arial 10"))
l_descricao.place(x=170, y=190)



def informacao():
    
    chave = '3c822c66381b52bd6ec6cd7a7cdf9c30'
    cidade = e_local.get()
    api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,chave)


    #--------chamando a API com o requests
    r = requests.get(api_link)

    #--------convertendo a reposta em JSON
    dados = r.json()
    print(dados)
    print('*'*45)

    #--------obtendo dados pela API
    pais_codigo = dados['sys']['country']
    print(pais_codigo)

    #---------zona
    zona_fuso = pytz.country_timezones[pais_codigo]

    #---------país
    pais = pytz.country_names[pais_codigo]
    #---------data
    zona = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime('%d %m %Y | %H:%M:%S %p')

    #---------tempo
    tempo = dados['main']['temp']
    pressao = dados['main']['pressure']
    humidade= dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']

    
    #---------mudando informacoes
    def pais_para_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
        
        return pais_continente_nome

    continente = pais_para_continente(pais)
    l_cidade['text'] = cidade + ' - ' + pais + ' / ' + continente
    l_data['text'] = zona_horas
    l_humidade['text'] = humidade
    l_h_simbolo['text'] = '%'
    l_h_nome['text'] = 'Humidade'
    l_pressao['text'] = "Pressão: " + str(pressao)
    l_velocidade['text'] = "Velocidade do Vento:" + str(velocidade)
    l_descricao['text'] = descricao

    #---icon
    zona_periodo = datetime.now(zona)
    zona_periodo =zona_periodo.strftime('%H')
    
    global imagem
    zona_periodo = int(zona_periodo)
    
    if zona_periodo <= 5:
        imagem =  Image.open('imagens/noite.png')
        
    elif zona_periodo <= 11:
        imagem =  Image.open('imagens/sol.png')
    else:
        pass
        
        
        
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_icon = Label(frame_corpo, image=imagem, bg=fundo, font=("Arial 10"))
    l_icon.place(x=162, y=50)
    
    
    
    
#-------------botão
b_ver = Button(frame_top, command=informacao, text='clima', bg=cor1, fg=cor3, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE,)
b_ver.place(x=250, y=10)

janela.mainloop()