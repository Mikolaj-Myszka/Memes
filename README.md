# Calculate
Function that returns the best combination of memes (to sell for the highest price) for a given USB size.

# Technologies
Project is created with Python 3.6.3 and is based on the standard library:
* csv
* chain, combinations from itertools
* itemgetter from operator 

# Input:
The function calculate(usb_size, memes) takes exactly 2 arguments:
* usb_size: int</br>
a number describing the capacity of the USB stick in GiB:</br>
e.g. 1 means a USB with 1 GiB capacity.
* memes: List[Tuple[str, int, int]]</br>
is a list of 3-element tuples, each with the name, size in MiB, and price in caps of a meme:</br>
e.g. [('dolan.png', 126, 5), ('expanding_brain.jpeg', 421, 10)]

# Output:
The function returns a tuple with the first element being the total value of all memes on the USB stick, and the second being the set of names of the memes that should be copied onto the USB stick to maximize its value:</br>
e.g. (15, {'dolan.png', 'expanding_brain.jpeg'})

Project consists of 2 elements:
1) main.py file where the function is defined
2) csv folder where example sets of memes are stored

# Usage
Function can be used as a standalone or imported module:

1) Standalone
```
$ python main.py
```
Set `MEME_MODE` to 0 to test default list of `MEMES`.</br>
</br>
You can also load sets of memes from a CSV file, in this case set `MEME_MODE` to 1 (or any other number except 0).</br>
The CSV files are stored in the 'csv' folder. You can make use of pre-defined csv files or upload your own.</br>
When using a new csv file, remember about changing a filename in 'main.py':
```python
with open('csv/07.csv', 'r') as meme_file:
```

2) Imported
```python
>>> from main import calculate
```

# Additional Notes
Program was checked with pylint and flake8.

# Suggestions
The project documentation says "The function should return a tuple".</br>
There might be a situation where there are 2 or more meme sets with the same maximum caps value (but different total MB capacity).</br>
I think it would be better if the function could take this scenario into consideration and return more meme sets with an additional information of total size in MB.</br>
Users then would have more options for choosing their preferable meme set.


