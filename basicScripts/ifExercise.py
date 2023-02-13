'''Calculating grades of school'''

value = int(input('Introduce the grade to measure: '))

if(value > 90):
    print('Is an A')
elif(value > 80 and value < 90):
    print('Is a B')
elif(value > 70 and value < 80):
    print('Is a C')
elif(value > 60 and value < 70):
    print('Is a D')
else:
    print('Is a F')
