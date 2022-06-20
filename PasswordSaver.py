import csv
import sys

# The password list - We start with it populated for testing purposes
passwords = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]


# The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

# The encryption key for the caesar cypher
encryptionKey = 16

# Caesar Cypher Encryption
def passwordEncrypt(unencryptedMessage, key):

    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage

# reused passwordEncrypt Function here to allow for decryption instead

def passwordDecrypt(encryptedMessage, key):

    # We will start with an empty string for the final decryptedMessage
    decryptedMessage = ''

    # For each symbol in the encryptedMessage we will add a decrypted symbol into the decryptedMessage
    for symbol in encryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num -= key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            decryptedMessage += chr(num)
        else:
            decryptedMessage += symbol

    return decryptedMessage

def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Replace a password")
    print(" 5. Save password file")
    print(" 6. Delete a password")
    print(" 7. Print the encrypted password list (for testing)")
    print(" 8. Quit program")
    print("Please enter a number (1-8)")
    choice = input()

    if(choice == '1'):  # Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)


    if(choice == '2'):  # Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        ####### YOUR CODE HERE ######

        # loops through the list to check all possible websites
        for i in range(len(passwords)):
            if passwordToLookup == passwords[i][0]:
                # print("Okay we are decrypting " + passwords[i][1])
                print("Your password is " + passwordDecrypt(passwords[i][1],encryptionKey))

        ####### YOUR CODE HERE ######


    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        ####### YOUR CODE HERE ######

        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)  #enrypts password in function
        # print(encryptedPassword)

        newPassword = [website, encryptedPassword]  # Creates a list of website and password input
        # print(newPassword)

        passwords.append(newPassword)  # Adds new password list to original list
        # print(passwords)

        ####### YOUR CODE HERE ######


    if(choice == '4'):  # replace a password
        print("Which website would you like to replace the password for?")
        replacePassword = input()

        for i in range(len(passwords)):
            if replacePassword == passwords[i][0]:  # if input matches website name, replace that index with new input
                print("Okay, what will your new password be? We will automatically encrypt it.")
                passwords[i][1] = passwordEncrypt(input(), encryptionKey)



    if(choice == '5'):  # Save the passwords to a file
        savePasswordFile(passwords, passwordFileName)


    if choice == '6':  # Added deletion option to delete passwords
        print("Which website would you like to delete the password for?")
        print(passwords)
        deletePassword = input()

        # Loops through the password list to check the websites
        for i in range(0, len(passwords)):
            if deletePassword == passwords[i][0]:  # if input matches website name, delete that index's list from the list
                passwords.remove(passwords[i])
                print("Okay, deleting password.")
                break


    if(choice == '7'):  # print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))


    if(choice == '8'):  # quit our program
        sys.exit()

    print()
    print()
