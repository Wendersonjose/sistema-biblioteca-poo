Guia Rápido
============

Este guia mostra como usar o Sistema de Biblioteca em poucos minutos.

Primeiro Uso
------------

1. **Importe as classes principais**:

.. code-block:: python

    from src.biblioteca_melhorada import Biblioteca, Livro, Usuario

2. **Crie uma biblioteca**:

.. code-block:: python

    biblioteca = Biblioteca("Biblioteca Municipal")

3. **Adicione alguns livros**:

.. code-block:: python

    # Livros clássicos
    livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro2 = Livro("O Cortiço", "Aluísio Azevedo", 1890)
    
    # Livros técnicos
    livro3 = Livro("Clean Code", "Robert Martin", 2008, "978-0132350884")
    
    # Adicione à biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

4. **Registre usuários**:

.. code-block:: python

    usuario1 = Usuario("Ana Silva", "ana@email.com")
    usuario2 = Usuario("Carlos Santos")
    
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

5. **Realize empréstimos**:

.. code-block:: python

    # Ana pega emprestado Clean Code
    usuario1.pegar_livro(livro3)
    
    # Carlos tenta pegar o mesmo livro (vai falhar)
    usuario2.pegar_livro(livro3)

6. **Consulte informações**:

.. code-block:: python

    # Liste o catálogo
    biblioteca.listar_livros()
    
    # Veja estatísticas
    biblioteca.estatisticas()
    
    # Busque por autor
    resultados = biblioteca.buscar_livro("machado")

Exemplo Completo
----------------

.. code-block:: python

    from src.biblioteca_melhorada import Biblioteca, Livro, Usuario

    def exemplo_basico():
        # 1. Criar biblioteca
        biblioteca = Biblioteca("Biblioteca Central")
        print("✅ Biblioteca criada!")
        
        # 2. Adicionar livros
        livros = [
            Livro("1984", "George Orwell", 1949),
            Livro("Clean Code", "Robert Martin", 2008),
            Livro("Python Fluente", "Luciano Ramalho", 2015)
        ]
        
        for livro in livros:
            biblioteca.adicionar_livro(livro)
        
        print(f"✅ {len(livros)} livros adicionados!")
        
        # 3. Registrar usuários
        usuarios = [
            Usuario("Maria Santos", "maria@email.com"),
            Usuario("João Oliveira")
        ]
        
        for usuario in usuarios:
            biblioteca.registrar_usuario(usuario)
        
        print(f"✅ {len(usuarios)} usuários registrados!")
        
        # 4. Demonstrar empréstimos
        print("\n📚 Realizando empréstimos...")
        usuarios[0].pegar_livro(livros[0])  # Maria pega 1984
        usuarios[1].pegar_livro(livros[1])  # João pega Clean Code
        
        # 5. Mostrar estatísticas
        print("\n📊 Estatísticas:")
        biblioteca.estatisticas()
        
        # 6. Buscar livros
        print("\n🔍 Buscando 'python':")
        resultados = biblioteca.buscar_livro("python")
        
        # 7. Devolver livro
        print("\n🔄 Devolvendo livro:")
        usuarios[0].devolver_livro(livros[0])
        
        return biblioteca

    if __name__ == "__main__":
        biblioteca = exemplo_basico()

Funcionalidades Principais
---------------------------

Gestão de Livros
~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Criar livro com validações automáticas
    livro = Livro(
        titulo="Clean Architecture",
        autor="Robert Martin", 
        ano=2017,
        isbn="978-0134494166"  # Opcional
    )
    
    # Verificar disponibilidade
    if livro.disponivel:
        print("Livro está disponível!")
    
    # Ver representação
    print(livro)  # Clean Architecture (2017) - Robert Martin | Status: Disponível

Gestão de Usuários
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Criar usuário
    usuario = Usuario("Ana Silva", "ana@email.com")
    
    # Verificar limite de livros
    print(f"Limite: {usuario.limite_livros}")  # 3 por padrão
    
    # Ver livros emprestados
    usuario.listar_livros_emprestados()
    
    # Representação do usuário
    print(usuario)  # Ana Silva (2/3 livros)

Gestão da Biblioteca
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    biblioteca = Biblioteca("Minha Biblioteca")
    
    # Busca inteligente (case-insensitive)
    resultados = biblioteca.buscar_livro("PYTHON")  # Encontra "Python Fluente"
    
    # Estatísticas detalhadas
    biblioteca.estatisticas()
    # 📚 Total de livros: 10
    # ✅ Livros disponíveis: 7
    # 📤 Livros emprestados: 3
    # 👥 Usuários registrados: 5
    # 📈 Taxa de utilização: 30.0%

Validações e Tratamento de Erros
---------------------------------

O sistema possui validações robustas:

.. code-block:: python

    # Estas operações vão gerar erros apropriados:
    
    try:
        # Título vazio
        Livro("", "Autor", 2020)
    except ValueError as e:
        print(f"Erro: {e}")  # Erro: Título não pode estar vazio
    
    try:
        # Ano inválido
        Livro("Título", "Autor", -100)
    except ValueError as e:
        print(f"Erro: {e}")  # Erro: Ano inválido para o livro
    
    try:
        # Usuário sem nome
        Usuario("")
    except ValueError as e:
        print(f"Erro: {e}")  # Erro: Nome não pode estar vazio

Próximos Passos
---------------

Agora que você conhece o básico, explore:

* :doc:`api` - Documentação completa da API
* :doc:`examples` - Exemplos avançados
* :doc:`contributing` - Como contribuir
* **Testes** - Execute ``pytest tests/ -v`` para ver todos os testes