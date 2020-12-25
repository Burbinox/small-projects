# this is a function which solve "the simplest unsolvable math problem" named collatz problem.
# made by Hubert Grobelny
import sys

try:
    variable = int(input('put a number: '))
except ValueError:
    print("can't you just put a number? ")
    sys.exit()


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    if number % 2 == 1:
        number = 3 * number + 1
        print(number)
        return number


while variable != 1:
    variable = collatz(variable)
