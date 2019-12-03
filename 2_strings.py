# Strings!

## Define strings - using ' ' and " "
my_string = "I'm learning python"
my_string2 = 'This is a string'

print(my_string)
print(type(my_string2))

# Concatenation - Joining two string
print(my_string + ' and ' + my_string2)
print('These are examples of strings', my_string, my_string2)

Concatenate = my_string2 + '  ' + my_string
print(Concatenate)

# Interpolation
age = 22
name = 'Rahavi'

## This is <> where we need to interpolate

print('Welcome <person>, you are <age> years old')
print('Welcome <person>, you were born on the year <birth_year>')

## This is how you interpolate

print(f'Welcome {name}, you are {age} years old')
print(f'Welcome {name}, you were born on the year {2019-age}')

print('Welcome {}, you were born on the year {}'.format(name,age))

## useful method for string
example_string = "Hello!"
print(example_string)

print(example_string.strip()) # Remove trailing white spaces
print(example_string.count('l')) # Counts number of characters on string
print(example_string.lower()) # lowercase
print(example_string.upper()) # uppercase
print(example_string.capitalize())

# Learning and using .spilt()

text_to_spilt = 'this is some example text in our file '
results_spilt = text_to_spilt.split(' ')
print(results_spilt)

# Casting and int
str_number = '1990'
print(type(str_number))

# str --> int
int_number = int(str_number)
print(type(int_number))

# int --> str
int_number1 = 2019
print(type(int_number1))
str_number1 = str(int_number1)
print(type(str_number1))
