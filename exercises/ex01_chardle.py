"""EX01 - Chardle - A cute step toward Wordle."""
__author__= "730462871"

word: str=str(input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5-characters") 
    exit()
character: str=str(input("Enter a single character: "))
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)

instance = 0

if character == word[0]:
    instance = instance + 1
    print(character + " found at index 0")
if character == word[1]:
    instance = instance + 1
    print(character + " found at index 1")
if character == word[2]:
    instance = instance + 1
    print(character + " found at index 2") 
if character == word[3]:
    instance = instance + 1
    print(character + " found at index 3")
if character == word[4]:
    instance = instance + 1
    print(character + " found at index 4")

print(str(instance) + " instances of " + character + " found in " + word)
