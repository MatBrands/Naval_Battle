# Batalha Naval
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

Este projeto tem como objetivo a execução do clássico jogo Batalha Naval de maneira interativa pelo terminal.

Conteúdo:
- Tecnologias
- Instalação/Execução
- Instruções
- Autores
- Organização do projeto
- License

## Tecnologias
Esse projeto utiliza as seguintes bibliotecas:

- python
- os
- pynput
- random
- termcolor

## Instalação/Execução
Foi utilizado o [Python](https://www.python.org/) v3.10.15.

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
O projeto foi todo desenvolvido para ser interativo via teclado com o terminal.
Este jogo possui a regra que as embarcações não podem se tocar na horizontal e vertical.

Para percorrer os menus de opções utilize as 'Setas' do teclado e para selecionar utilize o 'Enter'.
Como o desenvolvimento foi via terminal, utilizando characteres a água é dada pelo token '~', e cada embarcação corresponde a quantidade de casas que ele é posicionado. Ex:. '1', '2' '2', '3' '3' '3', etc.

O jogo possui 3 modalidades diferentes:
- Player vs. Máquina
- Player vs. Player (Local)
- Player vs. Player (Rede)

### Player vs. Máquina
Ao selecionar a quantidade de embarcações elas são posicionadas de maneira aleatória. O jogador possui 3 tiros por tentativa, ao finalizar o turno poderá prosseguir ou encerrar. Finalizando o jogo acertando todas as embarcações ou encerrando é mostrado as tentativas e tiros para o usuário.

### Player vs. Player (Local)
O jogadores poderão optar pela quantidade de embarcações, e então se desejam posiciona-las de maneira automática ou manual.
Automatica: Embarcações posicionadas de maneira aleatória.
Manual: O jogador pode escolher qual embarcação posicionar ao longo do mapa. Caso a posição esteja disponível ficará em VERDE, caso contrário em VERMELHO. Para percorrer o campo utilizar as 'Setas' do teclado, mudar a orientação para vertical ou horizontal com 'Espaço' e selecionar com 'Enter'.

### Player vs. Player (Rede)
Em desenvolvimento ...

## Autores
Projeto desenvolvido pelo Dev:

- [Matheus Miranda Brandão](https://github.com/MatBrands)

## Organização do projeto
```sh
.Naval_Battle
    ├── License
    ├── Readme.md
    ├── naval_battle
    │   ├── __init__.py
    │   ├── controller
    │   │   └── Readme.md
    │   ├── model
    │   │   ├── clear.py
    │   │   ├── Game.py
    │   │   └── Menu.py
    │   └── view
    │       └── interface.py
    └── utils
        ├── environment.yml
        └── requirements.txt
```

## License
MIT