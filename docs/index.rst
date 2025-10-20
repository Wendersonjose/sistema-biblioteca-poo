Sistema de Biblioteca
=====================

.. toctree::
   :maxdepth: 2
   :caption: Conteúdo:

   installation
   quickstart
   api
   examples
   contributing
   changelog

Bem-vindo à documentação do Sistema de Biblioteca!

Este é um sistema completo de gerenciamento de biblioteca desenvolvido em Python usando Programação Orientada a Objetos (POO). 

O projeto demonstra boas práticas de desenvolvimento, arquitetura limpa, testes abrangentes e documentação detalhada.

Características Principais
-------------------------

* 🏗️ **Arquitetura Sólida**: Design orientado a objetos com responsabilidades bem definidas
* ✅ **Testes Abrangentes**: Cobertura de 80%+ com pytest
* 📝 **Documentação Completa**: Arquitetura, API e guias de uso
* 🔧 **Ferramentas Modernas**: Type hints, dataclasses, validações robustas
* 📦 **Estrutura Profissional**: Organização de código para projetos reais

Início Rápido
--------------

.. code-block:: python

    from src.biblioteca_melhorada import Biblioteca, Livro, Usuario

    # Criar biblioteca
    biblioteca = Biblioteca("Minha Biblioteca")
    
    # Adicionar livro
    livro = Livro("Clean Code", "Robert Martin", 2008)
    biblioteca.adicionar_livro(livro)
    
    # Registrar usuário
    usuario = Usuario("João Silva")
    biblioteca.registrar_usuario(usuario)
    
    # Emprestar livro
    usuario.pegar_livro(livro)

Índices e Tabelas
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`