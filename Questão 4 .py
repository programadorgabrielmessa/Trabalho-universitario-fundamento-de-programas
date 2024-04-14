"""
Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerencial de pessoas. Este software deve ter o seguinte menu e opções:

1)	Cadastrar Colaborador
2)	Consultar Colaborador
1.	Consultar Todos 
2.	Consultar por Id;
3.	Consultar por Setor;
4.	Retornar ao menu;
3)	Remover Colaborador
4)	Encerrar Programa

Elabore um programa em Python que: 

A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
B.	Deve-se criar uma lista vazia com o nome de lista_colaboradores e a variável id_global com valor inicial igual a 0 [EXIGÊNCIA DE CÓDIGO 1 de 7];
C.	Deve-se criar uma função chamada cadastrar_colaborador(id) em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
a.	Pergunta nome,setor, pagamento do colaborador;
b.	Armazena oid (este é fornecido via parâmetro da função),nome, setor, salário dentro de um dicionário;
c.	Copiar o dicionário dentro para dentro da lista_colaboradores;
D.	Deve-se criar uma função chamada consultar_colaborador() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
a.	Deve-se pergunta qual opção deseja (1. Consultar Todos /2. Consultar por Id/ 3. Consultar por Setor / 4. Retornar ao menu) e   realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4:
i.	Se Consultar Todos, apresentar todos os colaboradores com todos os seus dados cadastrados;
ii.	Se Consultar por Id, apresentar ocolaborador específico com todos os seus dados cadastrados;
iii.	Se Consultar por Setor, apresentar todos os colaboradores do setor específico com todos os seus dados cadastrados;
iv.	Se Retornar ao menu, deve-se retornar ao menu principal
E.	Deve-se criar uma função chamada remover_colaborador() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
a.	Deve-se pergunta pelo id do colaborador a ser removido;
b.	Remover o colaborador da lista_colaboradores;
F.	Deve-se criar uma estrutura de menu no main em que: [EXIGÊNCIA DE CÓDIGO 5 de 7];
a.	Deve-se pergunta qual opção deseja (1. Cadastrar Colaborador / 2. Consultar Colaborador / 3. Remover Colaborador / 4. Encerrar Programa)e realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4:
i.	Se Cadastrar Colaborador, acrescentar em uma variavel id_ global e chamar a função cadastrar_colaborador(id_ global);
ii.	Se Consultar Colaborador, chamar função consultar_colaborador();
iii.	Se Remover Colaborador, chamar função remover_colaborador();
iv.	Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
G.	Deve-se utilizar lista de dicionários(uma lista contento dicionários dentro)[EXIGÊNCIA DE CÓDIGO 6 de 7];
H.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
I.	Deve-se colocar na apresentação de saída de console o cadastro de 3 colaboradores (sendo 2 deles no mesmo setor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
J.	Deve-se colocar na apresentação de saída de console a consulta de todos os colaboradores [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de ];
K.	Deve-se colocar na apresentação de saída de console a consulta por código de um dos colaboradores[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
L.	Deve-se colocar na apresentação de saída de console a consulta por setor em que 2 colaboradores façam parte [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
M.	Deve-se colocar na apresentação de saída de console a remoção de um dos colaboradores e na sequência a consulta de todos os colaboradores[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];
 

"""
# Imprime uma mensagem de boas-vindas ao iniciar o programa.
Seu_nome = 'Gabriel Rodrigues de Almeida Messa'
print(f"Bem-vindo ao software de gerenciamento de pessoas por {Seu_nome}!")

# Inicializa uma lista vazia para armazenar os colaboradores e uma variável id_global com valor inicial zero.
# A lista armazena os dados dos colaboradores e id_global é usado para atribuir IDs exclusivos aos colaboradores.
lista_colaboradores = []
id_global = 0

# Função para cadastrar colaboradores. Ela aceita um ID como parâmetro, que é o valor atual de id_global.
def cadastrar_colaborador(id_global):
    # Coleta informações básicas do colaborador.
    print("\nCadastro de Novo Colaborador:")
    nome = input("Digite o nome completo do colaborador: ")
    setor = input("Digite o setor em que o colaborador trabalha: ")

    # Validação do valor de pagamento para garantir que seja um número.
    while True:
        try:
            pagamento = float(input("Digite o pagamento mensal do colaborador: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número válido para o pagamento.")

    # Cria um dicionário com as informações do colaborador e adiciona à lista de colaboradores.
    colaborador = {
        "id": id_global,
        "nome": nome,
        "setor": setor,
        "pagamento": pagamento
    }
    lista_colaboradores.append(colaborador)
    print("Colaborador cadastrado com sucesso!")

# Função para consultar colaboradores. Pode buscar todos os colaboradores, por ID específico ou por setor.
def consultar_colaborador():
    while True:
        # Apresenta as opções de consulta ao usuário.
        print("\nOpções de Consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")

        # Captura a escolha do usuário e realiza a ação correspondente.
        try:
            opcao_consulta = int(input("Escolha uma opção de consulta: "))
            if opcao_consulta in [1, 2, 3, 4]:
                if opcao_consulta == 1:
                    print("\nListagem de Todos os Colaboradores:")
                    print("ID | Nome | Setor | Pagamento")
                    for colaborador in lista_colaboradores:
                        print(f"{colaborador['id']} | {colaborador['nome']} | {colaborador['setor']} | {colaborador['pagamento']}")
                elif opcao_consulta == 2:
                    print("\nConsulta por ID:")
                    id_busca = int(input("Digite o id do colaborador: "))
                    # Flag para verificar se o colaborador foi encontrado.
                    encontrado = False
                    for colaborador in lista_colaboradores:
                        if colaborador['id'] == id_busca:
                            print(f"ID: {colaborador['id']}, Nome: {colaborador['nome']}, Setor: {colaborador['setor']}, Pagamento: {colaborador['pagamento']}")
                            encontrado = True
                            break
                    if not encontrado:
                        print("Colaborador não encontrado.")
                elif opcao_consulta == 3:
                    print("\nConsulta por Setor:")
                    setor_busca = input("Digite o setor: ")
                    # Filtra colaboradores pelo setor e exibe os encontrados.
                    colaboradores_setor = [col for col in lista_colaboradores if col['setor'] == setor_busca]
                    if colaboradores_setor:
                        print(f"Colaboradores do setor {setor_busca}:")
                        for col in colaboradores_setor:
                            print(f"{col['id']} | {col['nome']} | {col['setor']} | {col['pagamento']}")
                    else:
                        print(f"Nenhum colaborador encontrado no setor '{setor_busca}'.")
                elif opcao_consulta == 4:
                    # Retorna ao menu principal.
                    return
            else:
                print("Opção inválida.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para a opção desejada.")

# Função para remover colaboradores.
def remover_colaborador():
    print("\nRemoção de Colaborador:")
    id_remover = int(input("Digite o ID do colaborador a ser removido: "))
    # Flag para verificar se o colaborador foi removido.
    removido = False
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id_remover:
            lista_colaboradores.remove(colaborador)
            removido = True
            print("Colaborador removido com sucesso!")
            break
    if not removido:
        print("Colaborador não encontrado.")

# Loop principal para execução do programa.
while True:
    # Apresenta o menu principal e as opções disponíveis.
    print("\nMenu Principal:")
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")

    # Captura a escolha do usuário e realiza a ação correspondente.
    try:
        opcao_menu = int(input("Escolha uma opção: "))
        if opcao_menu in [1, 2, 3, 4]:
            if opcao_menu == 1:
                # Incrementa o ID global para cada novo colaborador e chama a função de cadastro.
                id_global += 1
                cadastrar_colaborador(id_global)
            elif opcao_menu == 2:
                # Chama a função de consulta.
                consultar_colaborador()
            elif opcao_menu == 3:
                # Chama a função de remoção.
                remover_colaborador()
            elif opcao_menu == 4:
                # Encerra o programa.
                print("Encerrando o programa.")
                break
        else:
            print("Opção inválida.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para a opção desejada.")

