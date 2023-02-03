from model.clear import *
from model.Game import *
from model.Menu import *

def selection_game() -> bool:
    title = 'Selecione a modalidade: '
    items = ['Jogador vs. Máquina', 'Jogador vs. Jogador (Local)', 'Jogador vs. Jogador (Rede)', 'Retornar']
    
    option = set_menu(title, items)
        
    if option == 0:
        bf = Game()
        bf.set_vessel(  set_menu('Selecione a quantidade de embarcações: ', range(1, 11))   +1)
        
        while player_vs_machine(bf):
            continue
    elif option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        return False

    return True

def player_vs_machine(bf: Game) -> bool:
    if bf.shot():
        if set_menu(title = '', items=['Continuar', 'Sair']):
            return False
        return True
    else:
        saida = ['Tentativa', 'Erro']
        if bf.tentative > 1:
            saida[0] += 's'
        if bf.shot_try > 1:
            saida[1] += 's'
        
        print('Vitória ! ')
        input(f'{bf.tentative} {saida[0]}, com um total de {bf.shot_try+1} {saida[1]}')
        return False