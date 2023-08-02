
def encontrar_chave(dicionario, valor_procurado):
    for chave, valor in dicionario.items():
        if valor == valor_procurado:
         return chave

month = int(input())

months_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

chave_encontrada = encontrar_chave(months_dict,month)

print(chave_encontrada)


