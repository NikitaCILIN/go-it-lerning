import random

def get_numbers_ticket(min, max, quantity):
    if min<1 or max > 1000 or max < min or quantity not in range (min, max):
        return 'Error'
    getnumtiklist = []
    while(len(getnumtiklist) < quantity):
        x = random.randint(min, max)
        if x not in getnumtiklist:
            getnumtiklist.append(x)
    getnumtiklist.sort()
    return getnumtiklist

print("Ваші лотерейні числа:", get_numbers_ticket(3, 77, 5))        
print("Ваші лотерейні числа:", get_numbers_ticket(-5, 55, 5))
print("Ваші лотерейні числа:", get_numbers_ticket(1, 1000, 5))
print("Ваші лотерейні числа:", get_numbers_ticket(-4, 10, 4))