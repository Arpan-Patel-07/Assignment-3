import math

number = int(input('Enter a number'))               #taking input from user

squarerot_number = math.pow(number,1/2)             #Calculate square root

def log10(number):                                  #function to calculate logarithm
    if number>0:
        log_num = math.log(number)
    else:
        print('Undefined')
        
    return log_num

log_number = log10(number)

sine_number = math.sin(number)                      #calculate sine value


#print output

print('Square root of', number, 'is', squarerot_number)
print('Logarithm of', number, 'is', log_number)
print('Sine of', number, 'is', sine_number)