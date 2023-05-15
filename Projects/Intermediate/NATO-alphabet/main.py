import pandas

df = pandas.read_csv('Projects/Intermediate/NATO-alphabet/nato_phonetic_alphabet.csv')
dict_NATO = {row.letter:row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_input = input('Enter with a word: ').upper()

    try:
        phonetic_dict = [dict_NATO[letter] for letter in user_input]
    except KeyError:
        print("Sorry. Only letters in the alphabet, please\n") 
        generate_phonetic() 
    else:
        print(phonetic_dict)

generate_phonetic()
