class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.ativo = True
        self.livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True
