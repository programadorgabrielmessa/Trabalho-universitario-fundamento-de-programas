"""
QUESTÃO 1 de 4 - Conteúdo até aula 03
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade as informações abaixo:

•	Se quantidade for menor que 200 o desconto será de 0%;
•	Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
•	Se quantidade for igual ou maior que1000 e menor que 2000 o desconto será de 10%;
•	Se quantidade for igual ou maior que 2000 o desconto será de 15%;

Elabore um programa em Python que:
A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
B.	Deve-se entrar com o valor unitário e quantidade do produto [EXIGÊNCIA DE CÓDIGO 1 de 4];
C.	Deve-se retornar o valor total sem desconto e o valor total com desconto[EXIGÊNCIA DE CÓDIGO 2 de 4];
D.	Deve-se utilizar as estruturas if, elif e else (todas elas)[EXIGÊNCIA DE CÓDIGO 3 de 4];
E.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 4 de 4];
F.	Deve-se colocar na apresentação de saída de consoleum pedido recebendo desconto[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 1];

EXEMPLO DE SAÍDA DE CONSOLE:
 
Figura 1: Exemplo de saída de console que o aluno deve fazer.Em que se perguntar o valor do produto (pode ser qualquer valor) a quantidade (deve ser maior que 200) e apresenta o valor final sem o desconto e com o desconto.
 

"""
# A. Mensagem de boas-vindas abaixo
nome = "Gabriel Rodrigues de Almeida Messa"
print(f"Bem-vindo, {nome}!")

# B. Entrada de valor e quantidade do produto
valor_unitario_do_produto = float(input("Digite o valor unitário do produto: "))
quantidades = int(input("Digite a quantidade do produto: "))

# C. Cálculo do valor total sem desconto
valor_total_sem_desconto = valor_unitario_do_produto * quantidades

# Cálculo do desconto com base na quantidade
if quantidades < 200:
    desconto_percentual = 0
elif quantidades < 1000:
    desconto_percentual = 0.05
elif quantidades < 2000:
    desconto_percentual = 0.1
else:
    desconto_percentual = 0.15

# Cálculo do valor total com desconto
valor_desconto = valor_total_sem_desconto * desconto_percentual
valor_total_com_desconto = valor_total_sem_desconto - valor_desconto

# D. Exibição do valor total sem desconto e com desconto
print(f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}")
print(f"Desconto aplicado: {desconto_percentual * 100:.0f}%")
print(f"Valor total com desconto: R${valor_total_com_desconto:.2f}")

# Exibe a saída do pedido e o desconto aplicado
print(f"Pedido: {quantidades} unidades")
print(f"Desconto aplicado: {desconto_percentual * 100:.0f}%")
