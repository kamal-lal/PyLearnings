# Dictionaries
#   --> are key-value paris
#   --> are mutable
#   --> are dynamic
#   --> can be nested
#   --> elements are accesed by keys (not index)


# ---- Declare Dictionary ---- #
# Syntax: dict_name{key1:value1, key2:value2, ....}
# NB: Keys in a dictionary must be unique
student_1 = {'name': 'Bob', 'age': 21, 'hobbies': ['surfing', 'music', 'reading']}

# Create dictionary step-by-step
student_2 = {}
student_2['name'] = 'Alice'
student_2['age'] = 22
student_2['hobbies'] = ['movies', 'travel']

# Keys need not be strings. Can be other data-types too.
example_dict = {101: 'a', 201: 'b', 301: 'c', 401: 'd'}

# ---- Accessing Dictionary elements ---- #
print(student_1['name'])
print(student_2['hobbies'])
print(example_dict[301])
# print(student_1['email'])   # raises KeyError

print(student_1.get('name'))                 # prints Bob
print(student_1.get('email'))                # prints None
print(student_1.get('email', 'Not found!'))  # prints Not Found!


# ---- Dictionary built-in methods ---- #
# Get value of a key if key exists
student_1.get('name')

# Get all keys
student_1.keys()

# Get all values
student_1.values()

# Remove an element from dict (if key exists) and return its associated value
s1_age = student_1.pop('age')
student_1.pop('email')                  # raises KeyError
student_1.pop('email', 'Not found!')    # prints Not Found!

# Remove last key-value pair (and return it as tuple)
student_2.popitem()

# Merge dict with another dict
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)   # {'a': 10, 'b': 200, 'c': 30, 'd': 400}
