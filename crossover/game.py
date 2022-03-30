import random

def game(a,b):
    on = True
    while on == True:
        answer = random.randint(a, b)
        count = 0
        guess = int(input("Guess a number in range " + str(a) + "," + str(b) + ": "))
        while guess is not answer:
            if guess == answer:
                print("Yea")
                print("Guesses: ", count)
                cont = input("Continue?: ")
                if (cont == "No" or cont == "no"):
                    on = False
            elif(guess > answer and guess <= b):
                print("Too high")
                count += 1
                break
            elif(guess < answer and guess >= a):
                print("Too Low")
                count += 1
                break
