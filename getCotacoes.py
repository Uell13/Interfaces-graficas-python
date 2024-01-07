import requests
from tkinter import *
# importando o tkinter, a biblioteca que ajuda a criar as janelas

# Esse código peguei na internet, não faço ideia de como funciona
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    # Esse código é para atribuir o valor a variável, quando o usuário interagir com o botão
    texto_valores_cotacoes["text"] = texto

# Criando a janela principal, editando o titulo e o tamanho que a janela vai ser aberta
janela_principal = Tk()
janela_principal.title("Cotações ataulizadas das moedas")
janela_principal.geometry("400x200")

# Adicionando textos a janela, definindo a variável e usando o parametro LABEL que gerencia os textos
# O parametro GRID, serve para definir onde a informação vai pararecer na janela, passando a coluna e a linha
texto_orientacao_1 = Label(janela_principal, text="Para ver a cotação das moedas atualizadas")
texto_orientacao_1.grid(column=0, row=0,)

texto_orientacao_2 = Label(janela_principal, text="Clique no botão abaixo!")
texto_orientacao_2.grid(column=0, row=1,)

# Adicionando um botão a janela, aqui usei para mandar um comando ao código para pegar as informações das cotações atualizadas
botao_atualizar = Button(janela_principal, text="BUSCAR", command=pegar_cotacoes)
botao_atualizar.grid(column=0, row=2)

# Nesse LABEL'text', vai aparecer os valores atualizados depois que o usuário interagir com o botão
texto_valores_cotacoes = Label(janela_principal, text="")
texto_valores_cotacoes.grid(column=0, row=3)

# Esse mainloop serve para informar onde termina o código da janela e evitar que ela feche ate o usuário decidir fecha-la
janela_principal.mainloop()