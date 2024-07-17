import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

new_word = input("Enter a new word: ").upper()
result = [new_dict[letter] for letter in new_word]
print (result)
