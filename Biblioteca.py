# Sistema de Biblioteca - Versão Original Simples
# Este é o arquivo original antes da transformação profissional

class Livro:
    def __init__(self, titulo, autor, isbn, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao}) - {status}"


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.livros_emprestados = []

    def __str__(self):
        return f"{self.nome} ({self.email}) - {len(self.livros_emprestados)} livros emprestados"


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário {usuario.nome} cadastrado.")

    def emprestar_livro(self, isbn, email_usuario):
        livro = None
        for l in self.livros:
            if l.isbn == isbn and l.disponivel:
                livro = l
                break

        if not livro:
            print("Livro não encontrado ou não disponível.")
            return

        usuario = None
        for u in self.usuarios:
            if u.email == email_usuario:
                usuario = u
                break

        if not usuario:
            print("Usuário não encontrado.")
            return

        livro.disponivel = False
        usuario.livros_emprestados.append(livro)
        print(f"Livro '{livro.titulo}' emprestado para {usuario.nome}.")

    def devolver_livro(self, isbn, email_usuario):
        usuario = None
        for u in self.usuarios:
            if u.email == email_usuario:
                usuario = u
                break

        if not usuario:
            print("Usuário não encontrado.")
            return

        livro = None
        for l in usuario.livros_emprestados:
            if l.isbn == isbn:
                livro = l
                break

        if not livro:
            print("Livro não está emprestado para este usuário.")
            return

        livro.disponivel = True
        usuario.livros_emprestados.remove(livro)
        print(f"Livro '{livro.titulo}' devolvido por {usuario.nome}.")

    def listar_livros(self):
        print("\n=== LIVROS NA BIBLIOTECA ===")
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return

        for livro in self.livros:
            print(livro)

    def listar_usuarios(self):
        print("\n=== USUÁRIOS CADASTRADOS ===")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for usuario in self.usuarios:
            print(usuario)


# Exemplo de uso
if __name__ == "__main__":
    # Criar biblioteca
    biblioteca = Biblioteca()

    # Adicionar alguns livros
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "123456789", 1954)
    livro2 = Livro("1984", "George Orwell", "987654321", 1949)
    livro3 = Livro("Dom Casmurro", "Machado de Assis", "111222333", 1899)

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    # Cadastrar usuários
    usuario1 = Usuario("João Silva", "joao@email.com")
    usuario2 = Usuario("Maria Santos", "maria@email.com")

    biblioteca.cadastrar_usuario(usuario1)
    biblioteca.cadastrar_usuario(usuario2)

    # Listar livros e usuários
    biblioteca.listar_livros()
    biblioteca.listar_usuarios()

    # Fazer empréstimos
    biblioteca.emprestar_livro("123456789", "joao@email.com")
    biblioteca.emprestar_livro("987654321", "maria@email.com")

    print("\n=== APÓS EMPRÉSTIMOS ===")
    biblioteca.listar_livros()

    # Devolver livro
    biblioteca.devolver_livro("123456789", "joao@email.com")

    print("\n=== APÓS DEVOLUÇÃO ===")
    biblioteca.listar_livros()