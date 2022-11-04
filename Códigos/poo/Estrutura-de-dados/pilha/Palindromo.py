from Stack import Stack

def isPalindrome(palavra):
    palindrome = Stack()
    word = str(palavra).upper()
    for i in word:
        palindrome.push(i)
    count = 0
    for i in word:
        if palindrome.pop() == i:
            count += 1
    if count == len(word):
        return True
    else: 
        return False     
    
    
print(isPalindrome("Revive"))