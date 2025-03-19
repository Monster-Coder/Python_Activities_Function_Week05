def display_menu():
    print("Menu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user():
    print("Hello! Welcome!")

def even_odd_checker_action():
    num = int(input("Enter an integer: "))
    print(check_even_odd(num))

def check_even_odd(number):
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."

def handle_menu_choice(choice):
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    return False

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-3): "))
        if handle_menu_choice(choice):
            break

main()
