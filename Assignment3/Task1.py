a = int(input("Enter number: "))
factorial_value = 1

def factorial(a):
    global factorial_value
    if a != 0:
        factorial_value *= a
        factorial(a-1)
    return factorial_value

print(factorial(a))