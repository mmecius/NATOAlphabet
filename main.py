import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

print(nato_phonetic_alphabet.items())
df = pandas.DataFrame(nato_phonetic_alphabet)

for (index, row) in df.iterrows():
    if row.letter == "a":
        print(row.score)


# {letter: code for (index, row) in df.iterrows()}

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

