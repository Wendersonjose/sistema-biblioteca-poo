# 🚀 Guia de Deploy e DevOps

Este documento fornece instruções completas para deploy e configuração de CI/CD do Sistema de Biblioteca.

## 📋 Pré-requisitos

### Ambiente de Desenvolvimento
- Python 3.8+
- Git
- Docker (opcional)
- VS Code ou IDE similar

### Contas e Serviços
- Conta no GitHub
- Conta no PyPI (para publicação)
- Codecov (para relatórios de cobertura)

## 🔧 Configuração Local

### 1. Setup Inicial
```bash
# Clone o repositório
git clone https://github.com/Wendersonjose/sistema-biblioteca-poo.git
cd sistema-biblioteca-poo

# Crie ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instale dependências
pip install -r requirements.txt
pip install -e .
```

### 2. Configuração de Desenvolvimento
```bash
# Instale ferramentas de desenvolvimento
pip install pre-commit black flake8 mypy

# Configure pre-commit hooks
pre-commit install

# Verifique instalação
python src/biblioteca_melhorada.py
pytest tests/ -v
```

## 🐳 Docker

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de requisitos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fonte
COPY src/ src/
COPY tests/ tests/
COPY docs/ docs/
COPY *.py *.ini *.md *.txt ./

# Instalar pacote
RUN pip install -e .

# Executar testes por padrão
CMD ["pytest", "tests/", "-v"]
```

### Docker Compose
```yaml
version: '3.8'

services:
  biblioteca:
    build: .
    volumes:
      - .:/app
    environment:
      - PYTHONPATH=/app/src
    ports:
      - "8000:8000"
    
  docs:
    build: .
    command: sphinx-build -b html docs/ docs/_build/
    volumes:
      - ./docs:/app/docs
    ports:
      - "8080:8080"
```

### Comandos Docker
```bash
# Build da imagem
docker build -t biblioteca-sistema .

# Executar testes
docker run --rm biblioteca-sistema

# Executar interativo
docker run -it --rm -v $(pwd):/app biblioteca-sistema /bin/bash

# Com docker-compose
docker-compose up --build
```

## 🚀 CI/CD com GitHub Actions

### Workflow Completo
O arquivo `.github/workflows/ci.yml` já está configurado com:

- **Testes multi-versão**: Python 3.8, 3.9, 3.10, 3.11
- **Análise de código**: flake8, mypy
- **Cobertura**: pytest-cov + Codecov
- **Segurança**: bandit, safety
- **Build**: Construção do pacote

### Configuração de Secrets

No GitHub, configure os seguintes secrets:

```bash
# Repository → Settings → Secrets and variables → Actions

CODECOV_TOKEN=<seu-token-codecov>
PYPI_API_TOKEN=<seu-token-pypi>
```

### Badge Status

Adicione badges no README:
```markdown
[![Tests](https://github.com/usuario/repo/workflows/CI/badge.svg)](https://github.com/usuario/repo/actions)
[![Coverage](https://codecov.io/gh/usuario/repo/branch/main/graph/badge.svg)](https://codecov.io/gh/usuario/repo)
[![PyPI version](https://badge.fury.io/py/sistema-biblioteca.svg)](https://badge.fury.io/py/sistema-biblioteca)
```

## 📦 Publicação no PyPI

### 1. Preparação
```bash
# Instalar ferramentas de build
pip install build twine

# Limpar builds anteriores
rm -rf dist/ build/ *.egg-info/
```

### 2. Build do Pacote
```bash
# Gerar distribuições
python -m build

# Verificar pacotes gerados
ls dist/
# sistema-biblioteca-1.0.0.tar.gz
# sistema_biblioteca-1.0.0-py3-none-any.whl
```

### 3. Testes Locais
```bash
# Testar instalação local
pip install dist/sistema_biblioteca-1.0.0-py3-none-any.whl

# Testar funcionamento
python -c "from src.biblioteca_melhorada import Biblioteca; print('OK')"
```

### 4. Upload para TestPyPI
```bash
# Upload para test.pypi.org primeiro
twine upload --repository testpypi dist/*

# Testar instalação do TestPyPI
pip install --index-url https://test.pypi.org/simple/ sistema-biblioteca
```

### 5. Upload para PyPI Oficial
```bash
# Upload final para PyPI
twine upload dist/*

# Verificar no site
# https://pypi.org/project/sistema-biblioteca/
```

## 📊 Monitoramento e Analytics

### Codecov - Cobertura de Código
```yaml
# codecov.yml
coverage:
  status:
    project:
      default:
        target: 80%
        threshold: 2%
    patch:
      default:
        target: 80%

comment:
  layout: "header, diff, flags, files"
  behavior: default
```

### SonarCloud - Qualidade de Código
```yaml
# .github/workflows/sonar.yml
name: SonarCloud Analysis

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  sonarcloud:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
      with:
        fetch-depth: 0
    
    - name: SonarCloud Scan
      uses: SonarSource/sonarcloud-github-action@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

## 🌐 Documentação Online

### GitHub Pages
```yaml
# .github/workflows/docs.yml
name: Deploy Docs

on:
  push:
    branches: [ main ]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.11
    
    - name: Install dependencies
      run: |
        pip install sphinx sphinx-rtd-theme
    
    - name: Build docs
      run: |
        sphinx-build -b html docs/ docs/_build/
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: docs/_build/
```

### Read the Docs
```yaml
# .readthedocs.yml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"

sphinx:
  configuration: docs/conf.py

python:
  install:
    - requirements: requirements.txt
    - method: pip
      path: .
```

## 🚨 Monitoramento de Dependências

### Dependabot
```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    
  - package-ecosystem: "github-actions"
    directory: "/.github/workflows"
    schedule:
      interval: "weekly"
```

### Safety Check
```bash
# Verificar vulnerabilidades
safety check

# Adicionar ao CI
pip install safety
safety check --json
```

## 📈 Performance e Profiling

### Benchmark Simples
```python
# scripts/benchmark.py
import time
import cProfile
from src.biblioteca_melhorada import Biblioteca, Livro, Usuario

def benchmark_sistema():
    """Benchmark básico do sistema."""
    
    biblioteca = Biblioteca("Benchmark")
    
    # Criar muitos livros
    start = time.time()
    for i in range(1000):
        livro = Livro(f"Livro {i}", f"Autor {i}", 2000 + (i % 24))
        biblioteca.adicionar_livro(livro)
    
    tempo_cadastro = time.time() - start
    
    # Buscar livros
    start = time.time()
    for i in range(100):
        biblioteca.buscar_livro(f"Livro {i}")
    
    tempo_busca = time.time() - start
    
    print(f"Cadastro de 1000 livros: {tempo_cadastro:.4f}s")
    print(f"100 buscas: {tempo_busca:.4f}s")

if __name__ == "__main__":
    cProfile.run("benchmark_sistema()")
```

## 🔒 Segurança

### Análise de Segurança
```bash
# Bandit - análise de código
bandit -r src/

# Safety - dependências
safety check

# Adicionar ao pre-commit
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/PyCQA/bandit
    rev: '1.7.5'
    hooks:
      - id: bandit
```

### GitHub Security
```yaml
# .github/workflows/security.yml
name: Security Scan

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Run Bandit Security Scan
      uses: securecodewarrior/github-action-bandit@v1
      with:
        confidence_level: medium
        severity_level: medium
```

## 🎯 Checklist de Deploy

### Pré-Deploy
- [ ] Testes passando (local e CI)
- [ ] Cobertura de código > 80%
- [ ] Documentação atualizada
- [ ] CHANGELOG.md atualizado
- [ ] Versão bumped (setup.py)
- [ ] Secrets configurados

### Deploy
- [ ] Tag de versão criada
- [ ] Build do pacote funcionando
- [ ] Upload para PyPI realizado
- [ ] Documentação publicada
- [ ] Release notes no GitHub

### Pós-Deploy
- [ ] Instalação testada
- [ ] Métricas de uso verificadas
- [ ] Issues reportadas monitoradas
- [ ] Próxima versão planejada

## 🆘 Troubleshooting

### Problemas Comuns

#### Testes falhando no CI
```bash
# Verificar localmente primeiro
pytest tests/ -v --tb=long

# Verificar dependências
pip check

# Testar em ambiente limpo
python -m venv test_env
source test_env/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

#### Build do pacote falhando
```bash
# Limpar arquivos antigos
rm -rf dist/ build/ *.egg-info/

# Verificar setup.py
python setup.py check

# Build verboso
python -m build --verbose
```

#### Documentação não gerando
```bash
# Testar Sphinx localmente
cd docs/
sphinx-build -b html . _build/

# Verificar warnings
sphinx-build -W -b html . _build/
```

## 🔄 Manutenção

### Rotina Semanal
- [ ] Revisar PRs pendentes
- [ ] Verificar issues novas
- [ ] Atualizar dependências
- [ ] Revisar métricas de cobertura

### Rotina Mensal
- [ ] Audit de segurança completo
- [ ] Benchmark de performance
- [ ] Limpeza de branches antigas
- [ ] Planejamento próxima release

### Rotina Trimestral
- [ ] Revisão da arquitetura
- [ ] Atualização da documentação
- [ ] Survey de satisfação dos usuários
- [ ] Roadmap atualizado