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
        venda_compra = str(input("DIGITE 'V' PARA VENDAS E 'C' PARA COMPRAS ").upper())
        corretagem = str(input('CORRETAGEM'))
        taxa_b3 = str(input('TAXA B3'))
        valor_operacao = float(input())
        registrados = (nome, quantidade, data, venda_compra,taxa_b3, valor_operacao)
        ch = guardar_registros(registros, codigo, registrados)
        print(ch)
    

    