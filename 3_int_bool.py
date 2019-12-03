# Numerical types
## Numerical types are: integers, floats, composite


# declaring an int

num1 = 20
print(type(num1))

num2 = 20.0
print(type(num2))

# Mathematical operators (+, -, *, %, /) ---> These take priority over logical operators,
# however, use brackets to be sure

result1 = 10 + 34 # addition
result2 = 34 - 10 # subtract
result3 = 10 * 34 # multiplying
result4 = 34 % 10 # Finding the remainder
result5 = 30 / 10 # Dividing
print(result1, result2, result3, result4, result5)

# Logical operators
# One = is assignment
num_a = 10
num_b = 10
num_c = 13

# Bigger than --> returns a boolean (bool)
print(num_b > num_c)
print(num_c > num_a)
print(num_b <= num_a)
print(num_a >= num_c)
print(num_a != num_b)

#  Check if it is equal
## data type matters
print('10' == 10)
print(10 == 10)
print(num_b == num_a)

## Boolean
## True or False
print(type(True))
print(type(False))

bool_true = True
bool_false = False

print(bool_true == bool_false)
print(bool_true != bool_false)

# Logical AND (both statements need to true in order to true)
# logical OR (returns true if either statement is true)

print(True and False) # returns False
print(True or False) # returns True

