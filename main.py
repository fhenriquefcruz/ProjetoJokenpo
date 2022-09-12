import tkinter as tk
from tkinter import LabelFrame, Button, Label, PhotoImage
import random

def pedra():
    jok(usuario='Pedra')

def papel():
    jok(usuario='Papel')

def tesoura():
    jok(usuario='Tesoura')

def jok (usuario):
    pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
    if usuario == pc:
        msg = f'''
            Você: {usuario}
            PC: {pc}
        
            Empatamos!
    '''

    elif (usuario == 'Pedra' and pc == 'Tesoura') \
            or (usuario == 'Papel' and pc == 'Pedra')\
            or (usuario == 'Tesoura' and pc == 'Papel'):
        msg = f'''
            Você: {usuario}
            PC: {pc}

            Você Ganhou!
            '''
    else:
        msg = f'''
            Você: {usuario}
            PC: {pc}

            Você Perdeu!
                    '''

    escolha.config(text=msg)


janela = tk.Tk()
frame = LabelFrame(janela, text='JOKENPÔ CONTRA O PC', padx=10,pady=10)
frame.pack()

iconpedra = PhotoImage(file='png/pedra.png')
iconpapel = PhotoImage(file='png/papel.png')
icotesoura = PhotoImage(file='png/tesoura.png')
Button(frame,text='Pedra', command=pedra, image=iconpedra).grid(column=0, row=1)
Button(frame,text='Papel', command=papel, image=iconpapel).grid(column=2, row=1)
Button(frame,text='Tesoura',command=tesoura, image=icotesoura).grid(column=4, row=1)

escolha = Label(frame, pady=20, padx=40, justify=tk.LEFT)
escolha.grid(column=1, row=2, columnspan=3)

janela.title ('Jokenpô')
janela.geometry("500x200+700+200")
janela.mainloop()
