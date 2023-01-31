# Batalha Naval
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

Este projeto tem como objetivo a execução do clássico jogo "Batalha Naval" de maneira interativa pelo terminal.

Conteúdo:
- Tecnologias
- Instalação/Execução
- Instruções
- Autores
- Organização do projeto
- License

## Tecnologias
Esse projeto utiliza as seguintes bibliotecas:

- ...

## Instalação/Execução
Foi utilizado o [Python](https://www.python.org/) v3.10.9.

### Conda
No desenvolvimento foi utilizado o gerenciador de pacotes e ambientes [Conda](https://conda.io/). Portanto para prosseguir necessita-se de sua [instalação](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
conda env create -f environment.yml
```

- Ativar
```sh
conda activate naval_battle_venv
```

- Desativar
```sh
conda deactivate
```

### Requirements
Pode-se utilizar o arquivo requirements.txt para criar o ambiente virtual.

- Criar ambiente virtual
```sh
python -m venv naval_battle_venv
```

- Ativar
```sh
source ./naval_battle_venv/bin/activate
```

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
pip install -r requirements.txt
```

- Desativar
```sh
deactivate
```

### Execução
- Navegar até a pasta de destino
```sh
cd naval_battle
```

- Execute o programa
```sh
python __init__.py
```

## Instruções


## Autores
Projeto desenvolvido pelo Dev:

- [Matheus Miranda Brandão](https://github.com/MatBrands)

## Organização do projeto
```sh
...
```

## License
MIT