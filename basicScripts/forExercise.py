'''Calculate the cube of all numbers from 1 to a given number'''

value = int(input('Introduce the value to calculate '))

#This for loop is between 1 until the value introduce plus 1, remember that the counter starts from 0
#The range function has two parametes, where it starts and when it finish
for i in range(1, value + 1):
    print('The current number is: ', i,' and his cube is: ', i ** 3)
