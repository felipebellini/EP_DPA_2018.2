varias_comandas = dict()
cardapio = {'banana': '3.50'}
e = 1
controle1 = [0, 1, 2, 3, 4]
controle2 = [0, 1, 2, 3, 4, 5, 6]
choice = int(input("Faça sua escolha:  "))
#
while choice != 0:
    lista1 = []
    for a in lista1:
        print(a)

    escolhas_comandas = int(input("Escolha uma opção acima:"))
    if escolhas_comandas not in controle1:
        print("Comando inválido.")

    elif escolhas_comandas == 0:
        print("Até mais")

    elif escolhas_comandas == 1:
        nome_comanda = input("Escreva o nome da comanda:")

        if nome_comanda not in varias_comandas:
            print("Comanda inválida")
        while e != 0:
            print(nome_comanda)
            lista2 = ["Comanda eletrônica", "0 - sair", "1 - imprimir cardápio",
                      "2 - adicionar item", "3 - remover item", "4 - imprimir comandas"]
            for b in lista2:
                print(b)
            controle_de_comandas = int(input("Faça sua escolha:"))
            if controle_de_comandas not in controle2:
                print("Comando inválido.")

            elif controle_de_comandas == 0:
                print("Até mais")

            elif controle_de_comandas == 1:
                print("O cardápio possui os seguintes itens:")
                for b in cardapio:
                    print("-{0} (R$ {1})".format(b, preco_unitario))

            elif controle_de_comandas == 2:
                produto = input("Nome do produto:")
                if produto not in cardapio:
                    cardapio[produto] = {}
                    quantidade_a_adicionar = int(input("Quantidade a adicionar:"))
                    while quantidade_a_adicionar < 0:
                        quantidade_a_adicionar = int(
                            input("Não é possível adicionar quantidade não positiva"))
                    # BUGADO!!! ele aparece o mesmo valor para todos os itens no cardapio
                    cardapio[produto]['Quantidade'] = quantidade_a_adicionar
                    valor = float(input("Preço unitário:"))
                    while valor < 0:
                        valor = float(
                            input("O preço não pode ser negativo. Digite novamente:"))
                    while valor == 0:
                        valor = float(
                            input("O preço não pode ser igual a zero. Digite novamente:"))
                    cardapio[produto]['Valor'] = valor
                    print("Produto cadastrado com sucesso.")
                else:
                    print("Produto já está cadastrado.")

            elif controle_de_comandas == 3:
                # BUGADO!!!
                # Falta perguntar a quantidade a remover
                produto = input("Nome do produto:")
                if produto in cardapio:
                    del((cardapio[produto]))
                    print("Produto removido com sucesso.")
                else:
                    print("Elemento não encontrado.")

            elif controle_de_comandas == 4:
                for c in cardapio[escolhas_comandas]['Quantidade']:
                    print("{0}:{1}".format(c, cardapio[escolhas_comandas][c]))
print("Até mais!")