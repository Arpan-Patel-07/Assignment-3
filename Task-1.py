def factorial(n):                                           #recursive function to calculate factorial
    if n<2:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input('Enter a number : '))                         #gettin a number from user

ans = factorial(n)                                          #function call
print('Factorial of number', n, 'is', ans)                  #print factorial of number that user gave