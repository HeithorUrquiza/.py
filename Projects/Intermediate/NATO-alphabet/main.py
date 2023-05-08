import pandas

df = pandas.read_csv('Projects/Intermediate/NATO-alphabet/nato_phonetic_alphabet.csv')

dict_NATO = {row.letter:row.code for (index, row) in df.iterrows()}
user_input = input('Enter with a word: ').upper()
phonetic_dict = [dict_NATO[letter] for letter in user_input]
        
print(phonetic_dict)
