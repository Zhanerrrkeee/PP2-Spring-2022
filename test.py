import random 
print("Hello! What is your name?\nKBTU")
print("\nWell, KBTU, I am thinking of a number between 1 and 20.")
print("Take a guess.")

def Guess_the_number(a, number, tries):
    if a == number:
        print(f'Good job, KBTU! You guessed my number in {tries} guesses!')
    else:
        tries += 1
        if number > a:
            print("Your guess is too high.\nTake a guess")
            number = int(input())
            Guess_the_number(a, number, tries)
        else:
            print("Your guess is too low.\nTake a guess")
            number = int(input())
            Guess_the_number(a, number, tries)


a = random.randrange(1,20)
number = int(input())
tries = 1
Guess_the_number(a, number, tries)