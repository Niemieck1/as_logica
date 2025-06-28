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

Quando um usuário solicita um empréstimo, o sistema primeiro verifica se ele existe, se o livro está cadastrado e se há exemplares disponíveis. 
Depois disso, ele define o prazo de devolução com base no tipo do usuário: Aluno ou professor.
Se for aluno, 7 dias de prazo. Se for professor, 10 dias de prazo.
Esse prazo é calculado somando o valor atual do dia_atual_sistema ao número de dias permitidos. Assim, o sistema registra dois dados importantes:
O dia do empréstimo que é o dia atual. E o dia da devolução prevista, baseado no tipo de usuário.

No empréstimo, o sistema verifica se o livro e o usuário existem e se há exemplar disponível. Depois, define o prazo: 7 dias para aluno e 10 para professor, somando ao dia atual do sistema.
Na devolução, registra o dia da entrega e, se houver atraso, calcula a multa com base nos dias de atraso, cobrando 1 real por dia.
Tudo é feito com um contador de dias, sem usar datas reais, e o tempo é avançado manualmente pelo usuário.

O sistema compara o dia da devolução com o prazo previsto. Se o livro for devolvido no prazo, não há multa.
Se houver atraso, calcula quantos dias passaram do prazo. Depois, multiplica esse atraso por R$ 1,00 por dia.
O valor final da multa é mostrado ao usuário na hora da devolução. Tudo isso é feito com base no dia simulado, sem usar datas reais.
O tempo no sistema é controlado por um contador que o usuário avança manualmente.

O sistema  usa um contador chamado dia_atual_sistema. Esse contador começa no dia 1. O usuário pode avançar os dias manualmente.
Isso é feito no menu de gerenciamento de tempo. Com isso, dá para simular o passar dos dias facilmente. Isso facilita testes, prazos e cálculo de multas no sistema.

