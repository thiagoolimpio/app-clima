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

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, padx=157)

# criando os frames
frame_top = Frame(janela, width=320, height=50, bg=cor2, pady=0, padx=0, )
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0, )
frame_corpo.grid(row=2, column=0, sticky=NW)

# configurando frame top:

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)
b_ver = Button(frame_top, text='clima', bg=cor1, fg=cor3, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE,)
b_ver.place(x=250, y=10)

# configurando frame corpo: 

l_cidade = Label(frame_corpo, text='Machado - Brasil / America do Sul', anchor='center', bg=fundo, fg=cor1, font=("Arial 14"))
l_cidade.place(x=10, y=4)






# estilizaçao
estilo = ttk.Style(janela)
estilo.theme_use('clam')

janela.mainloop()