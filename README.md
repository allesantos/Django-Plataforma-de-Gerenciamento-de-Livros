# Casa dos Livros - Plataforma de Gerenciamento de Livros
 
Este é um projeto de uma plataforma de gerenciamento de livros desenvolvida com Django. 

## Índice
- [Descrição](#Descrição)
- [Recursos](#Recursos)
- [Tecnologias Utilizadas](#Tecnologias)
- [Pré-requisitos](#Pré-requisitos)
- [Uso](#Uso)
- [Instalação](#Instalação)
- [Contribuição](#Contribuição)
- [Licença](#Licença)

## Descrição
**Casa dos Livros** é uma plataforma que permite que os usuários se cadastrem, façam login e publiquem informações sobre os livros que possuem. Além disso, os usuários podem emprestar seus livros fisicamente para outros usuários cadastrados ou visitantes, registrar devoluções e avaliar o estado dos livros devolvidos.

## Recursos
- Cadastro e login de usuários.
- Publicação de informações sobre livros.
- Empréstimo de livros para outros usuários ou visitantes.
- Registro de devoluções com avaliação do estado do livro.
- Interface amigável e responsiva.

## Tecnologias
- __Backend:__ Django 5.x
- __Banco de Dados:__ SQLite (padrão)
- __Frontend:__ HTML, CSS, Bootstrap e JavaScript

## Pré-requisitos
Antes de iniciar, certifique-se de ter os seguintes itens instalados:
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado para isolamento do ambiente)
- Git

## Uso
1. Na imagem abaixo, temos uma representação da tela inicial do projeto.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/01.png">


2. Para utilizar o sistema é necessário realizar um cadastro, registrando apenas usuário, email e senha.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/02.png">


3. Após o cadastro, é preciso fazer login para ter acesso a sua própria sessão de usuário.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/03.png">


4. No canto direito da página, após realizar o login, temos um botão de Menu, onde é possível desde realizar cadastro, emprestimo, devolução como também visualizar os livros que alguém emprestou para este usuário e ver o total de livros já publicados.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/05.png">


5. Clicando em Opções do Menu, temos "Categoria", "Livro", "Empréstimo" e "Devolução". Realize primeiro o cadastro das categorias dos livros que deseja publicar, por exemplo, "Ação", "Romance", "Terror" etc. Quando for cadastrar um livro, você também pode enviar uma imagem que servirá como capa do livro.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/06.png">


5. Em "Emprestimo" você poderá emprestar seus livros para usuários "Visitante", ou seja que não possui ainda um cadastro no sistema como também para usuários que já possuem um cadastro, basta apenas alternar entre os dois botões.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/07.png">


6. Quando for acessar a página que possui mais informações sobre um dos livros publicados, nela é possível ainda alterar ou excluir o livro.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/08.png">

7. Quando for registrar a devolução de um livro que havia antes emprestado para um usuário, é possível avaliar o estado de como foi devolvido o livro. A avaliação será classificada em forma de estrelas.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/10.png">

Note que não será possível avaliar a devolução de um livro caso o usuário ainda não tenha devolvido para você, sendo assim, o botão "Avaliar" será visualizado, porém indisponível para avaliação.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Biblioteca-Django/11.png">

## Instalação
1. Clone o repositório para sua máquina local:

    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie e ative um ambiente virtual:

    ```
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:

    ```
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```
    python manage.py runserver
    ```

6. Acesse o sistema em http://127.0.0.1:8000/ no seu navegador.

## Contribuição
Sinta-se à vontade para contribuir com este projeto. Siga estas etapas:

1. Faça um fork do repositório.

2. Crie uma nova branch para sua feature/bugfix:

    ```
    git checkout -b minha-feature
    ```

3. Envie suas alterações:

    ```
    git push origin minha-feature
    ```

4. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.

