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
        
        if set_menu(title='Como deseja estabelecer as embarcações ?', items=['Automático', 'Manual']):
            for i in range (number_of_vessels):
                vessel = set_menu(f'Tamanho da embarcação nº {i+1}: ', range(1, 6))+1
                bf_1.set_vesel_manual(vessel)
        else:
            bf_1.set_vessel_auto(number_of_vessels)    
        bf_2 = Game()
        print("#"*50)
        print("#"*50)
        print(f"{'Jogador 2 organize seu campo de batalha': ^50}")
        print("#"*50)
        input("#"*50)
            
        number_of_vessels = set_menu([f'{"Player: 2": ^20}\n', 'Selecione a quantidade de embarcações: '], range(1, 11))+1
        if set_menu(title='Como deseja estabelecer as embarcações ?', items=['Automático', 'Manual']):
            for i in range (number_of_vessels):
                vessel = set_menu(f'Tamanho da embarcação nº {i+1}: ', range(1, 6))+1
                bf_2.set_vesel_manual(vessel)
        else:
            bf_2.set_vessel_auto(number_of_vessels)    
            
        player_vs_player_local(bf_1, bf_2)
        
    elif option == 2:
        pass
    elif option == 3:
        return False

    return True

def player_vs_machine(bf: Game) -> bool:
    if bf.shot():
        if set_menu(title = '', items=['Atacar', 'Encerrar']):
            return False
        return True
    else:
        saida = ['Tentativa', 'Erro']
        if bf.tentative > 1:
            saida[0] += 's'
        if bf.shots_count > 1:
            saida[1] += 's'
        
        print('Vitória !')
        input(f'{bf.tentative} {saida[0]}, com um total de {bf.shots_count} {saida[1]}')
        return False
    
def player_vs_player_local(bf_1: Game, bf_2: Game) -> bool:
    surrender_1 = False
    surrender_2 = False
    
    while True:
        if bf_2.shot() and not bf_1.check_victory():
            if set_menu(title = 'Turno do Player 2', items=['Atacar', 'Encerrar']):
                surrender_1 = True
                break
        else:
            break
        
        if bf_1.shot() and not bf_2.check_victory():
            if set_menu(title = 'Turno do Player 1', items=['Atacar', 'Encerrar']):
                surrender_2 = True
                break
        else:
            break
            
    if surrender_1:
        print('Vitória do Player 2 !')
    elif surrender_2:
        print('Vitória do Player 1 !')
    elif bf_1.shots_count < bf_2.shots_count:
        print('Vitória do Player 2 !')
    elif bf_1.shots_count > bf_2.shots_count:
        print('Vitória do Player 2 !')
    else:
        print('Empate')
        
    print(f'Player 1: {bf_2.tentative} tentativas, com um total de {bf_2.shots_count} erros')
    input(f'Player 2: {bf_1.tentative} tentativas, com um total de {bf_1.shots_count} erros')
        