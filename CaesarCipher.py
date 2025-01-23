print("1. Encryption\n2. Decryption")
choice = int(input("Choose either (1 or 2): "))

if choice == 1:
    print("Encryption\n")
    
    print("Message can only be lower or upper case\n")
    message = input("Enter Message: ")
    
    shift = int(input("Enter key (0-25): "))
    encryptedMessage = ""
    
    for char in message:
    
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encryptedChar = chr((ord(char) - base + shift) % 26 + base)
            encryptedMessage += encryptedChar
        else: 
            encryptedMessage += char
    print(encryptedMessage)
                
elif choice == 2:
    print("Decryption\n")
        
    print("Message can only be lower or upper case\n")
    message = input("Enter Message: ")
        
    shift = int(input("Enter key (0-25): "))
    decryptedMessage = ""
        
    for char in message:
        
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decryptedChar = chr((ord(char) - base - shift) % 26 + base)
            decryptedMessage += decryptedChar
        else:
            decryptedMessage += char
    print(decryptedMessage)
            
else:
    print("Please choose from either option 1 or 2")
