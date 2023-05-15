import requests

from tkinter import *
def pegar_cotacoes():
    requisicao = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto =  f'''
    Dolar:{cotacao_dolar}
    Euro:{cotacao_euro}
    Btc: {cotacao_btc}'''
    texto_orientacao["text"] = texto

janela = Tk()
janela.title('cotacao atual das moedas')


texto_orientacao = Label(janela, text="Clique no botao para ver as cotacaoes da moedas")
texto_orientacao.grid(column= 0, row=0 , padx= 10, pady=10)

botao = Button(janela, text="Buscar cotacões Dolar/Euro/BTC", command=pegar_cotacoes)
botao.grid(column=0, row=1 , padx= 10, pady=10)

texto_orientacao = Label(janela, text="")
texto_orientacao.grid(column=0 , row=2, padx=10, pady=10)



janela.mainloop()

