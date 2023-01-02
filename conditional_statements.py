# Conditional Statements
# NB: The 'expression' below is somthing which evaluates to True or False

# General Notes:
# In addition to the obvious options such as Boolean literals(True, False),
# comparison operations ( < , <= , > , >= , == , != ) etc. the following statements
# could also give a True / False result.
#
# True result with membership operators `in` / `not in`:
#     'ing' in 'learning'
#     'xyz' not in 'learning'
#     42 in [12, 22, 32, 42, 52]
#     99 not in (12, 22, 32, 42, 52)
#
# False result with membership operators `in` / `not in`:
#     'xyz' in 'learning'
#     42 not in [12, 22, 32, 42, 52]
#     99 in (12, 22, 32, 42, 52)
#
# The following items evaluates to False.
#     Integer value - 0
#     Complex num - 0+0j
#     Empty string, list, tuple, dict etc.
#
# The following evalutes to True.
#     Zero and non zero float - 0.0, 4.8, -0.2
#     Non zero integer value - 37, -3
#     Non zero complex num - 3-5j
#     Non empty string, list, tuple, dict etc.


# IF statement
# Syntax:
# if <expression>:
#     do_something
#     do_something
#     do_something
# do_rest_of_stuff

create_log = True
user_name = 'admin'

if create_log:
    print(f'[INFO] User "{user_name}" successfully logged in.')

print(f'Welcome, {user_name}!')


# IF..ELSE statement
# Syntax:
# if <expression>:
#     do_something
#     do_something
#     do_something
# else:
#     do_anotherthing
#     do_anotherthing
#     do_anotherthing
# do_rest_of_stuff

minutes = 130

if minutes > 60:
    hr = minutes // 60
    mn = minutes % 60
    print(f'Total time is {hr} hrs, {mn} mins.')
else:
    print(f'Total time is {minutes} mins.')


# IF..ELIF..ELSE statement
# Syntax:
# if <expression_1>:
#     do_thing_a
#     do_thing_a
# elif <expression_2>:
#     do_thing_b
#     do_thing_b
# elif <expression_3>:
#     do_thing_c
#     do_thing_c
# else:
#     do_anotherthing
#     do_anotherthing
# do_rest_of_stuff

num = -12

if num > 0:
    print("It is a positive number.")
elif num < 0:
    print("It is a negative number.")
else:
    print("It is zero.")
