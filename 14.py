print('If you want to convert grams to ounces, enter "1"\n')
print('If you want to calculate and display the equivalent centigrade temperature, enter "2"\n')
print('If you want to get only prime numbers from your numbers list, enter "3"\n')
print('If you want to calculate the volume of the sphere taking into account its radius, enter "4"\n')
print('If you want to checks whether a word or phrase is palindrome or not, enter "5"\n')
print('If you want to play a game, enter "6"\n')
print('If you want to calculate number of being with 2 legs and another with 4 legs by entering their all heads and all legs, enter "7"\n')
enter = int(input())

if enter == 1:
    def convert(grams):
        ounces = grams / 28.3495231
        return float(ounces)
    grams = float(input("Grams to ounces:"))
    print(convert(grams))

elif enter == 2:
    def toCelsius(F):
        Celsius = (5/9)
        Celsius *= F - 32
        return f'Celsius temperature: {round(Celsius,4)}'
    F = int(input("Fahrenheit temperature:"))
    print(toCelsius(F))

elif enter == 3:
    list_of_prime_numbers = []
    def filter_prime(a):
        for i in a:
            num = 0
            for j in range(1, int(i) + 1):
                if int(i) % int(j) == 0:
                    num += 1
            if num == 2:
                list_of_prime_numbers.append(i)
    a = input("Your list of numbers to print only prime numbers: ").split()
    filter_prime(a)
    print(f'Prime numbers: {list_of_prime_numbers}')

elif enter == 4:
    import math
    def Volume(radius):
        value = (4/3 * math.pi * radius**3)
        return f'Volume = {value}'

    radius = int(input("Radius = "))
    print(Volume(radius))

elif enter == 5:
    def checking(word):
        if word.lower() == word[::-1].lower():
            return f'{word} is Palindrome'
        else:
            return f'{word} is not Palindrome'

    word = input("Enter your word to chech if is it palindrome: ")
    print(checking(word))

elif enter == 6:
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

elif enter == 7:
    def solve(numheads, numlegs):
        y = numlegs / 2
        rabbit = y - numheads
        chicken = numheads - rabbit
        return f'Chickens: {int(chicken)}; Rabbits: {int(rabbit)};'

    a = int(input("Number of heads: "))
    b = int(input("Number of legs: "))
    print(solve(a, b))

elif enter > 7:
    import random 
    print("Hello, you out of range! What is your name?\nKBTU")
    print("\nWell, KBTU, let`s play a game, I am thinking of a number between 1 and 20.")
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



