"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""

import text_utils

file = open("sample.txt", "r")
lines = file.readlines()
sum = 0
for line in lines:
    sum += text_utils.count_words(line)
average = sum / len(lines)
print(f"Average words per line: {average}")