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

file = open("sample.txt", "r") # Opens the file
lines = file.readlines() # Splits the text into individual lines

sum = 0
for line in lines: # Counts the total number of words in the file
    sum += text_utils.count_words(line)
average = sum / len(lines) # Averages the number of words per line
if average - int(average) == 0: # Makes the result an int if it is a whole number
    average = int(average)
print(f"Average words per line: {average}")