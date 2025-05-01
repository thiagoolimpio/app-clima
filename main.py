from tkinter import *
from tkinter import ttk

################# cor ################
cor1 ='#444466' # preto
cor2 ='#feffff' # branco
cor3 ='#6f9fbd' # azul

bck_dia = '#6cc4cc'
bck_noite = '#484f60'
bck_tarde = '#bfb86d'

fundo = bck_dia
 

janela = Tk()
janela.title('XsWeather')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

janela.mainloop()