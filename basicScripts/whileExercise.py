'''Write a program to accept a number from a user and calculate the sum of all 
numbers from 1 to a given number'''

sumUp = int(input('Introduce the value to sum up: '))
value = 1
sum = 0

while value <= sumUp:
    sum += value
    value += 1

print(sum)
