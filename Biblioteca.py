class Livro:

    def __init__(self, titulo=None, autor=None, ano=None):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False
        
    def devolver(self):
        self.disponivel = True

class Usuario:

    def __init__(self, nome):
        self.nome = nome
        self.livros_alocados = []

    def pegar_livro(self, livro: Livro):
        if livro.emprestar():
            self.livros_alocados.append(livro)
            print(f"{self.nome} alocou o livro {livro.titulo}")
        else:
            print(f"O livro {livro.titulo} já está emprestado")

    def devolver_livro(self, livro: Livro):
        if livro in self.livros_alocados:
            livro.devolver()
            self.livros_alocados.remove(livro)
            print(f"{self.nome} devolveu o livro {livro.titulo}")
        else:
            print(f"{self.nome} não alocou esse livro.")

class Biblioteca:

    def __init__(self, nome):
        self.nome_biblioteca = nome
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def listar_livros(self):
        print(f"\n---- Catálogo da {self.nome_biblioteca} ----------")
        for livro in self.livros:
            print(f"Titulo: {livro.titulo} | Ano: {livro.ano} | Autor: {livro.autor} | Disponível: {livro.disponivel}")

if __name__ == "__main__":

    biblioteca = Biblioteca("Biblioteca Central")

    #adicionar livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro2 = Livro("Auto da Compadecida", "Ariano Suassuna", 1955)
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # adicionar usuario
    usuario1 = Usuario("Amanda")
    usuario2 = Usuario("Fulano")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    biblioteca.listar_livros()

    usuario1.pegar_livro(livro2)

    biblioteca.listar_livros()

    usuario1.devolver_livro(livro2)

    biblioteca.listar_livros()
