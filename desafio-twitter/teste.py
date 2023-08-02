def encontrar_chave_por_valor(dicionario, valor_procurado):
    for chave, valor in dicionario.items():
        if valor == valor_procurado:
            return chave
    return None  # Retorna None caso o valor não seja encontrado

# Exemplo de uso:
meu_dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 2}

# Solicita ao usuário que digite o valor a ser procurado
valor_digitado = int(input("Digite o valor que você deseja buscar no dicionário: "))

# Chama a função para encontrar a chave correspondente ao valor digitado
chave_encontrada = encontrar_chave_por_valor(meu_dicionario, valor_digitado)

# Verifica se a chave foi encontrada e exibe o resultado
if chave_encontrada is not None:
    print("Chave encontrada:", chave_encontrada)
else:
    print("Valor não encontrado no dicionário.")