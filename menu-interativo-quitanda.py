#Escreva um script em python que represente uma quitanda. O seu programa deverá
#apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
#deverá ser adicionada a uma cesta de compras:

#Menu principal:
#1 Quitanda:
#2 1: Ver cesta
#3 2: Adicionar frutas
#4 3: Sair
#5
#6 Digite a opção desejada:

#1 Menu de frutas:
#2
#3 Escolha fruta desejada:
#4 1 - Maça
#5 2 - Uva
#6 3 - Kiwi
#7
#8 Digite à opção desejada: 2
#9 Uva adicionada com sucesso!
#Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.
#Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem
#Digite uma opção inválida)

# Incremente a sua quitanda para consolidar o valor
# total de sua cesta de compras. Deverá ser adicionado ao seu menu inicial a opção
# checkout e esta deverá listar os produtos de sua cesta bem como o valor total:
# 1 Menu:
# 2 1: Ver cesta
# 3 2: Adicionar Frutas
# 4 3: Checkout
# 5 4: Sair
# 6
# 7 Digite a opção desejada:
# A saída do checkout deverá ser da seguinte maneira:
# 1 Total de compras: 15,00
# 2 Cesta de compras: Maça, Uva, Kiwi
# Considere os seguintes preços:
# Maça: 2.50 Uva: 6.50 Kiwi: 10.00
# Dica: Você pode armazenar os dados de frutas e seus respectivos preços em um dicionário

# Primeiro passo, criação da lista que vai percorrer os menus interativos:
cesta = []

#Segundo passo, criação do dicionário da lista de frutas:
frutas = {
    '1':'Maça',
    '2':'Uva',
    '3':'Kiwi'
}

#Terceiro passo, criação do dicionário do preço da lista de frutas:
precos = {
    'Maça':2.50,
    'Uva':6.50,
    'Kiwi':10.00
}


#Quarto passo, criação da primeira parte do menu interativo
while True:

# A primeira parte do menu irá retornar tudo que foi acumulado até então na lista criada como cesta, 
#no começo ele retorna a cesta vazia.
  op = input('Quitanda: \n1:Ver cesta\n2:Adicionar frutas\n3:Checkout\n4:Sair\nDigite a opção desejada:')
  if op == '1':
    print('Cesta de compras')
    for items in cesta:
      print(items)
      print('-'*15)

#o segundo menu, é a apresentação da cesta de frutas
  elif op == '2':
    fruta = input(f'Escolha a fruta desejada:\n' \
                      f'1 - Maça\n' \
                      f'2 - Uva\n' \
                      f'3 - Kiwi\n' \
                      f'Digite a opção desejada: ')
    #o if irá percorrer dentro do dicionário frutas pelo código digitado,    
    if fruta in frutas:
        #o código irá adicionar o item a lista cesta.
      cesta.append(frutas[fruta])
      print(f'{frutas[fruta]} foi adicionado com sucesso')
      print('-'*15)
    # caso o código não esteja dentro da lista, irá apresentar opção inválida
    else:
      print('Opção inválida')
      print('-'*15)

#Para fazer o checkout, o código vai percorrer a lista cesta, e caso ela tenha algum item, irá buscar no dicionário precos
  elif op == '3':
        if len(cesta) > 0:
            total = 0
            #quando ele encontra o item na lista cesta, ele busca o valor no dicionário precos, somando o valor aplicado
            for item in cesta:
                total += precos[item]
            #saída com os dois acumulos, a lista cesta e o total acumulado
            print(f'Total de compras: {total}')
            print(f'Cesta de compras: {cesta}')
        else:
            #caso não tenha itens na cesta
            print('Cesta de compras vazia.')
            
#Menu para saída do Menu interativo
  elif op == '4':
    break
  else:
    print('Opção Inválida')