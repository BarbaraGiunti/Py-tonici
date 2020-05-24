user_input = input('Type a number:')
try:
    # Try do do something that could fail.
    user_input_as_number = float(user_input)
except ValueError:
    # This will be executed if a ``ValueError`` is raised.
    print('You did not enter a number.')
else:
    # This will be executed if not exception got raised in the
    # ``try`` statement.
    print('The square of your number is ', user_input_as_number**2)
finally:
    # This will be executed whether or not an exception is raised.
    print('Thank you')

def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age