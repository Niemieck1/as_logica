Entrega do trabalho final de Logica de Programação

- Respondendo possiveis dúvidas

Entidades principais do código são "Livro, Usuário, Emprestimo", cada um deles armazenando informações base para o funcionamento do codigo, como código do livro, quantidade de copias disponivel, ID do usuário, prazo de devolução, status (Devolvido ou ativo) e qual usuário pegou qual livro.

Menu Pricnipal criado para facilitar anavegação e a organização do codigo para o bibliotecario para que ele consiga fazer seus cadastros, consultas e alterações com facilidade.
Cada opção do menu principal leva a um submenu ou realiza a consulta que o bibliotecario deseja.

Ao efetuar um cadastro o sistema verifica se não ha duplicidade de IDs ou codigos. Mantendo assim a organização do estoque de livros.
Na devolução o programa atualiza o status do livro, a quantidade em estoque e calcula a multa caso haja atraso.
o sistema tambem pode listar um relatorio com os livros emprestados, disponiveis e atrasados.

##Principais funções: 
menu_principal(): controla todo o fluxo do sistema.
menu_gerenciar_livros(): controla os cadastros e gereciamento de livros.
cadastrar_livro(): Registra um novo livro no sistema.
listar_livros(): Exibe todos os livros cadastrados com a quantidade disponivel.
menu_gerenciar_usuarios(): Controla os cadastros de alunos e professores.
cadastrar_usuario(): cadastra um novo aluno ou professor.
listar_usuarios(): Mostra os usuários ja cadastrados.
realizar_emprestimo(): registra o emprestimno do livro e calcula o prazo de devolução.
realizar_devolucao(): encerra o emprestimo e calcula a multa em caso de atraso.
menu_relatorios(): Lista os emprestimos em andamento e devoluções em atraso.
relatorio_emprestimos_ativos(): lista todos os emprestimos em andamento e data de devolução prevista.
relatorio_atrasos(): Mostra os emprestimos que estão atrasados no sistema.
menu_gerenciar_tempo(): Permite avançar o tempo no sistema simulando dias passados para controle de prazos e atrasos.
