from Stack import Stack

def isPalindrome(palavra):
    palindrome = Stack()
    word = str(palavra).upper()
    for i in word:
        palindrome.push(i)
    count = 0
    for i in word:
        if palindrome.pop() != i:
            return False
    return True    
    
    
def main():
    word = input("\nDigite a palavra: ")
    if isPalindrome(word):
        print("\nEsta palavra é um palindromo !!\n")
    else:
        print("\nEsta palavra NÃO é um palindromo !!\n")


main()