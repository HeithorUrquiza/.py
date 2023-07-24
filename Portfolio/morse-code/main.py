alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
morse_numbers = ['.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']  


def get_message(): 
    return input('Type your message: ')


def encode(msg):
    output = []
    for char in msg.lower():
        if char in alphabet:
            index = alphabet.index(char)
            output.append(morse_alphabet[index] + ' ')
        elif char in numbers: 
            index = numbers.index(char)
            output.append(morse_numbers[index] + ' ')
        else:
            output.append(' ' * 3)
    return ''.join(output)
        

def decode(msg):
    output = []
    count = 0
    for code in msg.split(' '):
        if code in morse_alphabet:
            index = morse_alphabet.index(code)
            output.append(alphabet[index])
        elif code in morse_numbers:
            index = morse_numbers.index(code)
            output.append(numbers[index])
        else:
            count += 1
            if count == 3:
                output.append(' ')
                count = 0
    return ''.join(output)
    

def app():
    answer = input('Do you wanna Encode or Decode your message?: ').lower()
    msg = get_message()
    if answer == 'encode':
        print(encode(msg))
    elif answer == 'decode':
        print(decode(msg))
    else:
        print('\nCommand invalid! Try again\n')
        app()
        
        
app()