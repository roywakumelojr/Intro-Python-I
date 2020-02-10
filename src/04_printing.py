"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('%i' % (x))
print('%g, and %s' % (y, z))
print('x is %i, y is %g, z is %s' % (x, round(y, 2), z))

# Use the 'format' string method to print the same thing
print('{}'.format(x))
print('{}, and {}'.format(y, z))
print('x is {}, y is {}, z is {}'.format(x, round(y, 2), z))

# Finally, print the same thing using an f-string
print(f'{x}')
print(f'{y}, and {z}')
print(f'x is {x}, y is {round(y, 2)}, z is {z}')
