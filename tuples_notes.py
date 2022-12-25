# Tuples
#   --> are ordered
#   --> are immutable
#   --> elements can be accessed by index
#   --> can contain any arbitary objects


# ---- Declare Tuple ---- #
fruits = ('mango', 'apple', 'orange')
squares = (1, 4, 9, 16, 25)
some_tuple = (42, 'hammer', False, 3.14)
an_emptytuple1 = ()
an_emptytuple2 = tuple()

# Special case - Creating tuple with single element. Note the comma.
tup_with_single_element = (42,)


# ---- Access tuple elements ---- #
vehicles = ('car', 'bike', 'truck', 'bus', 'cycle', 'airplane', 'ship', 'helicopter')

# first element
print(vehicles[0])

# sixth element
print(vehicles[5])

# last element
print(vehicles[7])   # works for tuple of 8 elements
print(vehicles[-1])  # works for tuple of any size

# access range of elements
# Syntax: tuple_name[start:end:step]
print(vehicles[3:7])    # prints element 3, 4, 5, 6
print(vehicles[3:])     # prints element 3 to end
print(vehicles[:6])     # prints element begining to 5
print(vehicles[1:8:3])  # prints every third elemet between 1 and 7
print(vehicles[::2])    # prints every second element from whole tuple


# ---- Tuple's immutability ---- #
# Since tuples are immutable, some of the operations available for list is not available here.
#   - value assignment
#   - append
#   - insert
#   - extend
#   - pop
#   - remove
#   - sort


# ---- Get total number of element in tuple ---- #
element_count = len(vehicles)

# ---- Get number of elements with specified value ---- #
car_count = vehicles.count('car')

# ---- Get index of a specific element ---- #
car_index = vehicles.index('car')
