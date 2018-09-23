#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:17:07 2018

@author: joseantonio
"""

lista_comandas = []
comanda = {}

cardapio = {'banana': '3.50', 'iphone':'10000'}

print("""
0 - Sair
1 - Imprimir cardápio 
2 - Adicionar item
3 - Remover item
4 - Imprimir comanda
""")



choice = int(input("Faça sua escolha:  "))


# Sair
if choice == 0:
    print("")
    print("Até mais!")

# Imprimir cardápio    
elif choice == 1:
    print("")
    print("O cardápio possui os seguintes itens: ")
    for c in cardapio: 
        print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))

# Adicionar item
elif choice == 2:
    print("")
    produto = input("Digite o nome do produto:  ")
    if produto in cardapio:
        quantidade = int(input("Digite a quantidade de produtos:  "))
        if quantidade < 0:
            print("Não é possivel adicionar quantidades negativas")
            quantidade = int(input("Digite a quantidade de produtos:  "))
            
        if produto in comanda: 
            comanda[produto] += quantidade
            print("Quantidade atual de {0}: {1}".format(produto, comanda[produto]))
            
        elif produto not in comanda:
            comanda[produto] = quantidade
            print("Quantidade atual de {0}: {1}".format(produto, comanda[produto]))
    elif produto not in cardapio:
        print("O item {0} não está no cardápio".format(produto))    

# Remover item
elif choice == 3:
    print("")
    produto = input("Digite o nome do produto:  ")
    quantidade = int(input("Digite a quantidade a remover:  "))
    
    if quantidade < 0:
        print("Não é possivel remover quantidades negativas")
        quantidade = int(input("Digite a quantidade a remover:  "))
        
    if produto in comanda: 
        if quantidade > comanda[produto]:
            print("Não é possível remover mais do que a quantidade presente na comanda")
            print("Máximo a ser removido: {0}".format(comanda[produto]))
            quantidade = int(input("Digite a quantidade a remover:  "))
        
        comanda[produto] -= quantidade
        print("Quantidade atual de {0}: {1}".format(produto, comanda[produto]))
        if comanda[produto] == 0:
            print("Removendo {0} da comanda...".format(produto))
            del comanda[produto]
            
# Imprimir comanda
elif choice == 4:
    for c in comanda:
        print("Nome do produto: {0}".format(c))
        print("Quantidade inicial: {0}".format(comanda[c]))
        print("")
        
            
            
            
    


    
    