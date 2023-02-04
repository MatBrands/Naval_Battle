from model.clear import *
from model.Game import *
from model.Menu import *

def selection_game() -> bool:
    title = 'Selecione a modalidade: '
    items = ['Jogador vs. Máquina', 'Jogador vs. Jogador (Local)', 'Jogador vs. Jogador (Rede)', 'Retornar']
    
    option = set_menu(title, items)
        
    if option == 0:
        bf = Game()
        bf.set_vessel_auto(  set_menu('Selecione a quantidade de embarcações: ', range(1, 11))   +1)
        
        while player_vs_machine(bf):
            continue
    elif option == 1:
        bf_1 = Game()
        print("#"*50)
        print("#"*50)
        print(f"{'Jogador 1 organize seu campo de batalha': ^50}")
        print("#"*50)
        input("#"*50)
        
        number_of_vessels = set_menu([f'{"Player: 1": ^20}\n', 'Selecione a quantidade de embarcações: '], range(1, 11))+1
        for i in range (number_of_vessels):
            vessel = set_menu(f'Tamanho da embarcação nº {i+1}: ', range(1, 6))+1
            bf_1.set_vesel_manual(vessel)
        
        bf_2 = Game()
        print("#"*50)
        print("#"*50)
        print(f"{'Jogador 2 organize seu campo de batalha': ^50}")
        print("#"*50)
        input("#"*50)
            
        number_of_vessels = set_menu([f'{"Player: 2": ^20}\n', 'Selecione a quantidade de embarcações: '], range(1, 11))+1
        for i in range (number_of_vessels):
            vessel = set_menu(f'Tamanho da embarcação nº {i+1}: ', range(1, 6))+1
            bf_2.set_vesel_manual(vessel)
            
    elif option == 2:
        pass
    elif option == 3:
        return False

    return True

def player_vs_machine(bf: Game) -> bool:
    if bf.shot():
        if set_menu(title = '', items=['Continuar', 'Encerrar']):
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