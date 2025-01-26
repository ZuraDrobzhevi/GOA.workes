





# Summing a number's digits

def sum_digits(number):
    return sum(int(i) for i in str(abs(number)) )