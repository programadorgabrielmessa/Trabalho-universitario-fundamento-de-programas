"""
QUESTÃO 2 de 4 - Conteúdo até aula 04
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma sorveteria. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Sorveteria possui seguinte relação:

•	1bolade sorvete no sabor tradicional (tr) custa 6 reais, no sabor premium (pr) 7 reais e no especial (es)8 reais;
•	2bolas de sorvete no sabor tradicional (tr) custam11 reais, no sabor premium (pr) 13 reais e no especial (es) 15 reais;
•	3bolas de sorvete no sabor tradicional (tr)custam15 reais, no sabor premium (pr) 18 reais e no especial (es) 21 reais;

Elabore um programa em Python que: 

A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
B.	Deve-se entrar com o sabor (tr/pr/es) e onúmero de bolas de sorvete desejado (1/2/3)[EXIGÊNCIA DE CÓDIGO 1 de 6];
C.	Deve-se executar o print da mensagem de “Quantidade de Bolas de Sorvete Inválida". Se o usuário entrar com a quantidade de bolas de sorvete diferente de 1,2 e 3repetir a partir do item B[EXIGÊNCIA DE CÓDIGO 2 de 6];
D.	Deve-se executar o printda mensagem de“Sabor de Sorvete Inválido" se o usuário entrar com um sabor diferente de tr (tradicional), pr (premium) e es (especial). Printar: e repetir a partir do item B; [EXIGÊNCIA DE CÓDIGO 3 de 6];
E.	Deve-se perguntar se o cliente quer pedir mais alguma coisa. Sesim repetir a partir do item B, senão encerrar o programa printando o valor total[EXIGÊNCIA DE CÓDIGO 4 de 6];
F.	Deve-se utilizar as estruturas de while, break, continue (todas elas)[EXIGÊNCIA DE CÓDIGO5 de 6];
G.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
H.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o sabor do sorvete[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
I.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o número de bolas de sorvete[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];
J.	Deve-se colocar na apresentação de saída de console um pedido com duas opções sabores diferentes com quantidade de bolas diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];

"""
nome = 'Gabriel Rodrigues de Almeida Messa'
print(f"Bem-vindo ao aplicativo de vendas da sorveteria do {nome}!")

tabela_valores = """
Opções:

+------------------------+----------Cardápio--------+----------------+-------------+
| Número de Bolas        | Sabor Tradicional | Sabor Premium  |    Sabor Especial  |
+------------------------+----------------+----------------+----------------+------+
| 1                      | R$ 6.00         | R$ 7.00         |    R$ 8.00          |
| 2                      | R$ 10.00        | R$ 12.00        |    R$ 14.00         |
| 3                      | R$ 14.00        | R$ 17.00        |    R$ 20.00         |
+------------------------+----------------+----------------+----------------+------+
"""

print(tabela_valores)

total_pedido = 0

while True:
    sabor = input("Digite o sabor do sorvete (tr/pr/es): ")
    quantidade = input("Digite a quantidade de bolas de sorvete (1/2/3): ")

    if quantidade not in ["1", "2", "3"]:
        print("Opção de quantidade inválida")
        continue

    if sabor not in ["tr", "pr", "es"]:
        print("Opção de sabor inválida")
        continue

    quantidade = int(quantidade)

    if quantidade == 1:
        if sabor == "tr":
            preco = 6
        elif sabor == "pr":
            preco = 7
        else:
            preco = 8
    elif quantidade == 2:
        if sabor == "tr":
            preco = 10
        elif sabor == "pr":
            preco = 12
        else:
            preco = 14
    else:
        if sabor == "tr":
            preco = 14
        elif sabor == "pr":
            preco = 17
        else:
            preco = 20

    total_pedido += preco

    print(f"Valor do pedido: R${preco:.2f}")

    mais = input("Deseja pedir mais alguma coisa? (s/n): ")
    if mais.lower() != "s":
        break

print(f"Valor total do pedido: R${total_pedido:.2f}")











