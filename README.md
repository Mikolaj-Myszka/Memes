# Memes
Function that returns the best combination of memes (to sell for the highest price) for a given USB size.

Python 3.6.3

Function is based on standard library:
import csv
from itertools import chain, combinations
from operator import itemgetter

# Input:
The function calculate(usb_size, memes) takes exactly 2 arguments:
● usb_size: int
a number describing the capacity of the USB stick in GiB:
e.g. 1 means a USB with 1 GiB capacity.
● memes: List[Tuple[str, int, int]]
is a list of 3-element tuples, each with the name, size in MiB, and price in caps of a meme:
e.g. [('dolan.png', 126, 5), ('expanding_brain.jpeg', 421, 10)]

# Output:
The function returns a tuple with the first element being the total value of all memes on the USB stick, and the second being the set of names of the memes that should be copied onto the USB stick to maximize its value.
e.g. (15, {'dolan.png', 'expanding_brain.jpeg'})


Project consists of 2 elements:
1) main.py file where the function is defined
2) csv folder where example sets of memes are stored

# How to run the function
Function can used as a standalone file or imported.

1) Standalone file


# About the solution

# (Adidtional Notes)