import csv
import re

text_file = open("words.txt", "r")
lines = text_file.readlines()

no_letters = '[gkmqvwxioz]'
longest_word = ""
for i in lines:
    bad_words = re.findall(no_letters,i)
    if len(i) <= len(longest_word):
        continue
    if bad_words:
        continue
    longest_word = i
print(longest_word)