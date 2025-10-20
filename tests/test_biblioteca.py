"""
Testes unitários para o Sistema de Biblioteca
Demonstra conhecimento em testes e pytest
"""

import pytest
import sys
import os
from datetime import datetime

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from biblioteca_melhorada import Livro, Usuario, Biblioteca


class TestLivro:
    """Testes para a classe Livro."""
    
    def test_criar_livro_valido(self):
        """Teste criação de livro válido."""
        livro = Livro("1984", "George Orwell", 1949)
        assert livro.titulo == "1984"
        assert livro.autor == "George Orwell"
        assert livro.ano == 1949
        assert livro.disponivel is True
        assert livro.data_emprestimo is None
    
    def test_criar_livro_com_isbn(self):
        """Teste criação de livro com ISBN."""
        livro = Livro("Clean Code", "Robert Martin", 2008, "978-0132350884")
        assert livro.isbn == "978-0132350884"
    
    def test_titulo_vazio_deve_falhar(self):
        """Teste validação de título vazio."""
        with pytest.raises(ValueError, match="Título não pode estar vazio"):
            Livro("", "Autor", 2000)
    
    def test_autor_vazio_deve_falhar(self):
        """Teste validação de autor vazio."""
        with pytest.raises(ValueError, match="Autor não pode estar vazio"):
            Livro("Título", "", 2000)
    
    def test_ano_invalido_deve_falhar(self):
        """Teste validação de ano inválido."""
        with pytest.raises(ValueError, match="Ano inválido"):
            Livro("Título", "Autor", -1)
        
        with pytest.raises(ValueError, match="Ano inválido"):
            Livro("Título", "Autor", 3000)
    
    def test_emprestar_livro_disponivel(self):
        """Teste empréstimo de livro disponível."""
        livro = Livro("1984", "George Orwell", 1949)
        resultado = livro.emprestar()
        
        assert resultado is True
        assert livro.disponivel is False
        assert livro.data_emprestimo is not None
        assert isinstance(livro.data_emprestimo, datetime)
    
    def test_emprestar_livro_indisponivel(self):
        """Teste empréstimo de livro já emprestado."""
        livro = Livro("1984", "George Orwell", 1949)
        livro.emprestar()  # Primeiro empréstimo
        
        resultado = livro.emprestar()  # Segundo empréstimo
        assert resultado is False
    
    def test_devolver_livro(self):
        """Teste devolução de livro."""
        livro = Livro("1984", "George Orwell", 1949)
        livro.emprestar()
        livro.devolver()
        
        assert livro.disponivel is True
        assert livro.data_emprestimo is None
    
    def test_str_representation(self):
        """Teste representação em string."""
        livro = Livro("1984", "George Orwell", 1949)
        esperado = "1984 (1949) - George Orwell | Status: Disponível"
        assert str(livro) == esperado


class TestUsuario:
    """Testes para a classe Usuario."""
    
    def test_criar_usuario_valido(self):
        """Teste criação de usuário válido."""
        usuario = Usuario("João Silva", "joao@email.com")
        assert usuario.nome == "João Silva"
        assert usuario.email == "joao@email.com"
        assert usuario.livros_emprestados == []
        assert usuario.limite_livros == 3
    
    def test_nome_vazio_deve_falhar(self):
        """Teste validação de nome vazio."""
        with pytest.raises(ValueError, match="Nome não pode estar vazio"):
            Usuario("")
    
    def test_pegar_livro_disponivel(self, capsys):
        """Teste empréstimo de livro disponível."""
        usuario = Usuario("João")
        livro = Livro("1984", "George Orwell", 1949)
        
        resultado = usuario.pegar_livro(livro)
        captured = capsys.readouterr()
        
        assert resultado is True
        assert livro in usuario.livros_emprestados
        assert "✅ João emprestou '1984'" in captured.out
    
    def test_pegar_livro_indisponivel(self, capsys):
        """Teste empréstimo de livro indisponível."""
        usuario1 = Usuario("João")
        usuario2 = Usuario("Maria")
        livro = Livro("1984", "George Orwell", 1949)
        
        usuario1.pegar_livro(livro)  # João pega primeiro
        resultado = usuario2.pegar_livro(livro)  # Maria tenta pegar
        captured = capsys.readouterr()
        
        assert resultado is False
        assert livro not in usuario2.livros_emprestados
        assert "❌ O livro '1984' não está disponível" in captured.out
    
    def test_limite_livros(self, capsys):
        """Teste limite de livros por usuário."""
        usuario = Usuario("João")
        livros = [
            Livro(f"Livro {i}", "Autor", 2000) 
            for i in range(5)
        ]
        
        # Emprestar até o limite
        for i in range(3):
            resultado = usuario.pegar_livro(livros[i])
            assert resultado is True
        
        # Tentar emprestar além do limite
        resultado = usuario.pegar_livro(livros[3])
        captured = capsys.readouterr()
        
        assert resultado is False
        assert "❌ João atingiu o limite de 3 livros" in captured.out
    
    def test_devolver_livro_emprestado(self, capsys):
        """Teste devolução de livro emprestado."""
        usuario = Usuario("João")
        livro = Livro("1984", "George Orwell", 1949)
        
        usuario.pegar_livro(livro)
        resultado = usuario.devolver_livro(livro)
        captured = capsys.readouterr()
        
        assert resultado is True
        assert livro not in usuario.livros_emprestados
        assert livro.disponivel is True
        assert "✅ João devolveu '1984'" in captured.out
    
    def test_devolver_livro_nao_emprestado(self, capsys):
        """Teste devolução de livro não emprestado."""
        usuario = Usuario("João")
        livro = Livro("1984", "George Orwell", 1949)
        
        resultado = usuario.devolver_livro(livro)
        captured = capsys.readouterr()
        
        assert resultado is False
        assert "❌ João não possui o livro '1984'" in captured.out


class TestBiblioteca:
    """Testes para a classe Biblioteca."""
    
    def test_criar_biblioteca_valida(self):
        """Teste criação de biblioteca válida."""
        biblioteca = Biblioteca("Biblioteca Central")
        assert biblioteca.nome == "Biblioteca Central"
        assert biblioteca.livros == []
        assert biblioteca.usuarios == []
    
    def test_nome_vazio_deve_falhar(self):
        """Teste validação de nome vazio."""
        with pytest.raises(ValueError, match="Nome da biblioteca não pode estar vazio"):
            Biblioteca("")
    
    def test_adicionar_livro(self, capsys):
        """Teste adição de livro."""
        biblioteca = Biblioteca("Biblioteca Central")
        livro = Livro("1984", "George Orwell", 1949)
        
        biblioteca.adicionar_livro(livro)
        captured = capsys.readouterr()
        
        assert livro in biblioteca.livros
        assert "📖 Livro '1984' adicionado ao acervo" in captured.out
    
    def test_registrar_usuario(self, capsys):
        """Teste registro de usuário."""
        biblioteca = Biblioteca("Biblioteca Central")
        usuario = Usuario("João Silva")
        
        biblioteca.registrar_usuario(usuario)
        captured = capsys.readouterr()
        
        assert usuario in biblioteca.usuarios
        assert "👤 Usuário 'João Silva' registrado com sucesso" in captured.out
    
    def test_registrar_usuario_duplicado(self, capsys):
        """Teste registro de usuário duplicado."""
        biblioteca = Biblioteca("Biblioteca Central")
        usuario1 = Usuario("João Silva")
        usuario2 = Usuario("joão silva")  # Caso diferente
        
        biblioteca.registrar_usuario(usuario1)
        biblioteca.registrar_usuario(usuario2)  # Duplicado
        captured = capsys.readouterr()
        
        assert len(biblioteca.usuarios) == 1
        assert "❌ Usuário 'joão silva' já está registrado" in captured.out
    
    def test_buscar_livro_por_titulo(self, capsys):
        """Teste busca de livro por título."""
        biblioteca = Biblioteca("Biblioteca Central")
        livro1 = Livro("1984", "George Orwell", 1949)
        livro2 = Livro("Animal Farm", "George Orwell", 1945)
        
        biblioteca.adicionar_livro(livro1)
        biblioteca.adicionar_livro(livro2)
        
        resultado = biblioteca.buscar_livro("1984")
        captured = capsys.readouterr()
        
        assert len(resultado) == 1
        assert livro1 in resultado
        assert "🔍 Encontrados 1 livro(s):" in captured.out
    
    def test_buscar_livro_por_autor(self, capsys):
        """Teste busca de livro por autor."""
        biblioteca = Biblioteca("Biblioteca Central")
        livro1 = Livro("1984", "George Orwell", 1949)
        livro2 = Livro("Animal Farm", "George Orwell", 1945)
        livro3 = Livro("Dom Casmurro", "Machado de Assis", 1899)
        
        for livro in [livro1, livro2, livro3]:
            biblioteca.adicionar_livro(livro)
        
        resultado = biblioteca.buscar_livro("orwell")
        captured = capsys.readouterr()
        
        assert len(resultado) == 2
        assert livro1 in resultado
        assert livro2 in resultado
        assert "🔍 Encontrados 2 livro(s):" in captured.out
    
    def test_buscar_livro_nao_encontrado(self, capsys):
        """Teste busca de livro não encontrado."""
        biblioteca = Biblioteca("Biblioteca Central")
        livro = Livro("1984", "George Orwell", 1949)
        biblioteca.adicionar_livro(livro)
        
        resultado = biblioteca.buscar_livro("inexistente")
        captured = capsys.readouterr()
        
        assert len(resultado) == 0
        assert "❌ Nenhum livro encontrado com o termo 'inexistente'" in captured.out


# Configuração para executar os testes
if __name__ == "__main__":
    pytest.main([__file__, "-v"])