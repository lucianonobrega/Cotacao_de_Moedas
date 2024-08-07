from tkinter import *
from time import time, sleep
from datetime import datetime
import requests


def info_me():
    label_nota["text"] = " Nota: Cotação atualiza a cada 30 segundos. "
    label_nota["bg"] = "white"

def refresh_me():
    pegar_cotacao()
    log = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print('[INFO]Atualizado em : '+ log )
    label_nota.after(1000, info_me)
    label_nota["text"] = " Atualizado em | "+ log
    label_nota["bg"] = "#90EE90"
    label_nota["width"] = 33

#Funções
def pegar_cotacao():
    response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    data = response.json()

    titles = ["Dólar -> Real: R$ ", "Euro -> Real: R$ ", "Bitcoin -> Real: R$ "]
    USDBRL = data["USDBRL"]["bid"]; EURBRL = data["EURBRL"]["bid"]; BTCBRL = data["BTCBRL"]["bid"]
    label["text"] = f"{titles[0]}{USDBRL}\n{titles[1]}{EURBRL}\n{titles[2]}{BTCBRL}"
    label.after(30000, refresh_me)

#Configurações
app = Tk()
app.title("Cotação de Moedas")
largura = 300
altura = 300
monitor_largura = app.winfo_screenwidth()
monitor_altura = app.winfo_screenheight()
posx = monitor_largura // 2 - largura // 2
posy = monitor_altura // 2 - altura // 2
app.geometry(f"{largura}x{altura}+{posx}+{posy}") #Centraliza a janela na tela
app.resizable(False, False)

#Widgets
frame = Frame(app, bg="#333333")
label = Label(app, width=31, height=7, text="Clique no botão 'Pegar Cotação'!", font=("Segoe", 10))
botao = Button(app, text="Pegar Cotação",command=pegar_cotacao)
label_nota = Label(app, text=" Nota: Cotação atualiza a cada 30 segundos. ")

#Posicionamento dos Widgets
frame.place(relwidth=1, relheight=1)
label.place(relx=0.080, rely=0.1)
botao.place(relx=0.36, rely=0.6)
label_nota.place(relx=0.111, rely=0.8)

#Looping
app.mainloop()