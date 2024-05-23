# Ana Laura Torres Loureiro - RM554375
#Geronimo Augusto Nascimento Santos - RM 557170
#pyqt 5
# kivy
def cadatro():
    nome=input('Digite seu nome: ')
    email=input('Digite seu email: ')
    print(f'Digite o CPF sem pontução')
    cpf=int(input('Digite seu CPF: '))
    data=input('Digite a data do seu aniversário: ')
    street=input('Digite o nome da sua rua: ')
    n=int(input('Digite o número da sua casa: '))
    c=input('Digite o complemento caso possua: ')
    if c=='':
        pass

def menu():
    print("""
        VINHOS TINTOS      
          Cabernet Sauvignon-R$100 
          Pinot Noir–R$115
          Tinto Malbec–R$80
          Tinto Merlot–R$95
     ----------------------------
        VINHOS BRANCOS
          Chardonnay–R$80
          Sauvignon Blanc–R$70
          Riesling–R$90
          Pinot Grigio–R$60       
     -----------------------------     
        VINHOS ROSÉ
          Cabernet Franc–R$70
          Syrah–R$80
          Grenache–R$60
    """)

def adiciona_carrinho(vinhos, tipo):
    if tipo == "Rosé":

        print(f'Você selecionou a categoria Vinho {tipo}')
        print(f"""\nEscolha o vinho que deseja
        1-{vinhos[0]} 
        2-{vinhos[1]}
        3-{vinhos[2]}\n""")
        vinho = input()

        while not vinho.isnumeric() and int(vinho) not in [1,2,3]:
            print(f"""\nEscolha o vinho que deseja    
        1-{vinhos[0]} 
        2-{vinhos[1]}
        3-{vinhos[2]}\n""")
            vinho = input()
    else:
        print(f'Você selecionou a categoria Vinho {tipo}')
        print(f"""\nEscolha o vinho que deseja
        1-{vinhos[0]} 
        2-{vinhos[1]}
        3-{vinhos[2]}
        4-{vinhos[3]}\n""")
        vinho = input() 

        while not vinho.isnumeric() and int(vinho) not in [1,2,3]:
            print(f"""\nEscolha o vinho que deseja    
        1-{vinhos[0]} 
        2-{vinhos[1]}
        3-{vinhos[2]}
        4-{vinhos[3]}\n""")
            vinho = input()

    return vinhos[int(vinho)-1]

def carrinho():
    tinto=[]
    branco=[]
    rose=[]
    tintos_tipos =["Cabernet Sauvignon: R$100","Pinot Noir: R$115","Tinto Malbec: R$80","Tinto Malbec: R$80"]
    brancos_tipos =["Chardonnay: R$80","Sauvignon Blanc: R$70","Riesling: R$90","Pinot Grigio: R$60"]
    roses_tipos =["Cabernet Franc: R$70","Syrah: R$80","Grenache: R$60"]
    
    while True:
        print("""\nEscolha a categoria do vinho que deseja
        1-VINHO TINTO
        2-VINHO BRANCO
        3-VINHO ROSÉ\n""")
        
        tipo=int(input())
        match tipo:
            case 1:
                tinto.append(adiciona_carrinho(tintos_tipos, 'Tinto'))

            case 2:
                branco.append(adiciona_carrinho(brancos_tipos, 'Branco'))
                
            case 3:
                rose.append(adiciona_carrinho(roses_tipos, 'Rosé'))
            
            case _:
                print("Opção inválida")
                
        r=int(input("\nDeseja adicionar mais?\n1-Sim\n2-Não\n"))
        
        if r==2:
            break
       

    return [tinto, branco, rose]

def separ_lista(itens_unicos):
    # Inicializa uma lista para armazenar os pares de nome e valor
    # vinhos_pares=[]
    # for tipo_vinho in vinhos_carrinho:
    #     if len(tipo_vinho) == 0:
    #         vinhos_pares.append(["Nenhum"])
            
    #     else:
    #         # Itera sobre cada item na lista
    vinhos = []
    preco= []
    for item in itens_unicos:
        # Divide a string no caractere ': R$'
        nome, valor = item.split(": R$")
        # Adiciona o par (nome, valor) à lista, convertendo o valor para inteiro
        vinhos.append(nome)
        preco.append(int(valor))
                
            # vinhos_pares.append(vinhos)
            
    return vinhos, preco
      
def repetidos(vinhos):

    itens_unicos = []
    contagens = []
    for tipo in vinhos:
        if len(tipo) == 0:
            continue
        # Itera sobre cada item na lista
        for compra in tipo:
            # Se o item já está na lista de itens únicos, incrementa a contagem correspondente
            if compra in itens_unicos:
                index = itens_unicos.index(compra)
                contagens[index] += 1
            else:
                # Se o item não está na lista de itens únicos, adiciona-o e inicializa sua contagem
                itens_unicos.append(compra)
                contagens.append(1)

    # Filtra apenas os itens que se repetem
    # itens_repetidos = [compra for compra, contagem in zip(itens_unicos, contagens) if contagem > 1]
    # contagens_repetidos = [contagem for contagem in contagens if contagem > 1]
    
    return itens_unicos, contagens


def valor_final(vinhos):
    itens_unicos, contagens =repetidos(vinhos)
    vinhos, preco = separ_lista(itens_unicos)
    for item, contagem in zip(itens_unicos, contagens):
        print(f"{item}: quantidade comprada {contagem}")

    precos = [contagem * valor for contagem, valor in zip(contagens, preco)]
    
    if 2 <= sum(contagens) <3:
        preco_final =sum(precos)*0.95
    elif 3 <= sum(contagens)<4:
        preco_final =sum(precos)*0.90
    elif 4 <= sum(contagens):
        preco_final = sum(precos)*0.8
    print(preco_final)        


def main():
    vinhos = carrinho()
    

    # menu()
    # carrinho()
    valor_final(vinhos)
    
main()
