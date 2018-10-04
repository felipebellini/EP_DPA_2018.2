import json

with open("cardapio.json", "r") as arquivo:
    cardapio = json.loads(arquivo.read())


with open("comandas.json", "r") as arquivo:
    comandas = json.loads(arquivo.read())



print("""
0 - Sair
1 - Alterar cardápio
2 - Alterar comanda

""")

escolha = int(input("O que deseja alterar?:  "))

# Alterar cardápio
while escolha == 1:
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
        escolha = None

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
            if preco < 0:
                print("Preço não pode ser negativo!")
                preco = float(input("Digite o preço:  "))
            cardapio[item] = preco
            # Printando o cardápio após alteração
            print("")
            print("O cardápio possui os seguintes itens: ")
            print("")
            for c in cardapio:
                print("{0}" "(R$" "{1:.2f}" ")".format(c, float(cardapio[c])))
                print("")
        
        elif item in cardapio:
            print("")
            print("Item já está no cardapio!")
            

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
            if novo_valor < 0:
                print("Preço não pode ser negativo!")
                preco = float(input("Digite o preço:  "))
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

with open ("cardapio.json","w") as arquivo:
    json.dump(cardapio, arquivo, sort_keys= True, indent=4)



###########################################################################################################



# Alterar comandas
while escolha == 2:
    
    print("""
    0 - Sair      
    1 - Adicionar comanda
    2 - Remover comanda
    3 - Editar comanda 
    4 - Imprimir comanda
    """)
    escolha_comandas = int(input("Faça sua escolha:  "))
    
    # Sair
    if escolha_comandas == 0:
        escolha = None
    
    # Adicionar comanda nova 
    elif escolha_comandas == 1:
        com = input("Digite o nome da comanda a ser adicionada:  ")
        if com not in comandas:
            comandas[com] = {}
            
            print("Comanda adicionada com sucesso!")
        
        elif com in comandas:
            print("{0} já está no sistema!".format(com))
        
    # Remover comanda
    elif escolha_comandas == 2:
        com = input("Digite o nome da comanda a ser removida:  ")
        if com not in comandas:
            print("Comanda não está no sistema!")
        
        elif com in comandas:
            del comandas[com]
            print("Comanda removida com sucesso!")
                
    # Editar comanda 
    elif escolha_comandas == 3:
        com = input("Digite o nome da comanda a ser editada:  ")
        if com not in comandas:
            print("Comanda não está no sistema!")
            escolha_comandas = None
        
        elif com in comandas:
            comanda = com
            escolha_comandas = 3
                    
    # Imprimir comanda
    elif escolha_comandas == 4:  
        com = input("Digite o nome da comanda a ser impressa:  ")
        if com not in comandas:
            print("Comanda não está no sistema!")
         
        elif com in comandas:
            comanda = com
            print("Imprimindo {0}...".format(com))
            choice = 4
            
                            
            
            
                 
    while escolha_comandas == 3:
        print("""
        0 - Sair
        1 - Imprimir cardápio
        2 - Adicionar item
        3 - Remover item
        4 - Imprimir comanda
        """)
    
        choice = int(input("Faça sua escolha:  "))
        
        if choice == 0:
            escolha = 0
        
        
        
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
    
                if produto in comandas[comanda]:
                    comandas[comanda][produto][0] += quantidade
                    print("Quantidade atual de {0}: {1}".format(produto, comandas[comanda][produto]))
    
                elif produto not in comandas[comanda]:
                    comandas[comanda][produto] = [quantidade, cardapio[produto]]
                    print("Quantidade atual de {0}: {1}".format(produto, comandas[comanda][produto][0]))
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
                if quantidade > comandas[comanda][produto][0]:
                    print("Não é possível remover mais do que a quantidade presente na comanda")
                    print("Máximo a ser removido: {0}".format(comandas[comanda][produto]))
                    quantidade = int(input("Digite a quantidade a remover:  "))
                
                if quantidade <= comandas[comanda][produto][0]:
                    comandas[comanda][produto][0] -= quantidade
                    print("Quantidade atual de {0}: {1}".format(produto, comandas[comanda][produto][0]))
            if comandas[comanda][produto][0] == 0:
                print("Removendo {0} da comanda...".format(produto))
                del comanda[produto]
    
        # Imprimir comanda
        elif choice == 4:
            total = 0
            for c in comandas[comanda]:
                print("")
                print("Nome do produto: {0}".format(c))
                print("")
                print("Quantidade inicial: {0}".format(comandas[comanda][c][0]))
                print("")
                print("Preço unitário: R${0:.2f}".format(cardapio[c]))
                print("")
                total += cardapio[c]*comandas[comanda][c][0]
            print("Total: R${0:.2f}".format(total))
            print("")
            print("Total (c/ 10%):{0:.2f}".format(total*1.1))
                
     

print("")    
print("Até mais!")
    
with open ("comandas.json","w") as arquivo:
    json.dump(comandas, arquivo, sort_keys= True, indent=4)              
  
