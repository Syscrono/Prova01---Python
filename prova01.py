# Crie uma lista contendo seis frutas de sua escolha. Depois de ter a lista pronta, 
# converta essa lista em uma tupla. Por fim, exiba o conteúdo da tupla resultante 
# para verificar as frutas que foram armazenadas.

num_frutas = 6
frutas_lista = []

for i in range(num_frutas):
    fruta = input(f'Digite o nome na {i + 1}ª fruta: ')
    frutas_lista.append(fruta)

frutas_tupla = tuple(frutas_lista)

print(f"As frutas incluídas na tupla são: {frutas_tupla}")