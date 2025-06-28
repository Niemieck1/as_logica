from dataclasses import dataclass

# Definição das entidades principais com dataclasses para clareza e simplicidade
@dataclass
class Livro:
    codigo: str
    titulo: str
    autor: str
    ano: int
    genero: str
    quantidade_total: int
    quantidade_disponivel: int

@dataclass
class Usuario:
    id_usuario: str
    nome: str
    tipo: str  # "aluno" ou "professor"

@dataclass
class Emprestimo:
    id_usuario: str
    codigo_livro: str
    dia_emprestimo: int
    dia_devolucao_prevista: int
    status: str  # "ativo" ou "devolvido"
    dia_devolucao_efetiva: int = None  # opcional, só usado na devolução

# Listas globais que armazenam dados do sistema
livros = []
usuarios = []
emprestimos = []

dia_atual_sistema = 1  # contador que simula o dia atual no sistema
VALOR_MULTA_POR_DIA = 1.0  # valor fixo da multa por dia de atraso

# Menu principal do sistema, fica em loop até o usuário escolher sair
def menu_principal():
    global dia_atual_sistema

    while True:
        print("\n========== MENU PRINCIPAL ==========")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Usuários")
        print("3. Realizar Empréstimo")
        print("4. Realizar Devolução")
        print("5. Relatórios")
        print("6. Gerenciar Tempo")
        print("7. Sair")
        print("--------------------------------------")

        escolha = input("Escolha uma opção: ")

        # Direciona para o submenu ou função correspondente
        if escolha == '1':
            menu_gerenciar_livros()
        elif escolha == '2':
            menu_gerenciar_usuarios()
        elif escolha == '3':
            realizar_emprestimo()
        elif escolha == '4':
            realizar_devolucao()
        elif escolha == '5':
            menu_relatorios()
        elif escolha == '6':
            dia_atual_sistema = menu_gerenciar_tempo(dia_atual_sistema)
        elif escolha == '7':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu para gerenciar livros (cadastrar, listar)
def menu_gerenciar_livros():
    while True:
        print("\n--- Gerenciar Livros ---")
        print("1. Cadastrar Novo Livro")
        print("2. Listar Todos os Livros")
        print("3. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para cadastrar um novo livro com validação de código único
def cadastrar_livro():
    print("\n--- Cadastro de Livro ---")
    codigo = input("Código do livro: ")

    # Verifica se já existe livro com o código informado
    for livro in livros:
        if livro.codigo == codigo:
            print("Já existe um livro com este código.")
            return

    titulo = input("Título: ")
    autor = input("Autor: ")

    try:
        ano = int(input("Ano de publicação: "))
        quantidade = int(input("Quantidade total de exemplares: "))
    except ValueError:
        print("Ano e quantidade devem ser números inteiros.")
        return

    genero = input("Gênero: ")

    # Cria e adiciona o livro à lista global
    novo_livro = Livro(codigo, titulo, autor, ano, genero, quantidade, quantidade)
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")

# Função para listar todos os livros cadastrados
def listar_livros():
    print("\n--- Lista de Livros ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print(f"\nCódigo: {livro.codigo}")
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Ano: {livro.ano}")
        print(f"Gênero: {livro.genero}")
        print(f"Quantidade Total: {livro.quantidade_total}")
        print(f"Quantidade Disponível: {livro.quantidade_disponivel}")

# Submenu para gerenciar usuários (cadastrar, listar)
def menu_gerenciar_usuarios():
    while True:
        print("\n--- Gerenciar Usuários ---")
        print("1. Cadastrar Novo Usuário")
        print("2. Listar Todos os Usuários")
        print("3. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Cadastra um novo usuário com validação de ID único e tipo válido
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    id_usuario = input("ID do usuário: ")

    for usuario in usuarios:
        if usuario.id_usuario == id_usuario:
            print("Já existe um usuário com este ID.")
            return

    nome = input("Nome: ")
    tipo = input("Tipo (aluno ou professor): ").strip().lower()

    if tipo not in ["aluno", "professor"]:
        print("Tipo inválido. Deve ser 'aluno' ou 'professor'.")
        return

    novo_usuario = Usuario(id_usuario, nome, tipo)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

# Lista todos os usuários cadastrados
def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(f"\nID: {usuario.id_usuario}")
        print(f"Nome: {usuario.nome}")
        print(f"Tipo: {usuario.tipo}")

# Função para realizar empréstimo, com validações e cálculo de prazo
def realizar_emprestimo():
    print("\n--- Realizar Empréstimo ---")
    id_usuario = input("ID do usuário: ")
    codigo_livro = input("Código do livro: ")

    # Procura usuário e livro, valida existência
    usuario = next((u for u in usuarios if u.id_usuario == id_usuario), None)
    if not usuario:
        print("Usuário não encontrado.")
        return

    livro = next((l for l in livros if l.codigo == codigo_livro), None)
    if not livro:
        print("Livro não encontrado.")
        return

    # Verifica se livro está disponível para empréstimo
    if livro.quantidade_disponivel <= 0:
        print("Não há exemplares disponíveis para empréstimo.")
        return

    # Define prazo conforme tipo do usuário
    prazo = 7 if usuario.tipo == "aluno" else 10

    dia_emprestimo = dia_atual_sistema
    dia_devolucao_prevista = dia_emprestimo + prazo

    # Registra empréstimo e atualiza estoque
    novo_emprestimo = Emprestimo(id_usuario, codigo_livro, dia_emprestimo, dia_devolucao_prevista, "ativo")
    emprestimos.append(novo_emprestimo)
    livro.quantidade_disponivel -= 1

    print("Empréstimo realizado com sucesso!")
    print(f"Devolução prevista para o dia: {dia_devolucao_prevista}")

# Função para registrar devolução e calcular multa se necessário
def realizar_devolucao():
    print("\n--- Realizar Devolução ---")
    id_usuario = input("ID do usuário: ")
    codigo_livro = input("Código do livro: ")

# Procura empréstimo ativo do usuário para o livro
    emprestimo = next((e for e in emprestimos 
                      if e.id_usuario == id_usuario and e.codigo_livro == codigo_livro and e.status == "ativo"), None)

    if not emprestimo:
        print("Nenhum empréstimo ativo encontrado para esse usuário e livro.")
        return

    # Atualiza status do empréstimo e quantidade disponível do livro
    emprestimo.dia_devolucao_efetiva = dia_atual_sistema
    emprestimo.status = "devolvido"
    livro = next((l for l in livros if l.codigo == codigo_livro), None)
    if livro:
        livro.quantidade_disponivel += 1

    # Calcula multa se houver atraso
    atraso = emprestimo.dia_devolucao_efetiva - emprestimo.dia_devolucao_prevista
    if atraso > 0:
        multa = atraso * VALOR_MULTA_POR_DIA
        print(f"Devolvido com atraso de {atraso} dia(s). Multa: R${multa:.2f}")
    else:
        print("Livro devolvido no prazo. Nenhuma multa aplicada.")

    print("Devolução registrada com sucesso.")

# Submenu para relatórios
def menu_relatorios():
    while True:
        print("\n--- Relatórios ---")
        print("1. Livros Emprestados Atualmente")
        print("2. Livros com Devolução em Atraso")
        print("3. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            relatorio_emprestimos_ativos()
        elif opcao == '2':
            relatorio_atrasos()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Exibe empréstimos ativos com dados do livro e usuário
def relatorio_emprestimos_ativos():
    print("\n--- Empréstimos Ativos ---")
    ativos = [e for e in emprestimos if e.status == "ativo"]

    if not ativos:
        print("Nenhum empréstimo ativo.")
        return

    for e in ativos:
        livro = next((l for l in livros if l.codigo == e.codigo_livro), None)
        usuario = next((u for u in usuarios if u.id_usuario == e.id_usuario), None)
        if livro and usuario:
            print(f"\nLivro: {livro.titulo}")
            print(f"Usuário: {usuario.nome}")
            print(f"Devolução prevista: Dia {e.dia_devolucao_prevista}")

# Exibe empréstimos em atraso baseando-se no dia atual do sistema
def relatorio_atrasos():
    print("\n--- Empréstimos em Atraso ---")
    atrasados = [e for e in emprestimos if e.status == "ativo" and e.dia_devolucao_prevista < dia_atual_sistema]

    if not atrasados:
        print("Nenhum empréstimo em atraso.")
        return

    for e in atrasados:
        livro = next((l for l in livros if l.codigo == e.codigo_livro), None)
        usuario = next((u for u in usuarios if u.id_usuario == e.id_usuario), None)
        atraso = dia_atual_sistema - e.dia_devolucao_prevista
        if livro and usuario:
            print(f"\nLivro: {livro.titulo}")
            print(f"Usuário: {usuario.nome}")
            print(f"Devolução prevista: Dia {e.dia_devolucao_prevista}")
            print(f"Atraso: {atraso} dia(s)")

# Submenu para simular passagem de tempo no sistema
def menu_gerenciar_tempo(dia_atual):
    while True:
        print("\n--- Gerenciar Tempo ---")
        print(f"Dia Atual do Sistema: {dia_atual}")
        print("1. Avançar 1 dia")
        print("2. Avançar 7 dias (1 semana)")
        print("3. Avançar N dias")
        print("4. Consultar dia atual")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            dia_atual += 1
            print(f"Avançou 1 dia. Novo dia: {dia_atual}")
        elif opcao == '2':
            dia_atual += 7
            print(f"Avançou 7 dias. Novo dia: {dia_atual}")
        elif opcao == '3':
            try:
                n = int(input("Quantos dias deseja avançar? "))
                if n > 0:
                    dia_atual += n
                    print(f"Avançou {n} dias. Novo dia: {dia_atual}")
                else:
                    print("Insira um número positivo.")
            except ValueError:
                print("Entrada inválida.")
        elif opcao == '4':
            print(f"O dia atual é: {dia_atual}")
        elif opcao == '5':
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    return dia_atual

# Inicia o sistema chamando o menu principal
menu_principal()
