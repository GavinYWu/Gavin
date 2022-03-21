def fibonacci(n):
    if n == 1 or n==0:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def printFibonacci():
    n = int(input("Enter a number: "))
    output = [fibonacci(x+1) for x in range(n)]
    print(*output)
if __name__ == "__main__":
    printFibonacci()