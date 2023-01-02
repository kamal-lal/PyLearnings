# Set
#   --> are unordered
#   --> are mutable, but elements must be immutable
#   --> elements are unique
#   --> very similar to the set theory in mathematics (venn diagrams stuff)


# ---- Declare Set ---- #
fruits = {'mango', 'apple', 'orange', 'banana'}
squares = {1, 4, 9, 16, 25}
some_set = {42, 'hammer', False, 3.14}
an_emptyset = set()
# not_an_emptyset = {}  # NB: this is a emply dictionary


# ---- Access set elements ---- #
# Set elements cannot be accessed individually.
# Can loop though set elements
# Membership operator (in / not in) works on set


# ---- Change values of elements in set ---- #
# Set elements can be changed once created.


# ---- Add elements to set ---- #
vehicles = {'car', 'bike', 'truck', 'bus', 'cycle', 'airplane', 'ship', 'helicopter'}
vehicles.add('boat')

# Add multiple elements
more_vehicles = ['scooter', 'tram']  # this can be list, tuple... (any iterable)
vehicles.add(more_vehicles)


# ---- Remove elements from set ---- #
# Removes element if exists. If not, raises error!
vehicles.remove('bus')

# Removes element if exists. If not, does nothing.
vehicles.discard('rikshaw')

# Remove a (random) element
vehicles.pop()  # popped item is returned and can be captured in a variable, if needed.


# ---- Get total number of element in set ---- #
element_count = len(vehicles)


# ---- Operations on set ---- #
s1 = {'a', 'b', 'c', 'd', 'e'}
s2 = {'d', 'e', 'f', 'g'}

# Union --> Elements either in s1 or s2
s_union_1 = s1 | s2
s_union_2 = s1.union(s2)

# Intersection --> Elements that are common in s1 and s2
s_intersec_1 = s1 & s2
s_intersec_2 = s1.intersection(s2)

# Difference --> Elements that are in s1, but not in s2.
s_diff_1 = s1 - s2
s_diff_2 = s1.difference(s2)

# isdisjoint --> returns True when s1 and s2 has no common elements
print(s1.isdisjoint(s2))

# issubset
print(s1 <= s2)
print(s1.issubset(s2))

# issuperset
print(s1 >= s2)
print(s1.issuperset(s2))
