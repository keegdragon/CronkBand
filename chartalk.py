import gametools
import gameview
import gamedata
import random


def build_char():
    print('+--------------------------------------------------------+\n' +
          '|  CCC  RRRR   OOO  N   N K   K BBBB   AAA  NN   N DDDD  |\n' +
          '| C   C R   R O   O NN  N K  K  B   B A   A N N  N D   D |\n' +
          '| C     RRRR  O   O N N N KKK   BBBB  AAAAA N  N N D   D |\n' +
          '| C   C R   R O   O N  NN K  K  B   B A   A N   NN D   D |\n' +
          '|  CCC  R   R  OOO  N   N K   K BBBB  A   A N    N DDDD  |\n' +
          '+--------------------------------------------------------+\n')
    print('Welcome to the CronkBand Character Generator!')
    print('')
    print('')
    print('Ah yes, we\'ve been expecting you.') 
    print('You\'ll have to be recorded before you\'re ready to begin.') 
    print('There is one way to do this (and the choice is yours).')
    print('')
    name = input('What is the name of your character? ')
    print('')
    symbol = ''
    while not len(symbol) == 1:
        print('What do you look like?')
        symbol = input('Choose a single ASCII character: ')
        print('')
    pc = gametools.Character(name, symbol)
    class_choice = input('What is your class? ')
    while class_choice not in #pc.class_list:
        class_choice = input('Not a valid class. Try again: ')
    
    return pc


