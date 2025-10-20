# Makefile para Sistema de Biblioteca
# Comandos úteis para desenvolvimento

.PHONY: help install test clean lint format run

help: ## Exibe esta ajuda
	@echo "Comandos disponíveis:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Instala dependências do projeto
	pip install -r requirements.txt
	pip install -e .

test: ## Executa os testes
	pytest tests/ -v --cov=src

test-coverage: ## Executa testes com relatório de cobertura
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

lint: ## Verifica qualidade do código
	flake8 src/ tests/
	mypy src/

format: ## Formata o código
	black src/ tests/
	isort src/ tests/

run: ## Executa o programa
	python src/biblioteca_melhorada.py

clean: ## Remove arquivos temporários
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/

setup-dev: install ## Configura ambiente de desenvolvimento
	pre-commit install

build: ## Constrói o pacote
	python setup.py sdist bdist_wheel

docs: ## Gera documentação HTML com Sphinx
	pip install sphinx sphinx-rtd-theme myst-parser
	sphinx-build -b html docs/ docs/_build/
	@echo "Documentação disponível em: docs/_build/index.html"

docs-serve: docs ## Gera e serve documentação localmente
	cd docs/_build && python -m http.server 8080
	@echo "Documentação servindo em: http://localhost:8080"

docs-clean: ## Limpa arquivos de documentação
	rm -rf docs/_build/

notebook: ## Abre tutorial interativo no Jupyter
	pip install jupyter
	jupyter notebook docs/tutorial_interativo.ipynb