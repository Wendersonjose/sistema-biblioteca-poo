Instalação
==========

Requisitos
----------

* Python 3.8 ou superior
* pip (gerenciador de pacotes Python)

Instalação via pip
-------------------

.. code-block:: bash

    # Clone o repositório
    git clone https://github.com/Wendersonjose/sistema-biblioteca-poo.git
    cd sistema-biblioteca-poo
    
    # Crie um ambiente virtual (recomendado)
    python -m venv venv
    
    # Ative o ambiente virtual
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
    
    # Instale as dependências
    pip install -r requirements.txt

Instalação para Desenvolvimento
--------------------------------

Se você deseja contribuir com o projeto:

.. code-block:: bash

    # Instale dependências de desenvolvimento
    pip install -r requirements.txt
    pip install -e .
    
    # Configure pre-commit hooks (opcional)
    pre-commit install

Verificando a Instalação
-------------------------

Para verificar se tudo foi instalado corretamente:

.. code-block:: bash

    # Execute o programa principal
    python src/biblioteca_melhorada.py
    
    # Execute os testes
    pytest tests/ -v

Ambiente Virtual
----------------

É altamente recomendado usar um ambiente virtual para isolar as dependências:

.. code-block:: bash

    # Criar ambiente virtual
    python -m venv biblioteca_env
    
    # Ativar (Windows)
    biblioteca_env\Scripts\activate
    
    # Ativar (Linux/Mac)
    source biblioteca_env/bin/activate
    
    # Desativar quando terminar
    deactivate

Dependências
------------

As principais dependências incluem:

* **pytest** - Framework de testes
* **pytest-cov** - Cobertura de código
* **black** - Formatação de código
* **flake8** - Análise estática
* **mypy** - Verificação de tipos

Para ver a lista completa, consulte o arquivo ``requirements.txt``.