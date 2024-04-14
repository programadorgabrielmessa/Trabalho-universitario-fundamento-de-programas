"""
Enunciado: Você foi contratado para desenvolver um sistema de cobrança de banho para um petshop. Você ficou com a parte de desenvolver a interface com o funcionário.
O petshop opera da seguinte maneira:
•	Para cães com peso menor que 3 kg o valor base é de 40 reais;
•	Para cães com peso igual ou maior que 3 kg e menor que 10 kg o valor base é de 50 reais;
•	Para cães com peso igual ou maior que 10 kg e menor que 30kg o valor base é de 60 reais;  
•	Para cães com peso igual ou maior que 30 kg e menor que 50kg o valor base é de 70 reais; 

	Para cães com pelo curto (c) o multiplicador é 1;
	Para cães com pelo médio (m) o multiplicador é 1.5;
	Para cães com pelo longo (l) o multiplicador é 2;

♦	Para o adicional de cortar unhas (1) do cachorro é cobrado um valor extra de 10 reais;
♦	Para o adicional de escovar os dentes (2) do cachorro é cobrado um valor extra de 12 reais;
♦	Para o adicional de limpar as orelhas (3) do cachorro é cobrado um valor extra de 15 reais;
♦	Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;


O valor final da conta é calculado da seguinte maneira:

total = base * multiplicador + extra

Elabore um programa em Python que: 

A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
B.	Deve-se criar uma função chamada cachorro_peso()em que:[EXIGÊNCIA DE CÓDIGO 1 de 6];
a.	Pergunta o peso do cachorro;
b.	Retorna o valor base com base no peso;
c.	Repete a pergunta do item B.a se peso for igual ou acima 50kg;
d.	Repete a pergunta do item B.a se digitar um valor não numérico;
C.	Deve-se criar uma função chamada cachorro_pelo() em que: [EXIGÊNCIA DE CÓDIGO 2 de 6];
a.	Pergunta o pelo do cachorro;
b.	Retorna o multiplicador com base nos itens descritos no enunciado;
c.	Repete a pergunta do item C.a se digitar uma opção diferente de: c/m/l;
D.	Deve-se criar uma função chamada cachorro_extra() em que: [EXIGÊNCIA DE CÓDIGO 3 de 6];
a.	Pergunta pelo serviço adicional;
b.	Acumular o valor extra de cada adicional;
c.	Repetir a pergunta item D enquanto não se digitar opção de: "não querer mais nada (0)";
d.	Quando digitar o adicional não querer mais nada (0) retornar o valor extra;
E.	Deve-se calcular o total a pagar na parte do mainconforme descrito no enunciado[EXIGÊNCIA DE CÓDIGO 4 de 6];
F.	Deve-se utilizar try/except [EXIGÊNCIA DE CÓDIGO 5 de 6];
G.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
H.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário digitou um valor não numérico para o peso [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
I.	Deve-se colocar na apresentação de console um pedido no qual o usuário digitou um valor acima 50 para o peso [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];
J.	Deve-se colocar na apresentação de console um pedido no qual o peso e o tipo de pelo sejam válidos e com mais 2 extras [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];
 

"""
nome = "Gabriel Rodrigues de Almeida Messa"
print(f"Bem-vindo, {nome}!")

def entrada_peso():
    print("Escolha o peso do cachorro:")
    print("Menor que 3 kg - Valor base: R$40")
    print("3 kg ou mais, e menor que 10 kg - Valor base: R$50")
    print("10 kg ou mais, e menor que 30 kg - Valor base: R$60")
    print("30 kg ou mais, e menor que 50 kg - Valor base: R$70")

    while True:
        try:
            peso = float(input("Digite o peso do cachorro em kg: "))
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Peso muito alto. Digite novamente.")
        except ValueError:
            print("Valor inválido. Digite novamente.")

def entrada_pelo():
    print("Escolha o tipo de pelo:")
    print("c - Pelo curto (Multiplicador: 1)")
    print("m - Pelo médio (Multiplicador: 1.5)")
    print("l - Pelo longo (Multiplicador: 2)")

    while True:
        pelo = input("Digite o tipo de pelo do cachorro (c/m/l): ")
        if pelo == "c":
            return 1
        elif pelo == "m":
            return 1.5
        elif pelo == "l":
            return 2
        else:
            print("Tipo de pelo inválido. Digite novamente.")

def entrada_adicionais():
    print("Escolha o serviço adicional:")
    print("1 - Cortar unhas (R$10)")
    print("2 - Escovar dentes (R$12)")
    print("3 - Limpar orelhas (R$15)")
    print("0 - Não querer mais nada (R$0)")

    extra = 0
    for _ in range(1):
        while True:
            try:
                adicional = int(input("Digite o número do serviço adicional: "))
                if adicional == 1:
                    extra += 10
                    print("Cortar unhas")
                elif adicional == 2:
                    extra += 12
                    print("Escovar dentes")
                elif adicional == 3:
                    extra += 15
                    print("Limpar orelhas")
                elif adicional == 0:
                    print("Não querer mais nada")
                    break
            except ValueError:
                print("Valor inválido. Digite novamente.")
    return extra

# Solicitar informações
peso = entrada_peso()
pelo = entrada_pelo()
extra = entrada_adicionais()

# Calcular total e mostrar resultado
total = extra + pelo + peso
print(f"Total a pagar: R${total:.2f}")



