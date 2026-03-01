ask = input('write the words or paragraph you want to count: ')
words = ask.strip().split()

word_count = len(words)  # total number of words
char_with_spaces = len(ask)
char_without_spaces = len(ask.replace(" ", ""))# this replace words as that it removes the whitespace" "(there is one space here) with replace it with ""(no space between them)

print('number of words', word_count)
print("characters with the spaces", char_with_spaces)
print('characters without the spaces', char_without_spaces)