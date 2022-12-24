# Lists

# Declare List
fruits = ['mango', 'apple', 'orange', 'banana']
squares = [1, 4, 9, 16, 25]
some_list = [42, 'hammer', False, 3.14]

# - Access list elements
vehicles = ['car', 'bike', 'truck', 'bus', 'cycle', 'airplane', 'ship', 'helicopter']

# -- first element
print(vehicles[0])

# -- sixth element
print(vehicles[5])

# -- last element
print(vehicles[7])   # works for list of 8 elements
print(vehicles[-1])  # works for list of any size

# -- access range of elements
# Syntax: list_name[start:end:step]
print(vehicles[3:7])    # prints element 3, 4, 5, 6
print(vehicles[3:])     # prints element 3 to end
print(vehicles[:6])     # prints element begining to 5
print(vehicles[1:8:3])  # prints every third elemet between 1 and 7
print(vehicles[::2])    # prints every second element from whole list

# - Add elements to list

# -- Add element at end of list
vehicles.append('boat')

# -- Add element at a specified position
vehicles.insert(2, 'cycle')  # Note: insert item at 3rd position

# -- Extends list
more_vehicles = ['scooter', 'tram']
vehicles.extend(more_vehicles)

# - Remove elements from list

# -- Remove last element
vehicles.pop()

# NB: 'pop' also returns the popped item.
removed_item = vehicles.pop()

# -- Remove element at specified position
vehicles.pop(4)

# -- Remove a specific element
vehicles.remove('ship')

# - Sort a list
# NB: These sorts the list 'in-place'. Thus original list is gone.
vehicles.sort()              # sorts Ascending order
vehicles.sort(reverse=True)  # sorts Descending order

# NB: this one, sorts and returns a new list. So original list remains as it is.
vehicles_sorted = sorted(vehicles)
vehicles_sorted = sorted(vehicles, reverse=True)

# - Get total number of element in list
element_count = len(vehicles)

# - Get number of elements with specified value
car_count = vehicles.count('car')

# - Get index of a specific element
car_index = vehicles.index('car')
