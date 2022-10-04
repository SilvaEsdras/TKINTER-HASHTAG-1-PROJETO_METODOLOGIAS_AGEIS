import tkinter

janela = tkinter.Tk()

janela.title('Bolsa de valores')

input_data = tkinter.Label(janela, text="DATA")
input_data.grid(column=0, row=0)

input_data = tkinter.Label(janela, text="CODIGO")
input_data.grid(column=0, row=1)

input_data = tkinter.Label(janela, text="QUANTIDADE")
input_data.grid(column=0, row=2)

input_data = tkinter.Label(janela, text="VALOR UNITÁRIO")
input_data.grid(column=0, row=3)

input_data = tkinter.Label(janela, text="TIPO OPERAÇÃO")
input_data.grid(column=0, row=4)

input_data = tkinter.Label(janela, text="VALOR OPERAÇÃO(SEM TAXAS)")
input_data.grid(column=0, row=5)

input_data = tkinter.Label(janela, text="CORRETAGEM")
input_data.grid(column=0, row=6)

input_data = tkinter.Label(janela, text="TAXA B3")
input_data.grid(column=0, row=7)

input_data = tkinter.Label(janela, text="VALOR DA OPERAÇÃO")
input_data.grid(column=0, row=8)


janela.mainloop()