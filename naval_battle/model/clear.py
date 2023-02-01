from os import system as os_system
from platform import system as so_system

def clear() -> None:
    so = so_system()
    if so == 'Windows':
        os_system('cls')
    else:
        os_system('clear')