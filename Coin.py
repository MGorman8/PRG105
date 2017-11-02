# pg 503
# simulate coin flip

import random


class Coin:

    def __init__(self):
        self.__side_up = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__side_up = 'Heads'
        else:
            self.__side_up = 'Tails'

    def get_side_up(self):
        return self.__side_up


def main():
    flip = Coin()
    heads = 0
    for i in range(0, 49):
        flip.toss()
        if flip.get_side_up() == 'Heads':
            heads += 1


    print('There were', heads,'heads and', 50 - heads, 'tails.')

main()
