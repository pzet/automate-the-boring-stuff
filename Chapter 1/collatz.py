def collatz(user_number):
    try:
        number = int(user_number)
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1
    except ValueError:
        return 'Input must be an integer.'



input_number = input('Enter a number: ')

print(collatz(input_number))
