import string

alpha = list(string.ascii_lowercase)


def shift(inList):  #Shifts the first item in the list to the end
    first = inList[0]
    inList.pop(0)
    inList.append(first)
    return inList
    
def encrypt(ciphertext, message):
    counter = 0
    for index, elem in enumerate(message):
        0
        for i in ciphertext:
            
    
    
    
#User input handling portion of the progam
userinput = input("Welcome to the vigenere cipher program. Type 'help' for help using the program, or continue using it if you already know how. To exit, type CTRL + C\n")
while True:
    
    try:
        #Damn, I wish python had switch case
    
        if userinput == 'help':
            print("encrypt [ciphertext] - encrypt a block of text, which you enter after inputting the ciphertext\n"
                  "decrypt [ciphertext] - decrypt a block of text, which you enter after inputting the ciphertext\n"
                  "help  - output this menu")
            userinput = input()
            
        elif userinput[:7] == 'encrypt':
            cipherText = userinput[8:]
            if cipherText == '':
                print("you didn't enter a ciphertext")
            else:
                print(ciphertext)  #replace this with the encrypt algorithm
            
            userinput = input()
            
        elif userinput == 'decrypt':
            cipherText = userinput[8:]
            if cipherText == '':
                print("you didn't enter a ciphertext")
            else:
                print(ciphertext)  #replace this with the encrypt algorithm
            
            userinput = input()            
            
        elif userinput == 'crack':
            userinput = input("haha you think this program actually has this feature\n")
            
        #elif userinput == 'exit':
            #sys.exit()
            
                        
        else:
            userinput = input("You didn't enter a command I recognize. Type help to see what commands are availible\n")
    
    
                
    except:
        print("fuck you")
        userinput = ''