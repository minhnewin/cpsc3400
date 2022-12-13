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



# The following code is not in a function, so it is what is executed when
# this module is loaded by Python

encryption0(5, "This is a sentence to be encrypted.")
