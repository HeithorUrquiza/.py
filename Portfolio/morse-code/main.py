alphabet = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
morse_numbers = {'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

def get_message(): 
    return input('Type your message: ')


def encode(msg):
    output = []
    for char in msg.lower():
        if char in alphabet:
            output.append(alphabet[char] + ' ')
        elif char in morse_numbers: 
            output.append(morse_numbers[char] + ' ')
        elif char.isspace():
            output.append(' ' * 3)
    return ''.join(output)


def decode(msg):
    output = []
    for code in msg.split(' '):
        if code in alphabet.values():
            index = list(alphabet.values()).index(code)
            output.append(list(alphabet.keys())[index])
        elif code in morse_numbers.values():
            index = list(morse_numbers.values()).index(code)
            output.append(list(morse_numbers.keys())[index])
        else:
            output.append(' ')
    return ''.join(output)
    

def app():
    while True:
        answer = input('Do you wanna Encode or Decode your message?: ').lower()
        msg = get_message()
        if answer == 'encode':
            print(encode(msg))
            break
        elif answer == 'decode':
            print(decode(msg))
            break
        else:
            print('Command invalid! Try again')

app()