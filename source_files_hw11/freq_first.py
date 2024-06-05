import numpy as np
import matplotlib.pyplot as plt
with open('Five Letter Words.txt', 'r') as words:

 text = words.read()
 letters_counts = {}

 for c in text[0:len(text):6]:
#reads every sixth character starting with the first
    if c.isalpha():
        c = c.lower()
        letters_counts[c] = letters_counts.get(c, 0) + 1

 letters, counts = [], []

 for c in sorted(letters_counts, key = letters_counts.get, reverse = True):
    letters.append(c)
    counts.append(letters_counts[c])

 plot = plt.figure(figsize = (10, 5))

 plt.bar(letters, counts, color='blue', width = 0.5)
 plt.xlabel("Letters")
 plt.ylabel("Frequency")
 plt.title("Frequency of Letters in First Letter of Wordle Guesses")
 plt.show()