def encryption0 (rotation,content):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Use parameter 'rotation' to create shifted alphabet
    shifted = ''### INSERT CODE HERE
    print()
    print("Rotated encryption alphabet")
    print (shifted)
    encrypted = ''
    decrypted = ''
    
    # Strip out non-alphabetic characters and convert to upper case
    newContent = ''
    ### INSERT CODE HERE
    print("\n Modified message: " + newContent)

    # Do encryption
    for ch in newContent:
        ### INSERT CODE HERE
        pass
    print("\n Encrypted message: " + encrypted)
    
    # Do decryption, using <str>.find(ch) to compute index into alph
    for ch in encrypted:
        ### INSERT CODE HERE
        pass
    print("\n Decrypted message:", decrypted)












def encryption1 (rotation,content):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Use parameter 'rotation' to create shifted alphabet
    shifted = alph[rotation:26] + alph[0:rotation]
    print()
    print("Rotated encryption alphabet")
    print (shifted)
    encrypted = ''
    decrypted = ''
    
    # Strip out non-alphabetic characters and convert to upper case
    newContent = ''
    for ch in content:
        if ch.isalpha():
            newContent += ch.upper()
    print("\n Modified message: " + newContent)
    
    # Do encryption, using distance from 'A' as index into shifted
    for ch in newContent:
        encrypted += shifted[ord(ch)-ord('A')]
    print("\n Encrypted message: " + encrypted)
    
    # Do decryption, using <str>.find(ch) to compute index into alph
    for ch in encrypted:
        decrypted += alph[shifted.find(ch)]
    print("\n Decrypted message:", decrypted)













    
# Here is the complete program using a randomly shuffled alphabet to do the
# encryption. Two different approaches are illustrated, first using corresponding
# array indices and then with the built-in string functions maketrans and translate.

import random

def encryption2(content):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # random.shuffle() will be used to create the new alphabet for encrypting messages
    # This functions works on lists rather than strings, so first we convert alph to a list
    temp = list(alph)
    random.shuffle(temp)
    
    # Convert the shuffled list back to a string so that we can use str.find()
    # Used join applied to a iterable of strings
    shuffled = "".join(temp)
    print()
    print("Random encryption alphabet:")
    print (shuffled)
    
    encrypted = ''
    decrypted = ''
    # Strip out non-alphabetic characters and convert to upper case
    newContent = ''
    for ch in content:
        if ch.isalpha():
            newContent += ch.upper()
    print("\n Message: " + newContent)

    # Do encryption, using distance from 'A' as index into shifted
    for ch in newContent:
        encrypted += shuffled[ord(ch)-ord('A')]
    print("\n Encrypted message: " + encrypted)

    # Do decryption, using <str>.find(ch) to compute index into alph
    for ch in encrypted:
        decrypted += alph[shuffled.find(ch)]
    print("\n Decrypted message: " + decrypted)
    
def _main ():
    encryption0(5, "This is a sentence to be encrypted.")
    encryption1(5, "This is a sentence to be encrypted.")
    encryption1(12, "This is a sentence with extra% stuff ()& to be encrypted.")
    encryption2("This is a sentence to be encrypted.")
    encryption2("This is a sentence with extra% stuff ()& to be encrypted.")
                
if __name__ == '__main__':
    _main()
