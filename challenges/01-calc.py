# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calc():
    operator = input('What calculation would you like to do?(choose add,sub,mult, and div):')
    num1 = int(input('What is number 1:'))
    num2 = int(input('What is number 2:'))

    if operator == "add":
        result = num1 + num2
    elif operator == "sub":
        result = num1 - num2
    elif operator == "mult":
        result = num1 * num2
    elif operator == "div":
        result = num1 / num2
    else:
        return print("operation undefined")
    return print("Your result is", result)

calc()

