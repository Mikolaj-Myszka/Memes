"""
Clearcode 'calculate' function Python project
"""

import csv
from itertools import chain, combinations
from operator import itemgetter
# DIAGNOSTICS -> Measuring operations time (not required)
# import time


def calculate(usb_size, memes):
    """Returns the best combination of memes (to sell for the highest price)
    for a given USB size."""

    print('USB size:', usb_size, 'GB')
    print('Memes:', memes)
    usb_size_in_mb = usb_size * 1024

    # Calculating all possible combinations
    comb = list(chain.from_iterable(
        combinations(memes, r) for r in range(1, len(memes)+1)
        ))
    print('\nNumber of possible combinations:', len(comb))
    # DIAGNOSTICS -> Watch out when dealing with large number of memes
    # print('\nCombinations:')
    # [print(i) for i in comb]
    # DIAGNOSTICS -> Time stamp
    # start = time.time()
    # Creating a 'res' list with a result
    res = []
    for j in comb:
        zipped = list(zip(*j))
        sum_mb = sum(zipped[1])
        # Filtering combinations that fit with USB size
        if sum_mb <= usb_size_in_mb:
            sum_caps = sum(zipped[2])
            meme_names = set(zipped[0])
            res.append((sum_caps, meme_names))
    # DIAGNOSTICS -> Time stamp
    # end = time.time()
    # print('\nOperation time:', end - start)

    # Deleting list with all combinations
    del comb
    # Sorting caps with descending order
    res.sort(key=itemgetter(0), reverse=True)
    # DIAGNOSTICS -> Top 5 scores
    # print('\nTop 5 scores:', res[0:5])

    return res[0]


if __name__ == '__main__':

    USB_SIZE = 1
    MEME_MODE = 0
    if MEME_MODE == 0:
        MEMES = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling_kid.avi', 605, 12)
            ]
    else:
        MEMES = []
        with open('csv/07.csv', 'r') as meme_file:
            CSV_FILE = csv.reader(meme_file, delimiter=',')
            for row in CSV_FILE:
                MEMES.append((row[0], int(row[1]), int(row[2])))

    print('\nWinner:', calculate(USB_SIZE, MEMES))
