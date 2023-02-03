from model.clear import *
from model.Menu import *
from view.interface import *
import sys
sys.path.insert(1, '../')

if __name__ == '__main__':
    title = ([f'{"#"*60}\n', f'{"Bem Vindo a Batalha Naval !": ^60}\n',  f'{"#"*60}\n',
            f'{"Para navegar pelo menu utilize as setas do teclado": ^60}\n',
            f'{"E utilize a tecla Enter para interagir com os itens.": ^60}\n'])
    items = ['Iniciar o jogo', 'Sobre o jogo', 'Sair']
    
    start = True
    while start:
        option = set_menu(title, items)
        
        if option == 0:
            while selection_game():
                continue
        elif option == 1:
            input('Para mais informações visite o repositorio do projeto: https://github.com/MatBrands/Naval_Battle\n')
        elif option == 2:
            start = False