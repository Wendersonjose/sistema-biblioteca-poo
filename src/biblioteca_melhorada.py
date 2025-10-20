"""
Sistema de Biblioteca em Python
Desenvolvido usando Programação Orientada a Objetos (POO)
Autor: Wenderson José
Data: Outubro 2025
"""

from datetime import datetime
from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class Livro:
    """Classe que representa um livro na biblioteca."""
    
    titulo: str
    autor: str
    ano: int
    isbn: Optional[str] = None
    disponivel: bool = True
    data_emprestimo: Optional[datetime] = None
    
    def __post_init__(self):
        """Validações após inicialização."""
        if self.ano < 0 or self.ano > datetime.now().year:
            raise ValueError("Ano inválido para o livro")
        if not self.titulo.strip():
            raise ValueError("Título não pode estar vazio")
        if not self.autor.strip():
            raise ValueError("Autor não pode estar vazio")

    def emprestar(self) -> bool:
        """
        Empresta o livro se estiver disponível.
        
        Returns:
            bool: True se emprestado com sucesso, False caso contrário
        """
        if self.disponivel:
            self.disponivel = False
            self.data_emprestimo = datetime.now()
            return True
        return False
        
    def devolver(self) -> None:
        """Devolve o livro, tornando-o disponível novamente."""
        self.disponivel = True
        self.data_emprestimo = None

    def __str__(self) -> str:
        """Representação em string do livro."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} ({self.ano}) - {self.autor} | Status: {status}"


@dataclass 
class Usuario:
    """Classe que representa um usuário da biblioteca."""
    
    nome: str
    email: Optional[str] = None
    livros_emprestados: List[Livro] = field(default_factory=list)
    limite_livros: int = 3
    
    def __post_init__(self):
        """Validações após inicialização."""
        if not self.nome.strip():
            raise ValueError("Nome não pode estar vazio")

    def pegar_livro(self, livro: Livro) -> bool:
        """
        Tenta emprestar um livro para o usuário.
        
        Args:
            livro: O livro a ser emprestado
            
        Returns:
            bool: True se emprestado com sucesso, False caso contrário
        """
        if len(self.livros_emprestados) >= self.limite_livros:
            print(f"❌ {self.nome} atingiu o limite de {self.limite_livros} livros")
            return False
            
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print(f"✅ {self.nome} emprestou '{livro.titulo}'")
            return True
        else:
            print(f"❌ O livro '{livro.titulo}' não está disponível")
            return False

    def devolver_livro(self, livro: Livro) -> bool:
        """
        Devolve um livro emprestado.
        
        Args:
            livro: O livro a ser devolvido
            
        Returns:
            bool: True se devolvido com sucesso, False caso contrário
        """
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"✅ {self.nome} devolveu '{livro.titulo}'")
            return True
        else:
            print(f"❌ {self.nome} não possui o livro '{livro.titulo}'")
            return False

    def listar_livros_emprestados(self) -> None:
        """Lista todos os livros emprestados pelo usuário."""
        if not self.livros_emprestados:
            print(f"📚 {self.nome} não possui livros emprestados")
        else:
            print(f"📚 Livros emprestados por {self.nome}:")
            for livro in self.livros_emprestados:
                dias_emprestado = (datetime.now() - livro.data_emprestimo).days
                print(f"  • {livro.titulo} - {dias_emprestado} dias")

    def __str__(self) -> str:
        """Representação em string do usuário."""
        return f"{self.nome} ({len(self.livros_emprestados)}/{self.limite_livros} livros)"


class Biblioteca:
    """Classe principal que gerencia a biblioteca."""
    
    def __init__(self, nome: str):
        """
        Inicializa a biblioteca.
        
        Args:
            nome: Nome da biblioteca
        """
        if not nome.strip():
            raise ValueError("Nome da biblioteca não pode estar vazio")
            
        self.nome = nome
        self.livros: List[Livro] = []
        self.usuarios: List[Usuario] = []

    def adicionar_livro(self, livro: Livro) -> None:
        """
        Adiciona um livro ao acervo.
        
        Args:
            livro: Livro a ser adicionado
        """
        self.livros.append(livro)
        print(f"📖 Livro '{livro.titulo}' adicionado ao acervo")

    def registrar_usuario(self, usuario: Usuario) -> None:
        """
        Registra um usuário na biblioteca.
        
        Args:
            usuario: Usuário a ser registrado
        """
        # Verifica se usuário já existe
        if any(u.nome.lower() == usuario.nome.lower() for u in self.usuarios):
            print(f"❌ Usuário '{usuario.nome}' já está registrado")
            return
            
        self.usuarios.append(usuario)
        print(f"👤 Usuário '{usuario.nome}' registrado com sucesso")

    def listar_livros(self) -> None:
        """Lista todos os livros do acervo."""
        if not self.livros:
            print("📚 Nenhum livro no acervo")
            return
            
        print(f"\n📚 ═══ Catálogo da {self.nome} ═══")
        print("-" * 50)
        
        for i, livro in enumerate(self.livros, 1):
            print(f"{i:2d}. {livro}")

    def buscar_livro(self, termo: str) -> List[Livro]:
        """
        Busca livros por título ou autor.
        
        Args:
            termo: Termo de busca
            
        Returns:
            Lista de livros encontrados
        """
        termo = termo.lower()
        encontrados = [
            livro for livro in self.livros 
            if termo in livro.titulo.lower() or termo in livro.autor.lower()
        ]
        
        if encontrados:
            print(f"\n🔍 Encontrados {len(encontrados)} livro(s):")
            for livro in encontrados:
                print(f"  • {livro}")
        else:
            print(f"❌ Nenhum livro encontrado com o termo '{termo}'")
            
        return encontrados

    def estatisticas(self) -> None:
        """Exibe estatísticas da biblioteca."""
        total_livros = len(self.livros)
        livros_disponiveis = sum(1 for livro in self.livros if livro.disponivel)
        livros_emprestados = total_livros - livros_disponiveis
        total_usuarios = len(self.usuarios)
        
        print(f"\n📊 ═══ Estatísticas da {self.nome} ═══")
        print(f"📚 Total de livros: {total_livros}")
        print(f"✅ Livros disponíveis: {livros_disponiveis}")
        print(f"📤 Livros emprestados: {livros_emprestados}")
        print(f"👥 Usuários registrados: {total_usuarios}")
        
        if total_livros > 0:
            taxa_utilizacao = (livros_emprestados / total_livros) * 100
            print(f"📈 Taxa de utilização: {taxa_utilizacao:.1f}%")


def main():
    """Função principal - demonstração do sistema."""
    print("🏛️  Sistema de Biblioteca - Demo")
    print("=" * 40)
    
    # Criar biblioteca
    biblioteca = Biblioteca("Biblioteca Central de São Paulo")
    
    # Adicionar livros
    livros = [
        Livro("Dom Casmurro", "Machado de Assis", 1899, "978-85-254-1234-5"),
        Livro("O Cortiço", "Aluísio Azevedo", 1890, "978-85-254-5678-9"),
        Livro("Auto da Compadecida", "Ariano Suassuna", 1955),
        Livro("Clean Code", "Robert C. Martin", 2008, "978-01-321-5063-2"),
        Livro("Python Fluente", "Luciano Ramalho", 2015, "978-85-7522-462-7")
    ]
    
    for livro in livros:
        biblioteca.adicionar_livro(livro)
    
    print()
    
    # Registrar usuários  
    usuarios = [
        Usuario("Amanda Silva", "amanda@email.com"),
        Usuario("Carlos Santos", "carlos@email.com"),
        Usuario("Maria Oliveira")
    ]
    
    for usuario in usuarios:
        biblioteca.registrar_usuario(usuario)
    
    print()
    
    # Demonstrar funcionalidades
    biblioteca.listar_livros()
    biblioteca.estatisticas()
    
    print("\n🎯 Demonstrando empréstimos:")
    print("-" * 30)
    
    # Empréstimos
    usuarios[0].pegar_livro(livros[0])  # Amanda pega Dom Casmurro
    usuarios[1].pegar_livro(livros[3])  # Carlos pega Clean Code
    usuarios[0].pegar_livro(livros[4])  # Amanda pega Python Fluente
    
    print()
    biblioteca.estatisticas()
    
    print("\n🔍 Testando busca:")
    print("-" * 20)
    biblioteca.buscar_livro("machado")
    biblioteca.buscar_livro("python")
    
    print("\n📚 Status dos usuários:")
    print("-" * 25)
    for usuario in usuarios:
        usuario.listar_livros_emprestados()
    
    print("\n🔄 Devolvendo livros:")
    print("-" * 20)
    usuarios[0].devolver_livro(livros[0])  # Amanda devolve Dom Casmurro
    
    print()
    biblioteca.estatisticas()


if __name__ == "__main__":
    main()