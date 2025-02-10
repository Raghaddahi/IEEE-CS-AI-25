#Create a program that reads a text file,
# counts the occurrences of each word, and prints the results.
with open('simple_text.txt') as file:
    contents=file.read( )

contents=contents.lower()
