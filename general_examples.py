
'''
Topic   :   RANGE
Goal    :   Take two numbers and produce several number between them and turn them into a list
'''
x = range (3,20,2) 
y=[*x] 

# Equivalent to 
y = [*range (3,20,2)]

print(y) # Output: [3, 5, 7, 9, 11, 13, 15, 17, 19]


'''
Topic   :   Loops
'''
# Goal  :   For loop with numbers
num_01 = [5,6,8,4,9,7,1]

for n in num_01:
    print('number is: {0}'.format(n) )

print("For Loop Over")

# Goal :    For loop with string
str_01 = ['Tim', 'Tom', 'Jack', 'Jone']

for st in str_01:
    print('Welcome back, {0}!'.format(st))
    print('How have you been?')

print("For Loop Over")

# Goal  :   Iterating over a range with a step and prinitng the output
for r_01 in range(5):
    print(r_01)


# Goal  :   Iterating over a range with a step and prinitng the output
for r_02 in range(3,20,2):
    print(r_02)


'''
Topic           :   Coloured Text Output
Package Name    :   colored
Installation    :   pip install colored 
'''
# Goal  :   To get colored outputs
from colored import fg, bg, attr 

print('{0}Hello There{1}'.format(fg('red'), attr(0)))

print('{0}{1}Hi Man!!{2}'.format(fg('blue'), bg('red'), attr(0)))


'''
Topic   :   Functions
'''

def sum(a,b):
    value = a+b
    return value

total=sum(5,6)

print('Total Vlaue is: {0} '.format(total))

# Equivalent Code

def sum(a,b):
    return a+b

print('Total Vlaue is: {0} '.format(sum(5,6)))