PLACEHOLDER = "[name]"

with open('Projects/Intermediate/mail-merge/Input/Names/list_names.txt') as file_names:
    names = file_names.readlines()

with open('Projects/Intermediate/mail-merge/Input/Letters/starting_letter.txt') as letter_file:
        line_content = letter_file.read()
        
        for name in names:
            stripped_name = name.strip()
            new_letter = line_content.replace(PLACEHOLDER, stripped_name)
            
            with open(f'Projects/Intermediate/mail-merge/Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as letter:
                letter.write(new_letter)