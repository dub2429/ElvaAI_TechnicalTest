import sys

def closed_paths(number):
    # Dictionary to store the number of closed paths for each digit
    closed_paths = {
        '0': 1,
        '4': 1,
        '6': 1,
        '8': 2,
        '9': 1
    }
    
    
    # The number is converted to a string and iterates each digit of the number
    total_paths = 0
    for digit in str(number):
        
        # If the digit is in the dictionary, add its value to the total
        if digit in closed_paths:
            total_paths += closed_paths[digit]
    
    return total_paths



print('Enter a number or write E for exit: ')
for input in sys.stdin:
    
    if 'E' == input.rstrip() or 'e' == input.rstrip():
        print('Exit')
        break
    
    print('\nThe number of closed paths for this number: ', closed_paths(input), '\n')
    