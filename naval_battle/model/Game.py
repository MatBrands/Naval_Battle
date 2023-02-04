from termcolor import colored
from pynput import keyboard
from random import randint
from model.clear import clear

LEN_BOARD = 10
MAX_LEN_VESSEL = 5

class Game:
    def __init__(self) -> None:
        self.board = [['~']*LEN_BOARD for _ in range(LEN_BOARD)]
        self.visible_board = [['~']*LEN_BOARD for _ in range(LEN_BOARD)]
        self.i = 0
        self.j = 0
        self.orientation = 0
        self.shot_try = 0
        self.tentative = 0
    
    def on_press(self, key) -> bool:
        if str(key) == 'Key.up':
            self.i -= 1
        elif str(key) == 'Key.down':
            self.i += 1
        elif str(key) == 'Key.left':
            self.j -= 1
        elif str(key) == 'Key.right':
            self.j += 1
        elif str(key) == 'Key.space':
            self.orientation += 1
        elif str(key) == 'Key.enter':
            self.acess = True

        return False
    
    def set_vessel_auto(self, num_of_vessels: int = 5) -> None:
        current_number = 0
        
        while current_number < num_of_vessels:
            status = True
            vessel = randint(1, MAX_LEN_VESSEL)
            line = randint(0, LEN_BOARD-1)
            column = randint(0, LEN_BOARD-1)
            direction = randint(0, 1)
            
            if direction:
                if line + vessel < LEN_BOARD:
                    for i in range(line, line + vessel):
                        if self.board[i][column] not in '~':
                            status = False
                            break
                        if i+1 < LEN_BOARD:
                            if self.board[i+1][column] not in '~':
                                status = False
                                break
                        if i-1 >= 0:
                            if self.board[i-1][column] not in '~':
                                status = False
                                break
                        if column+1 < LEN_BOARD:
                            if self.board[i][column+1] not in '~':
                                status = False
                                break
                        if column-1 >= 0:
                            if self.board[i][column-1] not in '~':
                                status = False
                                break
                        
                    if status:
                        for i in range(line, line + vessel):
                            self.board[i][column] = str(vessel)
                else:
                    status = False
                            
            else:
                if column + vessel < LEN_BOARD:
                    for i in range(column, column + vessel):
                        if self.board[line][i] not in '~':
                            status = False
                            break
                        if i+1 < LEN_BOARD:
                            if self.board[line][i+1] not in '~':
                                status = False
                                break
                        if i-1 >= 0:
                            if self.board[line][i-1] not in '~':
                                status = False
                                break
                        if line+1 < LEN_BOARD:
                            if self.board[line+1][i] not in '~':
                                status = False
                                break
                        if line-1 >= 0:
                            if self.board[line-1][i] not in '~':
                                status = False
                                break
                        
                    if status:
                        for i in range(column, column + vessel):
                            self.board[line][i] = str(vessel)
                else:
                    status = False
                    
            if status:
                current_number+=1
    
    def set_vesel_manual(self, vessel: int) -> None:
        self.i = 0
        self.j = 0
        self.orientation = 0
        self.acess = False
        current_board = [item.copy() for item in self.board]
        
        while not self.acess:
            self.status = False
            self.print_set_vessel(current_board, vessel)

            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
                current_board = [item.copy() for item in self.board]
        
            if self.acess and not self.status:
                i = self.i % LEN_BOARD
                j = self.j % LEN_BOARD
                for k in range(vessel):
                    if self.orientation:
                        self.board[i+k][j] = str(vessel)
                    else:
                        self.board[i][j+k] = str(vessel)
            else:
                self.acess = False
        
        input()
        clear()
    
    def battlefield(self) -> None:
        self.acess = False
        current_board = [item.copy() for item in self.visible_board]
        
        while not self.acess:
            self.print_battlefield(current_board)

            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
                current_board = [item.copy() for item in self.visible_board]
        
            if self.acess:
                if current_board[self.i % LEN_BOARD][self.j % LEN_BOARD] not in '~':
                    self.acess = False
                elif self.board[self.i % LEN_BOARD][self.j % LEN_BOARD] not in '~':
                    self.visible_board[self.i % LEN_BOARD][self.j % LEN_BOARD] = self.board[self.i % LEN_BOARD][self.j % LEN_BOARD]
                else:
                    self.visible_board[self.i % LEN_BOARD][self.j % LEN_BOARD] = '*'
                    self.shot_try += 1
        
        input()
        
        clear()
        
        if self.shot_try%4 == 3:
            self.print_battlefield(self.visible_board)
            input("Prosseguir ")
    
    def shot(self) -> True:
        self.i = 0
        self.j = 0
        self.tentative += 1
        
        while self.shot_try%4 < 3:
            self.battlefield()
            if self.check_victory():
                return False
            
        self.shot_try+=1
        
        return True
    
    def print_battlefield(self, current_board: list) -> None:
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        clear()
        
        print(f'Tentativa: {self.tentative}')
        print(f'Tiro: {self.shot_try%4} de 3')
        
        for i in range (LEN_BOARD+1):
            if i: print(i, end='   ')
            else: print(' ', end='   ')
            
        for i in range(LEN_BOARD):
            if not i: print()
            print(f'{letter[i]}', end='   ')
            for j in range(LEN_BOARD):
                if self.i % LEN_BOARD == i and self.j % LEN_BOARD == j:
                    print(colored(current_board[i][j], 'green'), end='   ')
                elif current_board[i][j] in '~':
                    print(colored(current_board[i][j], 'blue'), end='   ')
                elif current_board[i][j] in '*':
                    print(colored(current_board[i][j], 'red'), end='   ')
                elif current_board[i][j] in '1':
                    print(colored(current_board[i][j], 'yellow'), end='   ')
                elif current_board[i][j] in '2':
                    print(colored(current_board[i][j], 'white'), end='   ')
                elif current_board[i][j] in '3':
                    print(colored(current_board[i][j], 'cyan'), end='   ')
                elif current_board[i][j] in '4':
                    print(colored(current_board[i][j], 'light_blue'), end='   ')
                elif current_board[i][j] in '5':
                    print(colored(current_board[i][j], 'magenta'), end='   ')
            print()
    
    def print_set_vessel(self, current_board: list, vessel: int) -> None:
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        clear()
            
        i = self.i % LEN_BOARD
        j= self.j % LEN_BOARD
        
        if self.orientation%2:
            if i-1 >= 0:
                if current_board[i-1][j] not in '~':
                    self.status = True
            if i+vessel < LEN_BOARD:
                if current_board[i+vessel][j] not in '~':
                    self.status = True
        else:
            if j-1 >= 0:
                if current_board[i][j-1] not in '~':
                    self.status = True
            if j+vessel < LEN_BOARD:
                if current_board[i][j+vessel] not in '~':
                    self.status = True
        
        for k in range(vessel):
            if self.orientation%2:
                if i+k < LEN_BOARD:
                    if current_board[i+k][j] not in '~':
                        self.status = True
                    if j+1 < LEN_BOARD:
                        if current_board[i+k][j+1] not in '~':
                            self.status = True
                    if j-1 >= 0:
                        if current_board[i+k][j-1] not in '~':
                            self.status = True
                
                if i+vessel > LEN_BOARD:
                    if i+k < LEN_BOARD:
                        self.status = True
            else:
                if j+k < LEN_BOARD:
                    if current_board[i][j+k] not in '~':
                        self.status = True
                    if i+1 < LEN_BOARD:
                        if current_board[i+1][j+k] not in '~':
                            self.status = True
                    if i-1 >= 0:
                        if current_board[i-1][j+k] not in '~':
                            self.status = True
                
                if j+vessel > LEN_BOARD:
                    if j+k < LEN_BOARD:
                        self.status = True
                
        for k in range(vessel):
            if self.orientation%2:
                if i+k < LEN_BOARD:
                    if self.status:
                        current_board[i+k][j] = colored(str(vessel), 'red')
                    else:
                        current_board[i+k][j] = colored(str(vessel), 'green')
            else:
                if j+k < LEN_BOARD:
                    if self.status:
                        current_board[i][j+k] = colored(str(vessel), 'red')
                    else:
                        current_board[i][j+k] = colored(str(vessel), 'green')
            
        for i in range(LEN_BOARD+1):
            if i: print(i, end='   ')
            else: print(' ', end='   ')
                       
        for i in range(LEN_BOARD):
            if not i: print()
            print(f'{letter[i]}', end='   ')
            for j in range(LEN_BOARD):
                if current_board[i][j] in '~': print(colored(current_board[i][j], 'blue'), end='   ')
                elif current_board[i][j] in '1': print(colored(current_board[i][j], 'yellow'), end='   ')
                elif current_board[i][j] in '2': print(colored(current_board[i][j], 'white'), end='   ')
                elif current_board[i][j] in '3': print(colored(current_board[i][j], 'cyan'), end='   ')
                elif current_board[i][j] in '4': print(colored(current_board[i][j], 'light_blue'), end='   ')
                elif current_board[i][j] in '5': print(colored(current_board[i][j], 'magenta'), end='   ')
                else: print(current_board[i][j], end='   ')
            print()
    
    def check_victory(self) -> bool:
        for i in range(LEN_BOARD):
            for j in range(LEN_BOARD):
                if self.board[i][j] not in '~':
                    if self.board[i][j] != self.visible_board[i][j]:
                        return False
        
        return True