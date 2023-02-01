from model.Game import *
import sys
sys.path.insert(1, '../')

if __name__ == '__main__':
    bf = Game()
    bf.set_vessel()
    bf.shot()
    bf.shot()