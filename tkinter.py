from datetime import datetime

def guardar_registros():
    registros = {}
    for c in range(3):
        codigo = int(input('DIGITE O CÓDIGO DO PRODUTO: '))
        nome = str(input('DIGITE O NOME DA OPERAÇÃO: '))
        quantidade = int(input('DIGITE A QUANTIDADE: '))
        data = input('DIGITE A DATA: ')
        date = datetime.strptime(data, '%d/%m/%Y').date()
        venda_compra = str(input("DIGITE 'V' PARA VENDAS E 'S' PARA COMPRAS "))
        registrados = (nome, quantidade, data, venda_compra)
        registros[codigo] = registrados
    return registros

ch = guardar_registros()
print(ch)



