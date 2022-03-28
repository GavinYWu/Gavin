class check:
    def __init__(self,number):
        self.num = number
    # checks if number is prime
    def __call__(self):
        for x in range(2, int(num ** (1/2)) + 1):
            # checks if any number is divisible by 1, if not then it's not a prime number
            if num % x == 0:
                return str(num) + " is a prime number"
        # if it is then it is a prime number
        return str(num) + " is not a prime number"


if __name__ == "__main__":
    num = 23
    checkprime = check(num)
    print(checkprime())

    num = 100
    checkprime = check(num)
    print(checkprime())

