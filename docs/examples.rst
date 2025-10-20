Exemplos Avançados
==================

Esta seção contém exemplos práticos e casos de uso avançados do Sistema de Biblioteca.

Exemplo 1: Biblioteca Escolar Completa
---------------------------------------

.. code-block:: python

    from src.biblioteca_melhorada import Biblioteca, Livro, Usuario
    from datetime import datetime

    def criar_biblioteca_escolar():
        """Exemplo de biblioteca escolar com dados realistas."""
        
        # 1. Criar biblioteca
        biblioteca = Biblioteca("Biblioteca Escola João XXIII")
        
        # 2. Adicionar acervo diversificado
        livros_literatura = [
            Livro("Dom Casmurro", "Machado de Assis", 1899, "978-85-254-1234-5"),
            Livro("O Cortiço", "Aluísio Azevedo", 1890, "978-85-254-5678-9"),
            Livro("Iracema", "José de Alencar", 1865, "978-85-254-9012-3"),
            Livro("O Guarani", "José de Alencar", 1857, "978-85-254-4567-8")
        ]
        
        livros_tecnicos = [
            Livro("Clean Code", "Robert C. Martin", 2008, "978-01-321-5063-2"),
            Livro("Python Fluente", "Luciano Ramalho", 2015, "978-85-7522-462-7"),
            Livro("Algoritmos", "Thomas H. Cormen", 2009, "978-85-352-3699-6"),
            Livro("Padrões de Projeto", "Gamma et al", 1994, "978-85-7522-166-4")
        ]
        
        livros_didaticos = [
            Livro("Matemática Volume 1", "Gelson Iezzi", 2016, "978-85-422-0123-4"),
            Livro("Física Moderna", "Halliday & Resnick", 2018, "978-85-216-2345-6"),
            Livro("Química Orgânica", "John McMurry", 2017, "978-85-221-3456-7")
        ]
        
        # Adicionar todos os livros
        todos_livros = livros_literatura + livros_tecnicos + livros_didaticos
        for livro in todos_livros:
            biblioteca.adicionar_livro(livro)
        
        print(f"📚 Acervo criado com {len(todos_livros)} livros")
        
        # 3. Registrar diferentes tipos de usuários
        professores = [
            Usuario("Prof. Ana Santos", "ana.santos@escola.edu.br"),
            Usuario("Prof. Carlos Lima", "carlos.lima@escola.edu.br"),
            Usuario("Prof. Maria Silva", "maria.silva@escola.edu.br")
        ]
        
        alunos = [
            Usuario("João Pedro (9º A)", "joao.pedro@aluno.edu.br"),
            Usuario("Maria Eduarda (8º B)", "maria.eduarda@aluno.edu.br"),
            Usuario("Lucas Oliveira (7º C)", "lucas.oliveira@aluno.edu.br"),
            Usuario("Ana Clara (9º A)", "ana.clara@aluno.edu.br"),
            Usuario("Pedro Henrique (8º A)", "pedro.henrique@aluno.edu.br")
        ]
        
        # Registrar usuários
        for professor in professores:
            biblioteca.registrar_usuario(professor)
        
        for aluno in alunos:
            biblioteca.registrar_usuario(aluno)
        
        print(f"👥 Registrados {len(professores)} professores e {len(alunos)} alunos")
        
        return biblioteca, todos_livros, professores, alunos

    def simular_semana_letiva(biblioteca, livros, professores, alunos):
        """Simula uma semana de empréstimos e devoluções."""
        
        print("\n📅 SIMULANDO SEMANA LETIVA")
        print("=" * 40)
        
        # Segunda-feira: Professores preparam aulas
        print("\n🗓️  Segunda-feira - Professores preparando aulas:")
        professores[0].pegar_livro(livros[4])  # Prof Ana - Clean Code
        professores[1].pegar_livro(livros[8])  # Prof Carlos - Matemática
        professores[2].pegar_livro(livros[9])  # Prof Maria - Física
        
        # Terça-feira: Alunos começam pesquisas
        print("\n🗓️  Terça-feira - Alunos fazendo pesquisas:")
        alunos[0].pegar_livro(livros[0])  # João - Dom Casmurro
        alunos[1].pegar_livro(livros[1])  # Maria Eduarda - O Cortiço
        alunos[2].pegar_livro(livros[2])  # Lucas - Iracema
        
        # Quarta-feira: Mais empréstimos
        print("\n🗓️  Quarta-feira - Continuando empréstimos:")
        alunos[3].pegar_livro(livros[5])  # Ana Clara - Python Fluente
        alunos[4].pegar_livro(livros[6])  # Pedro - Algoritmos
        
        # Quinta-feira: Alguns alunos tentam pegar mais livros
        print("\n🗓️  Quinta-feira - Tentativas de novos empréstimos:")
        alunos[0].pegar_livro(livros[3])  # João tenta pegar outro
        alunos[1].pegar_livro(livros[7])  # Maria Eduarda - Padrões de Projeto
        
        # Sexta-feira: Devoluções começam
        print("\n🗓️  Sexta-feira - Primeiras devoluções:")
        professores[0].devolver_livro(livros[4])  # Prof Ana devolve Clean Code
        alunos[2].devolver_livro(livros[2])      # Lucas devolve Iracema
        
        # Status da biblioteca no final da semana
        print("\n📊 STATUS NO FINAL DA SEMANA:")
        biblioteca.estatisticas()

    # Executar exemplo
    if __name__ == "__main__":
        bib, livros, profs, estudantes = criar_biblioteca_escolar()
        simular_semana_letiva(bib, livros, profs, estudantes)

Exemplo 2: Sistema de Busca Avançada
-------------------------------------

.. code-block:: python

    def sistema_busca_avancada():
        """Demonstra funcionalidades avançadas de busca."""
        
        biblioteca = Biblioteca("Biblioteca Técnica")
        
        # Criar acervo técnico
        livros_python = [
            Livro("Python Fluente", "Luciano Ramalho", 2015),
            Livro("Effective Python", "Brett Slatkin", 2019),
            Livro("Python Tricks", "Dan Bader", 2017),
            Livro("Automate Python", "Al Sweigart", 2019)
        ]
        
        livros_outros = [
            Livro("Clean Code", "Robert Martin", 2008),
            Livro("Clean Architecture", "Robert Martin", 2017),
            Livro("JavaScript Eloquente", "Marijn Haverbeke", 2018),
            Livro("Algoritmos em C", "Robert Sedgewick", 2011)
        ]
        
        for livro in livros_python + livros_outros:
            biblioteca.adicionar_livro(livro)
        
        # Demonstrar diferentes tipos de busca
        print("🔍 DEMONSTRAÇÃO DE BUSCA AVANÇADA")
        print("=" * 50)
        
        # Busca por linguagem
        print("\n📖 Busca por 'python':")
        resultado_python = biblioteca.buscar_livro("python")
        
        print(f"\n📖 Busca por 'robert' (autor):")
        resultado_robert = biblioteca.buscar_livro("robert")
        
        print(f"\n📖 Busca por 'clean' (série):")
        resultado_clean = biblioteca.buscar_livro("clean")
        
        print(f"\n📖 Busca por termo inexistente:")
        resultado_vazio = biblioteca.buscar_livro("php")
        
        return biblioteca

    def busca_com_filtros_customizados(biblioteca):
        """Exemplo de filtros personalizados (extensão do sistema)."""
        
        def buscar_por_ano(biblioteca, ano_inicio, ano_fim=None):
            """Busca livros por intervalo de anos."""
            if ano_fim is None:
                ano_fim = ano_inicio
            
            encontrados = [
                livro for livro in biblioteca.livros 
                if ano_inicio <= livro.ano <= ano_fim
            ]
            
            print(f"\n📅 Livros entre {ano_inicio}-{ano_fim}:")
            if encontrados:
                for livro in encontrados:
                    print(f"  • {livro}")
            else:
                print("  Nenhum livro encontrado no período")
            
            return encontrados
        
        def buscar_disponiveis(biblioteca):
            """Busca apenas livros disponíveis."""
            disponiveis = [
                livro for livro in biblioteca.livros 
                if livro.disponivel
            ]
            
            print(f"\n✅ Livros disponíveis ({len(disponiveis)}):")
            for livro in disponiveis:
                print(f"  • {livro}")
            
            return disponiveis
        
        # Usar filtros customizados
        print("\n🎯 FILTROS PERSONALIZADOS")
        print("=" * 30)
        
        buscar_por_ano(biblioteca, 2015, 2020)
        buscar_por_ano(biblioteca, 2008)
        buscar_disponiveis(biblioteca)

Exemplo 3: Relatórios e Analytics
----------------------------------

.. code-block:: python

    def gerar_relatorios_avancados(biblioteca):
        """Gera relatórios detalhados da biblioteca."""
        
        def relatorio_utilizacao():
            """Relatório de utilização por categoria."""
            
            print("\n📈 RELATÓRIO DE UTILIZAÇÃO")
            print("=" * 40)
            
            total_livros = len(biblioteca.livros)
            total_usuarios = len(biblioteca.usuarios)
            total_emprestimos = sum(
                len(usuario.livros_emprestados) 
                for usuario in biblioteca.usuarios
            )
            
            print(f"📊 Métricas Gerais:")
            print(f"  • Total de livros: {total_livros}")
            print(f"  • Total de usuários: {total_usuarios}")
            print(f"  • Total de empréstimos ativos: {total_emprestimos}")
            
            if total_livros > 0:
                taxa_utilizacao = (total_emprestimos / total_livros) * 100
                print(f"  • Taxa de utilização: {taxa_utilizacao:.1f}%")
            
            # Ranking de usuários mais ativos
            usuarios_ordenados = sorted(
                biblioteca.usuarios,
                key=lambda u: len(u.livros_emprestados),
                reverse=True
            )
            
            print(f"\n👥 Top 3 Usuários Mais Ativos:")
            for i, usuario in enumerate(usuarios_ordenados[:3], 1):
                qtd_livros = len(usuario.livros_emprestados)
                print(f"  {i}. {usuario.nome} - {qtd_livros} livro(s)")
        
        def relatorio_acervo():
            """Relatório do acervo por década."""
            
            from collections import defaultdict
            
            print(f"\n📚 RELATÓRIO DO ACERVO")
            print("=" * 30)
            
            # Agrupar por década
            por_decada = defaultdict(list)
            for livro in biblioteca.livros:
                decada = (livro.ano // 10) * 10
                por_decada[decada].append(livro)
            
            # Mostrar por década
            for decada in sorted(por_decada.keys()):
                livros_decada = por_decada[decada]
                disponiveis = sum(1 for l in livros_decada if l.disponivel)
                
                print(f"\n📅 Década de {decada}:")
                print(f"  • Total: {len(livros_decada)} livros")
                print(f"  • Disponíveis: {disponiveis}")
                print(f"  • Emprestados: {len(livros_decada) - disponiveis}")
                
                # Mostrar alguns títulos
                print("  • Títulos:")
                for livro in livros_decada[:3]:  # Primeiros 3
                    status = "📗" if livro.disponivel else "📕"
                    print(f"    {status} {livro.titulo} ({livro.autor})")
                
                if len(livros_decada) > 3:
                    print(f"    ... e mais {len(livros_decada) - 3} livro(s)")
        
        def relatorio_emprestimos():
            """Relatório detalhado de empréstimos."""
            
            print(f"\n🔄 RELATÓRIO DE EMPRÉSTIMOS")
            print("=" * 35)
            
            emprestimos_ativos = []
            for usuario in biblioteca.usuarios:
                for livro in usuario.livros_emprestados:
                    if livro.data_emprestimo:
                        dias = (datetime.now() - livro.data_emprestimo).days
                        emprestimos_ativos.append({
                            'usuario': usuario.nome,
                            'livro': livro.titulo,
                            'autor': livro.autor,
                            'dias': dias
                        })
            
            if not emprestimos_ativos:
                print("  Nenhum empréstimo ativo no momento.")
                return
            
            # Ordenar por dias de empréstimo
            emprestimos_ativos.sort(key=lambda x: x['dias'], reverse=True)
            
            print(f"  Total de empréstimos ativos: {len(emprestimos_ativos)}")
            print(f"\n  📋 Detalhes:")
            
            for emp in emprestimos_ativos:
                status_emoji = "🟡" if emp['dias'] <= 7 else "🟠" if emp['dias'] <= 14 else "🔴"
                print(f"  {status_emoji} {emp['livro']} - {emp['usuario']} ({emp['dias']} dias)")
        
        # Gerar todos os relatórios
        relatorio_utilizacao()
        relatorio_acervo()
        relatorio_emprestimos()

    # Executar exemplo completo
    if __name__ == "__main__":
        # Usar biblioteca do exemplo anterior
        biblioteca = sistema_busca_avancada()
        busca_com_filtros_customizados(biblioteca)
        gerar_relatorios_avancados(biblioteca)

Exemplo 4: Extensão do Sistema
------------------------------

.. code-block:: python

    class BibliotecaExtendida(Biblioteca):
        """Versão estendida com funcionalidades extras."""
        
        def __init__(self, nome: str):
            super().__init__(nome)
            self.historico_emprestimos = []
            self.reservas = {}
        
        def reservar_livro(self, usuario: Usuario, livro: Livro) -> bool:
            """Permite reservar livro emprestado."""
            
            if livro.disponivel:
                print(f"📚 Livro '{livro.titulo}' está disponível! Empreste diretamente.")
                return False
            
            if livro in self.reservas:
                print(f"📋 Livro '{livro.titulo}' já possui reserva.")
                return False
            
            self.reservas[livro] = usuario
            print(f"✅ Livro '{livro.titulo}' reservado para {usuario.nome}")
            return True
        
        def devolver_com_reserva(self, usuario: Usuario, livro: Livro) -> bool:
            """Devolve livro e processa reserva automaticamente."""
            
            if not usuario.devolver_livro(livro):
                return False
            
            # Verificar se há reserva
            if livro in self.reservas:
                proximo_usuario = self.reservas.pop(livro)
                print(f"🔄 Processando reserva para {proximo_usuario.nome}")
                
                if proximo_usuario.pegar_livro(livro):
                    print(f"✅ Empréstimo automático realizado!")
                else:
                    print(f"❌ Não foi possível emprestar automaticamente")
            
            return True
        
        def relatorio_reservas(self):
            """Mostra todas as reservas pendentes."""
            
            print(f"\n📋 RESERVAS PENDENTES ({len(self.reservas)})")
            print("=" * 30)
            
            if not self.reservas:
                print("  Nenhuma reserva pendente.")
                return
            
            for livro, usuario in self.reservas.items():
                print(f"  📖 {livro.titulo} → {usuario.nome}")

    def exemplo_sistema_estendido():
        """Demonstra funcionalidades estendidas."""
        
        biblioteca = BibliotecaExtendida("Biblioteca Moderna")
        
        # Setup básico
        livro1 = Livro("Design Patterns", "Gang of Four", 1994)
        livro2 = Livro("Refactoring", "Martin Fowler", 2018)
        
        usuario1 = Usuario("Alice", "alice@dev.com")
        usuario2 = Usuario("Bob", "bob@dev.com")
        usuario3 = Usuario("Carol", "carol@dev.com")
        
        biblioteca.adicionar_livro(livro1)
        biblioteca.adicionar_livro(livro2)
        biblioteca.registrar_usuario(usuario1)
        biblioteca.registrar_usuario(usuario2)
        biblioteca.registrar_usuario(usuario3)
        
        # Demonstrar funcionalidades
        print("🚀 SISTEMA ESTENDIDO EM AÇÃO")
        print("=" * 35)
        
        # Alice pega livro
        print("\n1. Alice empresta Design Patterns:")
        usuario1.pegar_livro(livro1)
        
        # Bob tenta pegar o mesmo livro (vai reservar)
        print("\n2. Bob tenta pegar o mesmo livro:")
        biblioteca.reservar_livro(usuario2, livro1)
        
        # Carol também tenta reservar
        print("\n3. Carol tenta reservar também:")
        biblioteca.reservar_livro(usuario3, livro1)
        
        # Ver reservas
        biblioteca.relatorio_reservas()
        
        # Alice devolve (Bob pega automaticamente)
        print("\n4. Alice devolve o livro:")
        biblioteca.devolver_com_reserva(usuario1, livro1)
        
        # Ver status final
        biblioteca.relatorio_reservas()
        biblioteca.estatisticas()

    if __name__ == "__main__":
        exemplo_sistema_estendido()

Exemplo 5: Integração e Testes
-------------------------------

.. code-block:: python

    def teste_integracao_completa():
        """Teste de integração que simula uso real."""
        
        print("🧪 TESTE DE INTEGRAÇÃO COMPLETA")
        print("=" * 40)
        
        # Setup
        biblioteca = Biblioteca("Biblioteca de Testes")
        
        # Cenário 1: Cadastro em massa
        print("\n📋 Cenário 1: Cadastro em Massa")
        
        livros_teste = [
            ("Livro A", "Autor 1", 2020),
            ("Livro B", "Autor 2", 2021), 
            ("Livro C", "Autor 1", 2022),
            ("Livro D", "Autor 3", 2023),
            ("Livro E", "Autor 2", 2024)
        ]
        
        for titulo, autor, ano in livros_teste:
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
        
        usuarios_teste = [
            ("Usuário A", "a@test.com"),
            ("Usuário B", "b@test.com"),
            ("Usuário C", None)
        ]
        
        for nome, email in usuarios_teste:
            usuario = Usuario(nome, email) if email else Usuario(nome)
            biblioteca.registrar_usuario(usuario)
        
        print(f"✅ Cadastrados {len(livros_teste)} livros e {len(usuarios_teste)} usuários")
        
        # Cenário 2: Empréstimos simultâneos
        print("\n📋 Cenário 2: Empréstimos Simultâneos")
        
        biblioteca.usuarios[0].pegar_livro(biblioteca.livros[0])
        biblioteca.usuarios[0].pegar_livro(biblioteca.livros[1])
        biblioteca.usuarios[1].pegar_livro(biblioteca.livros[2])
        biblioteca.usuarios[2].pegar_livro(biblioteca.livros[3])
        
        # Cenário 3: Tentativas de erro
        print("\n📋 Cenário 3: Tratamento de Erros")
        
        # Tentativa de pegar livro já emprestado
        resultado = biblioteca.usuarios[1].pegar_livro(biblioteca.livros[0])
        assert not resultado, "Deveria falhar - livro já emprestado"
        
        # Tentativa de exceder limite
        biblioteca.usuarios[0].pegar_livro(biblioteca.livros[4])  # 3º livro - OK
        resultado = biblioteca.usuarios[0].pegar_livro(biblioteca.livros[4])  # Já tem este
        
        # Cenário 4: Buscas diversas
        print("\n📋 Cenário 4: Funcionalidade de Busca")
        
        busca1 = biblioteca.buscar_livro("Autor 1")
        busca2 = biblioteca.buscar_livro("Livro")
        busca3 = biblioteca.buscar_livro("inexistente")
        
        assert len(busca1) == 2, f"Esperado 2, obtido {len(busca1)}"
        assert len(busca2) == 5, f"Esperado 5, obtido {len(busca2)}"
        assert len(busca3) == 0, f"Esperado 0, obtido {len(busca3)}"
        
        # Cenário 5: Status final
        print("\n📋 Cenário 5: Verificação Final")
        biblioteca.estatisticas()
        
        # Validações finais
        total_emprestados = sum(
            len(u.livros_emprestados) for u in biblioteca.usuarios
        )
        
        livros_nao_disponiveis = sum(
            1 for l in biblioteca.livros if not l.disponivel
        )
        
        assert total_emprestados == livros_nao_disponiveis, \
            "Inconsistência: empréstimos != livros indisponíveis"
        
        print("✅ Todos os testes de integração passaram!")
        
        return biblioteca

    if __name__ == "__main__":
        teste_integracao_completa()

Executando os Exemplos
-----------------------

Para executar qualquer exemplo:

.. code-block:: bash

    # Salve o código em um arquivo (ex: exemplo1.py)
    python exemplo1.py
    
    # Ou execute interativamente
    python -i exemplo1.py

Cada exemplo demonstra aspectos diferentes do sistema:

* **Exemplo 1**: Caso de uso real (escola)
* **Exemplo 2**: Funcionalidades de busca
* **Exemplo 3**: Relatórios e analytics  
* **Exemplo 4**: Extensão do sistema base
* **Exemplo 5**: Testes de integração

Estes exemplos mostram a flexibilidade e robustez do sistema para diferentes cenários de uso.