import random 
def get_random_code(length): 
    """Generate a random string of letters and digits of the specified length.""" 
    # Randomly select x letters and digits from the set of all such characters. 
    char = ''.join([chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)]). 
    return ''. join(random.sample(char * length, length)) 