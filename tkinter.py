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
    date = datetime.strptime(data, '%d/%m/%Y').date()
    venda_compra = str(input("DIGITE 'V' PARA VENDAS E 'C' PARA COMPRAS ").upper())
    registrados = (nome, quantidade, data, venda_compra)
    ch = guardar_registros(registros, codigo, registrados)
    print(registros)

if __name__=='__main__':
  main()

#INTERFACE COM TKINTER

janela = tkinter.Tk()



janela.mainloop()