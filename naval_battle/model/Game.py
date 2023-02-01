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
        self.shot_try = 0
        self.test = 0

    def on_press(self, key) -> bool:
        if str(key) == 'Key.up':
            self.i -= 1
        elif str(key) == 'Key.down':
            self.i += 1
        elif str(key) == 'Key.left':
            self.j -= 1
        elif str(key) == 'Key.right':
            self.j += 1
        elif str(key) == 'Key.enter':
            self.acess = True

        return False
    
    def set_vessel(self, num_of_vessels: int = 5) -> int:
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
    
    def show_bf(self) -> None:
        self.i = 0
        self.j = 0
        self.acess = False
        current_board = [item.copy() for item in self.visible_board]
        
        while not self.acess:
            self.show_board(current_board)

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

    def shot(self, number_of_shots: int = 3) -> None:
        self.test += 1
        while self.shot_try%4 < number_of_shots:
            self.show_bf()
            
        self.shot_try+=1
    
    def show_board(self, current_board: list) -> None:
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        clear()
        
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