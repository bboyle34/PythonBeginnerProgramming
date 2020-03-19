from random import randint # import randint

# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# Generate a random lowercase letter
def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')

# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

# Generate a random digit character
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')

# Generate a random character
def getRandomASCIICharacter():
    return getRandomCharacter(chr(0), chr(127))
def main():
    choice = input("Enter a choice: ")
    if choice[0].upper() == "L":
        getRandomLowerCaseLetter()
    elif choice[0].upper() == "U":
        getRandomUpperCaseLetter()
    elif choice[0].upper() == "D":
        getRandomDigitCharacter()
    elif choice[0].upper() == "A":
        getRandomASCIICharacter()
    else:
        choice = input("Enter  choice that fits: ")
        main()
main()
    
