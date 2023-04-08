alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encoded_mesage = []
    for letter in text:
        letter_encoded = alphabet.index(letter.lower()) + shift
        
        if letter_encoded > len(alphabet) - 1:
            encoded_mesage.append(alphabet[(letter_encoded - len(alphabet) - 1)])
        else:
            encoded_mesage.append(alphabet[letter_encoded])
    
    print(''.join(encoded_mesage))

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text=text, shift=shift)