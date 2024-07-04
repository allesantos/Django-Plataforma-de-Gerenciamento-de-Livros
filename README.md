# Projeto em Django - Sistema de Gerenciamento de Livros Alleart
 
Este é um projeto de uma plataforma de gerenciamento de livros onde é possível o usuário se cadastrar, fazer login e publicar informações sobre os livros que ele possui. Também é possível este usuário emprestar seus livros de forma física para outros usuários cadastrados ou não cadastrados (visitantes), assim como também fazer o registro da devolução e avaliar o estado do livro devolvido. Este projeto ainda está em sua fase beta, portanto será feito no futuro ainda alguns outros aprimoramentos, correções e mais features. É possível acessar o sistema através do link https://allesantos.pythonanywhere.com/auth/cadastro/ . Está funcional, então caso queira testa-lo, basta criar um cadastro, depois fazer login e começar publicar informações de livros.


Na imagem abaixo, temos alguns exemplos de livros publicados por um usuário.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/01.png">



Para utilizar o sistema é necessário realizar um cadastro, registrando apenas nome, email e senha.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/07.png">



Após o cadastro, é preciso fazer login para ter acesso a sua própria sessão de usuário.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/08.png">


No canto direito da página, após realizar o login, temos um botão de Menu, onde é possível desde realizar cadastro, emprestimo, devolução como também visualizar os livros que alguém emprestou para este usuário e ver o total de livros já publicados.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/02.png">


Clicando em Opções do Menu, temos "Categoria", "Livro", "Empréstimo" e "Devolução". Realize primeiro o cadastro das categorias dos livros que deseja publicar, por exemplo, "Ação", "Romance", "Terror" etc. Quando for cadastrar um livro, você também pode enviar uma imagem que servirá como capa do livro.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/03.png">


Em "Emprestimo" você poderá emprestar seus livros para usuários "Visitante", ou seja que não possui ainda um cadastro no sistema como também para usuários que já possuem um cadastro, basta apenas alternar entre os dois botões.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/04.png">


Quando for acessar a página que possui mais informações sobre um dos livros publicados, nela é possível ainda alterar ou excluir o livro.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/05.png">


Quando for registrar a devolução de um livro que havia antes emprestado para um usuário, é possível avaliar o estado de como foi devolvido o livro. A avaliação será classificada em forma de estrelas.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/05b.png">


Note que não será possível avaliar a devolução de um livro caso o usuário ainda não tenha devolvido para você, sendo assim, o botão "Avaliar" será visualizado, porém indisponível para avaliação.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/05c.png">


