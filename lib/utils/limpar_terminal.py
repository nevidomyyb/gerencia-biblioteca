from os import system
from platform import system as sys

def limpar_terminal():
    '''
    Limpar terminal
    '''
    if sys() == "Windows":
        system('cls')
    else:
        system('clear')