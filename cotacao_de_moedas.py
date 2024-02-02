#Importações------------------------------------------------------------------------------------------------------------
from tkinter import *
import requests

#Funções----------------------------------------------------------------------------------------------------------------
def pegar_cotacao():
    response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    data = response.json()

    dolar_real_dados = data["USDBRL"]
    dolar_real_valor = dolar_real_dados["bid"]

    euro_real_dados = data["EURBRL"]
    euro_real_valor = euro_real_dados["bid"]

    bitcoin_real_dados = data["BTCBRL"]
    bitcoin_real_valor = bitcoin_real_dados["bid"]

    label["text"] = f"Dólar -> Real: R$ {dolar_real_valor}\nEuro -> Real: R$ {euro_real_valor}\nBitcoin -> Real: R$ {bitcoin_real_valor}"

#Configurações----------------------------------------------------------------------------------------------------------
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

#Widgets----------------------------------------------------------------------------------------------------------------
frame = Frame(app, bg="#333333")
label = Label(app, width=35, height=7, text="")
botao = Button(app, text="Pegar cotação",command=pegar_cotacao)
label_nota = Label(app, text="Nota: Cotação atualiza a cada 30 segundos.")

#Posicionamento dos Widgets---------------------------------------------------------------------------------------------
frame.place(relwidth=1, relheight=1)
label.place(relx=0.080, rely=0.1)
botao.place(relx=0.36, rely=0.6)
label_nota.place(relx=0.111, rely=0.8)

#Looping----------------------------------------------------------------------------------------------------------------
app.mainloop()