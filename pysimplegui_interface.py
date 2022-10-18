import tkinter

registros = {}
def guardar_registros(registros, codigo, tupla):
    for c in range(2):
        registros.update({codigo:tupla})


def main():
    for c in range(2):
        codigo = int(input('DIGITE O CÓDIGO DO PRODUTO: '))
        nome = str(input('DIGITE O NOME DA OPERAÇÃO: ').upper())
        quantidade = int(input('DIGITE A QUANTIDADE: '))
        data = input('DIGITE A DATA: ')
        venda_compra = str(input("DIGITE 'V' PARA VENDAS E 'C' PARA COMPRAS: ").upper())
        corretagem = str(input('CORRETAGEM: '))
        taxa_b3 = str(input('TAXA B3: '))
        valor_operacao = float(input('Valor da operação: '))
        registrados = (nome, quantidade, data, venda_compra,taxa_b3, valor_operacao)
        ch = guardar_registros(registros, codigo, registrados)
        print(registros)
    
if _name=='main_':
    main()


##TKINTER

janela = tkinter.Tk()

janela.title('Bolsa de valores')


input_data = tkinter.Label(janela, text="DATA")
input_data.grid(column=0, row=0, padx=10, pady=10)

data = tkinter.Entry(janela)
data.grid(column=0, row=1, padx = 10, pady = 10)
data_campo = data.get()

input_data = tkinter.Label(janela, text="CODIGO")
input_data.grid(column=0, row=1, padx=10, pady=10)

input_data = tkinter.Label(janela, text="QUANTIDADE")
input_data.grid(column=0, row=2, padx=10, pady=10)

input_data = tkinter.Label(janela, text="VALOR UNITÁRIO")
input_data.grid(column=0, row=3, padx=10, pady=10)

input_data = tkinter.Label(janela, text="TIPO OPERAÇÃO")
input_data.grid(column=0, row=4, padx=10, pady=10)

input_data = tkinter.Label(janela, text="VALOR OPERAÇÃO(SEM TAXAS)")
input_data.grid(column=0, row=5, padx=10, pady=10)

input_data = tkinter.Label(janela, text="CORRETAGEM")
input_data.grid(column=0, row=6, padx=10, pady=10)

input_data = tkinter.Label(janela, text="TAXA B3")
input_data.grid(column=0, row=7, padx=10, pady=10)

input_data = tkinter.Label(janela, text="VALOR DA OPERAÇÃO")
input_data.grid(column=0, row=8, padx=10, pady=10)

def historico():
    tela = tkinter.Tk()
    tela.title("Historico")

botao = tkinter.Button(janela, text="Ver histórico")
botao.grid(column=0, row=9, padx=10, pady=10)

janela.mainloop()
