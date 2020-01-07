def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


try:
    user_number = int(input('Please enter a number: '))

    while collatz(user_number) != 1:
        user_number = collatz(user_number)
        print(user_number)

except ValueError:
    print('Error. The input number is not an integer.')

print(collatz(user_number))
