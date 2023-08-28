dicio = {'primeiro':1, 'segundo':2,'terceiro':3}
print(type(dicio))
print(dicio)

print("")


dicio_2 = dict(primeiro=1, segundo=2, terceiro=3)
print(type(dicio_2))
print(dicio_2)

print("")

dicio_3 = dict(zip(['primeiro','segundo','terceiro'],[1,2,3]))
print(type(dicio_3))
print(dicio_3)

print("")


dicio_4 = dict([('primeiro',1),('segundo',2),('terceiro',3)])
print(type(dicio_4))
print(dicio_4)


print("")


dicio_5 = {name: idx + 1 for idx, name in enumerate(('primeiro','segundo','terceiro'))}
print(type(dicio_5))
print(dicio_5)


print("")


dicio_6 = dict({'primeiro':1, 'segundo':2, 'terceiro':3})
print(type(dicio_6))
print(dicio_6)


print("")

pessoa = {'nome': 'Pythonico', 'altura': 1.65, 'idade': 23}
print(pessoa['nome'])

print(pessoa.get('nome'))

print(pessoa.get('peso','Chave não encontrada'))

print("")

computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250bg'}
print(computador.keys())

print("")

computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250bg'}
for chave in computador.keys():
    print(f'chave = {chave} e valor = {computador[chave]}')
    
    
print("")

"""
notas_value = {'Mat':8 , 'Port': 4, 'Hist': 6}
for valor in notas_value():
    print(f'Valor: [valor]')
"""

print("")


frutas = {'pera': 10, 'uva':2 , 'maça':55}
print(frutas.items())



print("")

dicio_cores = {'amarelo':10, 'vermelho':2, 'cinza':29}

if 'amarelo' in dicio_cores:
    print(f"Como a cor desejada existe: {dicio_cores['amarelo']}")
    
if 10 in dicio_cores.values():
    print('O valor desejado existe')


print("")


dicio = {'nome': 'David'}
dicio['idade'] = 20
dicio['altura'] = 1.80
print(dicio)

print("")


dicio = {'nome' : 'David'}

dicio.update({'nome':'Fabio'})

dicio.update({'idade': 60})
dicio.update(tamanho = 1.85)
print(dicio)

print("")


pessoa = {'nome': 'Fabio', 'idade': 60, 'tamanho': 1.85}

del pessoa['tamanho']
print(pessoa)

print("")


sacola = {'maça': 10, 'ovos': 6, 'farinha': 2}
ovos = sacola.pop('ovos')

print(ovos)
print(sacola)

print("")


sacola = {'maça': 2, 'ovos': 6, 'farinha':2}

farinha = sacola.popitem()

print(farinha)
print(sacola)


print("")


dicio = {'nome': 'F9', 'motor': 'v8', 'ano':2015}
dicio.clear()

print(dicio)


print("")


dicio = {'operação': 'web scraping', 'dados':250}

copia = dicio.copy()

print(copia)
print(dicio)


print("")


dicio = {'coleta':'scrapy', 'dados':200}

set_dados = dicio.setdefault('dados')

print(set_dados)
print(dicio)


print("")


dicio = {'coleta': 'scrapy','dados':200}
set_data = dicio.setdefault('data')
set_teste = dicio.setdefault('teste',1)

print(set_data)
print(set_teste)
print(dicio)


print("")


chaves = ['chave1', 'chave2' , 'chave3']
valor = 0

dicio = dicio.fromkeys(chaves, valor)
print(dicio)


print("")


#Ex 31 - crie um dicionario vazio e imprima-o

dicio = {}
print(dicio)

print("")

#Ex 32 - Crie um dicionario com tres pares chave-valor representando nomes de 
#frutas e suas quantidades, imprima o dicionario

frutas = {'maça': 5, 'banana': 6, 'laranja':7}
print(frutas)


#Ex 33 - Adicione uma nova fruta ao dicionario do exercicio com sua respectiva
# quantidade, imprima o dicionario atualzado
frutas['uvas'] = 9
print(frutas)

print("")

#Ex 34 - Dado um dicionario de notas de notas dos alunos, calcule a medias 
#das notas e imprima o resultado

notas = {'David': 7, 'Vh': 8, 'Edu':6}
media = sum(notas.values())/len(notas)
print(f"A média das notas é: {media:.2f}")




#Ex 35 - Crie um dicionario de palavras e suas traduções em outro idioma. 
#Peça ao usuário para digitar uam palavra e retornar


traducao = {'Ola': 'Hello', 'Tchau': 'Bye', 'Cão': 'Dog'}
palavra = input("Digite uma palavra em portugues para ver a traducao em ingles: ")
traducao = traducao.get(palavra, 'Tradução não encontrada!')
print(traducao)

print("")


#Ex 36 - Crie um dicionario com nomes de cidades como keys e suas 
#populações como valores. Peça ao usuario para digitar uma cidade e mostra a 
#populaçao correspondente

cidades = {'New York': 86230000, 'Los Angeles': 3990000, 'Chicago': 2716000}
cidade = input("Digite o nome da cidade: ")
populacao = cidades.get(cidade, "Cidade não encontrada!")
print(f"A população de {cidade} é {populacao}")

print("")


#Ex 37 - Crie um dicionario com nomes de produtos e seus preços. Calcule o valor 
#total de uma lista de compras fornecida pelo usuário

produtos = {'maça': 1.25, 'banana': 0.75, 'laranja': 0.90}
shopping_list = input('Digite os produtos da lista (separados por virgula): ').split(', ')
total_cost = sum(produtos[item] for item in shopping_list if item in produtos)
print(f"O custo total é: R${total_cost:.2f}")

print("")

#Ex 38 - Crie um programa que simule um dicionario de conteudo. 
#Permita ao usuario adicionar, remover e buscar contatos pelo nome.
contatos = {}
while True:
    print('1. Adicionar contato')
    print('2. Remover contato')
    print('3. Buscar contato')
    print('4. Sair')
    choice = int(input("Escolha uma opção: "))
    
    print("")

    
    if choice ==1:
        nome = input("Digite o nome do contato: ")
        numero = input("Digite o numero de contato: ")
        contatos[nome] = numero
        print("")
    elif choice == 2: 
        nome = input('Digite o nome do contato a ser removido: ')
        print("")
        if nome in contatos:
            del contatos[nome]
            print(f'Contato {nome} removido.')
            print("")
        else: 
            print('Contato não encontrado')
            print("")
    elif choice == 3:
        nome = input("Digite o nome do contato a ser buscado: ")
        numero = contatos.get(nome, "Contato não encontrado")
        print(f'Número de {nome}: {numero}')
        print("")
    elif choice == 4:
        break

print("")

#39 - Crie um dicionario conteudo nomes de paises e suas capitais. Peça ao usuario
#para adivinhar a capital de um pais escolhido aleatoriamente

import random

paises = {'Brasil': 'Brasília', 'EUA': 'Washington', 'França':'Paris'}
pais = random.choice(list(paises.keys()))
guess = input(f'Qual é a capital de {pais}?')
if guess == paises[pais]:
    print("Resposta correta!")
else:
    print(f'A resposta incorreta. A capital de {pais} é {paises[pais]}')
    
print("")


#Ex 40 - Crie um dicionario com palavras-chave e suas definicoes. Desafie o 
#usuario a adivinhar uma definicao a partir de uma palavra

import random

definicoes = {'python': 'Linguagem de programação de alto nível', 'database':'Conjunto organizacional'}
palavra_chave = random.choice(list(definicoes.keys()))
definicao = input(f"Qual é a definição de'{palavra_chave}'? ")
if definicao == definicoes[palavra_chave]:
    print("Resposta correta!")
else:
    print(f"A resposta está incorreta. A definição de '{palavra_chave}' é '{definicoes{palavra_chave}}'.")


#Ex 41 - Crie um programa de cadastro de funcionarios utilizando dicionarios para
#armazenar informações como nome, cargo e salário.

empregados = {}
while True:
    print('1. Cadastrar funcionário')
    print('2. Listar funcionarios')
    print('3. Sair')
    choice = int(input('Escolha uma opção: '))
    
if choice ==1:
    empregado = {}
    empregado['nome'] = input('Nome: ')
    empregado['cargo'] = input('Cargo: ')
    empregado['salario'] = float(input('Salário: '))
    empregados.append(empregado)
    print("Funcionário cadastrado!")
elif choice ==2:
    for empregado in empregados:
        print(f"Nome: {empregado:{'nome'}} , Cargo: {empregados{'cargo'}}, Salário: {empregados{'salario'}}")
elif choice == 3:
    break



print(" ")

#Ex 42 - Crie um dicionario com nome de filmes e seus anos de lançamento.
#Peça ao usuario para digitar um ano e exiba os filmes lançados naquele ano.

filmes = {}


"""
Ex 51 - Grenciamento de estoque
Enunciado- Você é responsavel por desenvolver um sistema de gerenciamento de estoque 
"""


