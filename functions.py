# functions
# - consists of function name, parameters.
# - starts "def" keyword.
# - Pptimizes and make a block of code reuseable.

# void function
# def averageOfThreeNumbers(num1, num2, num3):
#     #codes ...
#     average = (num1 + num2 + num3) / 3
#     print("Average: ", average)


# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)

# return function
title = "ang alamat ni Loudie"
title2 = ": Bagsak Era"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.upper()

def stringToLowercase(message):
    return message.lower()

def JoinString(message, message2):
    return message.join(message2)

def countLetters(message):
    return len(message)


print(stringToTitle(title))
print(stringToUppercase(title))
print(stringToLowercase(title))
# print(JoinString(title, title2))
print(countLetters(title))
