#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:17:07 2018

@author: joseantonio
"""


import json

comanda = {}


with open("cardapio.json", "r") as arquivo:
    cardapio = json.loads(arquivo.read())

print("""
0 - Alterar cardápio
1 - Alterar comanda      
""")

escolha = int(input("O que deseja alterar?:  "))

# Alterar cardápio
if escolha == 0:
    print("""
0 - Sair
1 - Imprimir cardápio 
2 - Adicionar item
3 - Remover item
4 - Alterar item
    """)
    escolha_menu = int(input("Faça sua escolha:  "))
    
    # Sair
    if escolha_menu == 0:
        print("")
        print("Até mais!")

    # Imprimir cardápio        
    elif escolha_menu == 1:
        print("")
        print("O cardápio possui os seguintes itens: ")
        print("")
        for c in cardapio: 
            print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
            print("")
            
    # Adicionar item
    elif escolha_menu == 2:
        item = input("Digite o item a ser adicionado:  ")
        if item not in cardapio:
            preco = float(input("Digite o preço:  "))
            cardapio[item] = preco
            # Printando o cardápio após alteração
            print("")
            print("O cardápio possui os seguintes itens: ")
            print("")
            for c in cardapio: 
                print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
                print("")

    # Remover item
    elif escolha_menu == 3: 
        # Imprimindo o cardápio
        print("O cardápio possui os seguintes itens: ")
        print("")
        for c in cardapio: 
            print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
            print("")
        # Perguntando item a ser removido
        item = input("Digite o item a ser removido:  ")
        
        if item not in cardapio:
            print("Item não está no cardápio")
            print("")
            # Impirimindo o cardápio
            print("O cardápio possui os seguintes itens: ")
            print("")
            for c in cardapio: 
                print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
                print("")
            item = input("Digite o item a ser removido:  ")
            del cardapio[item]
            
        elif item in cardapio:
            del cardapio[item]
            print("O cardápio possui os seguintes itens: ")
            print("")
            for c in cardapio: 
                print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
                print("")
    # Alterar item            
    elif escolha_menu == 4:
        print("O cardápio possui os seguintes itens: ")
        print("")
        for c in cardapio: 
            print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
            print("")
        # Perguntando item a ser alterado
        item = input("Digite o item a ser alterado:  ")
        
        if item not in cardapio:
            print("Item não está no cardápio!")
            print("")
            # Impirimindo o cardápio
            print("Escolha apensa itens do cardápio: ")
            print("")
            for c in cardapio: 
                print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
                print("")
            item = input("Digite o item a ser alterado:  ")
            novo_valor = float(input("Digite o novo valor:  "))
            # Deletando o preço antigo
            del cardapio[item]
            # Adicionando o preço novo
            cardapio[item] = novo_valor
            # Imprimindo o cardápio alterado
            print("O novo cardápio possui os seguintes itens: ")
            print("")
            for c in cardapio: 
                print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
                print("")
        
        elif item in cardapio:
            novo_valor = float(input("Digite o novo valor:  "))
            # Deletando o preço antigo
            del cardapio[item]
            # Adicionando o preço novo
            cardapio[item] = novo_valor
            # Imprimindo o cardápio alterado
            print("O novo cardápio possui os seguintes itens: ")
            print("")
            for c in cardapio: 
                print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
                print("")
        
        with open ("cardapio.json","w") as fim:
            cardapio_final = json.dumps(cardapio, sort_keys= True, indent=4)
    
# Alterar comanda
if escolha == 1:

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
        print("")
        for c in cardapio: 
            print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
            print("")
    
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
            
                
                
            
    


    
    