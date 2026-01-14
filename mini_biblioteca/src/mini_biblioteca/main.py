from livros import Livro
from usuarios import Usuario
from emprestimos import Emprestimo

def main():
    novo_usuario = Usuario("Roger", 1)

    novo_livro = Livro("Os Pequeninos", "Samuel Jackson", "1234")

    novo_emprestimo = Emprestimo(novo_livro, novo_usuario)

    novo_emprestimo.devolver()
    print(f"Empréstimo devolvido:\nLivro disponível: {novo_emprestimo.livro.disponivel}\nEmpréstimo ativo: {novo_emprestimo.ativo}")


if __name__ == "__main__":
    main()
    