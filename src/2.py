import random
def get_random_code():
    numbers = "1234567890"
    symbols = "!@#$%^&*"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ""
    for i in range(1, 10):
        password += random.choice(numbers)
        password += random.choice(symbols)
        password += random.choice(letters)
        return password