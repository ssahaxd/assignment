# Global variables
SIZE = 256
S = [0] * SIZE


def setKey(key):
    # RC4 Key Scheduling Algorithm
    global S
    S = [n for n in range(SIZE)]
    j = 0
    for i in range(SIZE):
        j = (j + S[i] + key[i % len(key)]) % SIZE
        
    S[i], S[j] = S[j], S[i]

def byteGenerator():
    # RC4 Pseudo-Random Generation Algorithm
    global p, q, S
    p = (p + 1) % SIZE
    q = (q + S[p]) % SIZE
    S[p], S[q] = S[q], S[p]
    return S[(S[p] + S[q]) % SIZE]

def encrypt(key,inputString):
    ##Encrypt input string returning a byte list
    setKey(string_to_list(key))
    return [ord(p) ^ byteGenerator() for p in inputString]

def decrypt(inputByteList):
    ##Decrypt input byte list returning a string
    return "".join([chr(c ^ byteGenerator()) for c in inputByteList])



def intToList(inputNumber):
    ##Convert a number into a byte list
    inputString = "{:02x}".format(inputNumber)
    return [int(inputString[i:i + 2], 16) for i in range(0,    len(inputString), 2)]

def string_to_list(inputString):
    ##Convert a string into a byte list
    return [ord(c) for c in inputString]




loop = 1
while loop == 1: #simple loop to always bring the user back to the menu

    print("RC4 Encryptor/Decryptor")
    print
    print("Please choose an option from the below menu")
    print
    print("1) Encrypt")
    print("2) Decrypt")
    print

    choice = input("Choose your option: ")
    choice = int(choice)

    if choice == 1:
        key = raw_input("Enter Key: ")
        inputstring = raw_input("enter plaintext: ")
        encrypt(key, inputstring)


    elif choice == 2:   
        key = raw_input("Enter Key: ")
        ciphertext = raw_input("enter plaintext: ")
        print decrypt(intToList(ciphertext))

    elif choice == 3: 
    #returns the user to the previous menu by ending the loop and clearing the screen.
        loop = 0

    else:   
        print ("please enter a valid option") #if any NUMBER other than 1, 2 or 3 is entered.