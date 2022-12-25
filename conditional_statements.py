# Conditional Statements
# NB: The 'expression' below is somthing which evaluates to True or False

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
