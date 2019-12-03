# List in python
# Lists are ordered by index
# Lists aka arrays or objects in JavaScript

# Syntax
    # Declare lists using []
    # Separate objects using ,

landlords = ['Sr. Julio', 'Jane', 'Alfred', 'Marksons']
print(landlords)
print(type(landlords))

# How to access 3rd landlord in the list
print(landlords[2]) # --> lists starts with 0

#accessing the 1st landlord
print(landlords[0])

# accessing the last landlord
print(landlords[-1])

cities = ['California', 'Rio de Janeiro', 'Melbourne', 'Manchester','Singapore']

# Reassign a index
cities[3] = 'Hawaii'
print(cities)

# Adding to the list: .append(object)
cities.append('LA')
print(len(cities))
print(cities)

# Adding and defining the index: .insert(index, object)
cities.insert(0, 'Lisbourn')
print(cities)

# Removing an item on the list: .pop(index)
cities.pop(3)
print(cities)

# List slicing
    # Used to manage lists

# Prints from index to end of list
print(cities[3:])

# Print from start to index of the list
print(cities[:3])

# Prints from specified index (inclusive) to second specified index (not inclusive)
print(cities[0:3])

# Skip slicing
print(cities[0::2])
# Reverse list
print(cities[::-1])

# Tuples
# Immutable lists
# Syntax
    # Defined using (obejct, object)
mortal_enemies = ('Mario', 'Sailormoon', 'Moon Cake', 'Jerry', 'Berry')
# tuple--> round brackets, list --> square brackets
print(type(mortal_enemies))
# if you try to reassign object in tuple it will break

# Prompting users to input the items in list
list_of_kit = []
item_1 = input('What is your first item to keep?')
list_of_kit.append(item_1)
item_2 = input('What is your second item to keep?')
list_of_kit.append(item_2)
item_3 = input('What is your last item to keep?')
list_of_kit.append(item_3)
print(list_of_kit)