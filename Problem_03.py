def get_non_negative_integer():
    num = int(input("Enter a non-negative integer: "))
    while num < 0:
        print("Invalid input. Please enter a non-negative integer.")
        num = int(input("Enter a non-negative integer: "))
    return num

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    num = get_non_negative_integer()
    result = calculate_factorial(num)
    print(f"The factorial of {num} is: {result}")

main()
