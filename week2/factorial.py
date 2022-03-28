# Hack 2: Write Factorial function using classes, providing implementation of call.
# Print final number

class factorial(object):
    def __init__(self,n):
        self.n = n
    def factorial(self, x=None):
        n = self.n if x is None else x
        result = 1
        # If the entered number is 1 result is also 1
        if self.n == 1:
            result = 1
            return result
        else:
            # Calculates the factorial if the number isn't 1
            for x in range(1,n+1):
                result*=x
            return result

def printfactorial():
    fac1 = factorial(int(input("Enter a number for its factorial:")))
    print(fac1.factorial())

if __name__ == "__main__":
    printfactorial()