def get_integer_input():
    num = int(input("Enter an integer: "))
    return num

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    num = get_integer_input()
    result = check_even_odd(num)
    print(result)

main()
