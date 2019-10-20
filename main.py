import random
from string import ascii_uppercase
from minus import minus

SPEFFZ_ALL = minus(ascii_uppercase, 'YZ')
NOT_M_SLICE = minus(SPEFFZ_ALL, 'AQ CI KU SW')
I_OR_S = 'IS'

INCLUDE_M_SLICE = False

def main():
    while True:
        i_or_s = random.choice(I_OR_S)
        if INCLUDE_M_SLICE:
            other = random.choice(SPEFFZ_ALL)
        else:
            other = random.choice(NOT_M_SLICE)
        letters = [i_or_s, other]
        random.shuffle(letters)
        pair = ''.join(letters)
        input(pair)

if __name__ == '__main__':
    main()
