import csv
from itertools import chain, combinations
from operator import itemgetter

def calculate(usb_size, memes):
    """
    Returns the best combination of memes (to sell for the highest price) for a given USB size.
    """

    print('USB size:', usb_size, 'GB')
    print('Memes:', memes)

    usb_size_in_mb = usb_size * 1024
    
    z = chain.from_iterable(combinations(memes, r) for r in range(1,len(memes)+1))
    #print(comb)
    comb = list(z)

    print('\nNumber of possible combinations:', len(comb))

    """
    print('\nCombinations:')
    for i in comb:
        print(i)
    """

    print('')
    res = []
    # Check size sum per combination
    for j in range(0,len(comb)):
        #print(comb[j])
        el_sum = 0
        for i in range(0,len(comb[j])):
            el_sum += comb[j][i][1]
        #print(el_sum)

        if el_sum <= usb_size_in_mb:
            meme_names = set()
            cap_sum = 0
            for i in range(0,len(comb[j])):
                meme_names.add(comb[j][i][0])
                cap_sum += comb[j][i][2]
            res.append((cap_sum, meme_names, el_sum))


    print('Potential winners:', len(res))
    print(res[0:5])

    
    res.sort(key=itemgetter(0), reverse=True)
    print(res[0:5])

    return res[0]


if __name__ == '__main__':

    usb_size = 1

    meme_mode = 1
    if meme_mode == 0:
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling_kid.avi', 605, 12)
            ]
    else:
        memes = []
        with open('csv/07.csv', 'r') as meme_file:
            csv_file = csv.reader(meme_file, delimiter=',')
            for row in csv_file:
                memes.append((row[0],int(row[1]),int(row[2])))

    print('\nWinner:', calculate(usb_size, memes))
