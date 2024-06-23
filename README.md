
# Sistema de Cadastro e Carrinho de Vinhos
## Descrição
Este projeto implementa um sistema de cadastro de usuários e um carrinho de compras para vinhos utilizando Python.
O sistema permite que os usuários se cadastrem, visualizem o menu de vinhos disponíveis e adicionem vinhos ao carrinho.
O preço final da compra é calculado com base na quantidade de vinhos comprados, aplicando descontos progressivos.

## Autores
- Ana Laura Torres Loureiro - RM554375
- Geronimo Augusto Nascimento Santos - RM 557170
## Como Utilizar
### Cadastro de Usuário
A função `cadastro()` coleta informações do usuário como nome, e-mail, CPF, data de aniversário, endereço e número da casa.

```python
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
```
### Menu de Vinhos
A função `menu()` exibe o menu de vinhos disponíveis, divididos em vinhos tintos, brancos e rosé.

```python
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
```
### Adicionar ao Carrinho
A função `adiciona_carrinho(vinhos, tipo)` permite ao usuário selecionar vinhos de uma determinada categoria e adicioná-los ao carrinho.

```python
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
        while not vinho.isnumeric() and int(vinho) not in [1,2,3,4]:
            print(f"""\nEscolha o vinho que deseja    
        1-{vinhos[0]} 
        2-{vinhos[1]}
        3-{vinhos[2]}
        4-{vinhos[3]}\n""")
            vinho = input()
    return vinhos[int(vinho)-1]
```
### Carrinho de Compras
A função `carrinho()` gerencia a seleção de vinhos e a adição ao carrinho.

```python
def carrinho():
    tinto=[]
    branco=[]
    rose=[]
    tintos_tipos =["Cabernet Sauvignon: R$100","Pinot Noir: R$115","Tinto Malbec: R$80","Tinto Merlot: R$95"]
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
```
### Cálculo do Valor Final
As funções `repetidos(vinhos)`, `separ_lista(itens_unicos)` e `valor_final(vinhos)` calculam o valor final da compra, aplicando descontos progressivos baseados na quantidade de vinhos adquiridos.

```python
def separ_lista(itens_unicos):
    vinhos = []
    preco= []
    for item in itens_unicos:
        nome, valor = item.split(": R$")
        vinhos.append(nome)
        preco.append(int(valor))
    return vinhos, preco

def repetidos(vinhos):
    itens_unicos = []
    contagens = []
    for tipo in vinhos:
        if len(tipo) == 0:
            continue
        for compra in tipo:
            if compra in itens_unicos:
                index = itens_unicos.index(compra)
                contagens[index] += 1
            else:
                itens_unicos.append(compra)
                contagens.append(1)
    return itens_unicos, contagens

def valor_final(vinhos):
    itens_unicos, contagens = repetidos(vinhos)
    vinhos, preco = separ_lista(itens_unicos)
    for item, contagem in zip(itens_unicos, contagens):
        print(f"{item}: quantidade comprada {contagem}")
    precos = [contagem * valor for contagem, valor in zip(contagens, preco)]
    
    if 2 <= sum(contagens) < 3:
        preco_final = sum(precos) * 0.95
    elif 3 <= sum(contagens) < 4:
        preco_final = sum(precos) * 0.90
    elif 4 <= sum(contagens):
        preco_final = sum(precos) * 0.8
    print(preco_final)
```       
### Função Principal
A função `main()` executa o fluxo principal do programa.

```python
def main():
    vinhos = carrinho()
    valor_final(vinhos)
    
main()
```




