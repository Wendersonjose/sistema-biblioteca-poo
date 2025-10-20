# 🤝 Guia de Contribuição

Obrigado por considerar contribuir para o Sistema de Biblioteca! Este documento fornece diretrizes para contribuir com o projeto.

## 📋 Código de Conduta

Este projeto adere a um código de conduta. Ao participar, você concorda em manter um ambiente respeitoso e inclusivo para todos.

## 🚀 Como Contribuir

### 1. Fork e Clone
```bash
# Fork o repositório no GitHub
# Clone seu fork
git clone https://github.com/SEU_USUARIO/sistema-biblioteca-poo.git
cd sistema-biblioteca-poo

# Adicione o repositório original como upstream
git remote add upstream https://github.com/Wendersonjose/sistema-biblioteca-poo.git
```

### 2. Configure o Ambiente
```bash
# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale dependências de desenvolvimento
pip install -r requirements.txt
pip install -e .

# Configure pre-commit hooks (opcional)
pre-commit install
```

### 3. Crie uma Branch
```bash
# Sempre crie uma nova branch para suas mudanças
git checkout -b feature/nome-da-feature
# ou
git checkout -b bugfix/nome-do-bug
# ou
git checkout -b docs/melhoria-documentacao
```

## 📝 Tipos de Contribuição

### 🐛 Reportar Bugs
- Use o template de issue para bugs
- Inclua informações do ambiente (Python version, OS)
- Forneça passos para reproduzir o problema
- Adicione logs de erro, se aplicável

### 💡 Sugerir Melhorias
- Use o template de issue para features
- Explique claramente o problema que resolve
- Descreva a solução proposta
- Considere alternativas

### 🔧 Contribuir com Código
- Siga as convenções de código estabelecidas
- Escreva testes para novas funcionalidades
- Atualize a documentação quando necessário
- Mantenha commits pequenos e focados

## 🎯 Padrões de Desenvolvimento

### Convenções de Código
```python
# Use type hints
def emprestar_livro(self, livro: Livro) -> bool:
    pass

# Docstrings no estilo Google
def buscar_livro(self, termo: str) -> List[Livro]:
    """
    Busca livros por título ou autor.
    
    Args:
        termo: Termo de busca (título ou autor)
        
    Returns:
        Lista de livros encontrados
        
    Raises:
        ValueError: Se termo estiver vazio
    """
    pass

# Use dataclasses quando apropriado
@dataclass
class NovaClasse:
    campo: str
    outro_campo: Optional[int] = None
```

### Formatação
```bash
# Formate o código com black
black src/ tests/

# Verifique estilo com flake8
flake8 src/ tests/

# Verifique tipos com mypy
mypy src/
```

### Testes
```python
# Estrutura de teste
class TestNovaFuncionalidade:
    """Testes para nova funcionalidade."""
    
    def test_caso_sucesso(self):
        """Teste do caso de sucesso."""
        # Arrange
        biblioteca = Biblioteca("Teste")
        
        # Act
        resultado = biblioteca.nova_funcionalidade()
        
        # Assert
        assert resultado is True
    
    def test_caso_erro(self):
        """Teste do caso de erro."""
        with pytest.raises(ValueError, match="Mensagem esperada"):
            funcao_que_deve_falhar()
```

### Commits
```bash
# Use conventional commits
git commit -m "feat: adicionar busca por ISBN"
git commit -m "fix: corrigir validação de ano"
git commit -m "docs: atualizar README com novas features"
git commit -m "test: adicionar testes para classe Usuario"
git commit -m "refactor: simplificar lógica de empréstimo"
```

Tipos de commit:
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação (sem mudança de código)
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Tarefas de manutenção

## ✅ Checklist para Pull Requests

Antes de submeter seu PR, verifique:

- [ ] Código segue os padrões estabelecidos
- [ ] Testes foram escritos e passam
- [ ] Cobertura de código mantida (>80%)
- [ ] Documentação atualizada
- [ ] Commits seguem conventional commits
- [ ] Branch está atualizada com main
- [ ] CI/CD passa sem erros

## 🧪 Executando Testes

```bash
# Todos os testes
pytest tests/ -v

# Com cobertura
pytest tests/ --cov=src --cov-report=html

# Testes específicos
pytest tests/test_biblioteca.py::TestLivro -v

# Testes marcados
pytest tests/ -m "not slow" -v
```

## 📊 Cobertura de Código

Mantemos cobertura mínima de 80%. Para verificar:

```bash
# Gerar relatório
pytest tests/ --cov=src --cov-report=html

# Abrir relatório
open htmlcov/index.html  # Mac
start htmlcov/index.html # Windows
xdg-open htmlcov/index.html # Linux
```

## 📖 Documentação

### Docstrings
- Use o estilo Google para docstrings
- Documente todos os métodos públicos
- Inclua exemplos quando apropriado

### README
- Mantenha atualizado com novas funcionalidades
- Inclua exemplos de uso
- Atualize seção de instalação se necessário

### Arquitetura
- Documente mudanças significativas em `docs/ARCHITECTURE.md`
- Atualize diagramas se necessário

## 🔍 Processo de Review

### Para Mantenedores
1. Verifique se PR segue guidelines
2. Execute testes localmente
3. Revise qualidade do código
4. Verifique documentação
5. Teste funcionalidade manualmente
6. Forneça feedback construtivo

### Para Contribuidores
1. Responda ao feedback prontamente
2. Faça ajustes solicitados
3. Mantenha discussão respeitosa
4. Teste sugestões antes de implementar

## 🎯 Áreas de Contribuição Prioritárias

### Alto Impacto
- [ ] Interface gráfica (Tkinter)
- [ ] Persistência de dados (SQLite)
- [ ] API REST (FastAPI)
- [ ] Melhorias de performance

### Médio Impacto
- [ ] Validações adicionais
- [ ] Relatórios avançados
- [ ] Testes de integração
- [ ] Documentação interativa

### Baixo Impacto
- [ ] Melhorias de UI/UX
- [ ] Otimizações menores
- [ ] Documentação adicional
- [ ] Exemplos de uso

## ❓ Dúvidas?

- Abra uma issue com a tag `question`
- Entre em contato via email: wenderson@email.com
- Consulte a documentação em `docs/`

## 🙏 Reconhecimento

Todos os contribuidores serão reconhecidos:
- Listados no arquivo CONTRIBUTORS.md
- Mencionados nos releases
- Créditos no README principal

Obrigado por contribuir! 🎉