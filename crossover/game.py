import random

def game(a,b):
    on = True
    while on == True:
        answer = random.randint(a, b)
        count = 0
        guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
        while guess != answer:
            if(guess > answer and guess <= b):
                print("Too high")
                guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
                count += 1

            elif(guess < answer and guess >= a):
                print("Too Low")
                guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
                count += 14

            else:
                print("Number outside predefined range")
                guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))


        print("Yea")
        print("Guesses: ", count)
        cont = input("Continue?: ")
        if (cont == "No" or cont == "no"):
            on = False
        else:
            on = True
def gamerun():
    a = int(input("Choose lowest number for range: "))
    b = int(input("Highest number: "))
    game(a,b)