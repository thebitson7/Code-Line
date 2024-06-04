from colorama import *


init(autoreset=True)

def print_pattern():
    try:
        rows = int(input(Fore.CYAN + "Enter the number of rows for the pattern: "))  
        if rows <= 0:
            print(Fore.RED + "Please enter a positive number.")  
            return
        for i in range(1, rows + 1):
            print(Fore.YELLOW + '*' * i)
    except ValueError:
        print(Fore.RED + "Please enter a valid number.") 

def filter_numbers():
    try:
        numbers = input(Fore.CYAN + "Enter a list of whole numbers separated by spaces: ")  
        numbers_list = list(map(int, numbers.split()))
        filtered_list = [num for num in numbers_list if num < 13 or num > 19]
        print(Fore.GREEN + "Output: " + ' '.join(map(str, filtered_list)))
    except ValueError:
        print(Fore.RED + "Please enter valid numbers.")  

def show_help():
    help_message = """
--- Help ---
Option 1: Print a specific pattern with 'n' rows.
Option 2: Remove numbers between 13 and 19 from a list of whole numbers.
Option 3: Display this help message.
Option 4: Exit the program.
""" 
    print(Fore.BLUE + help_message)

def main():
    while True:
        print(Fore.MAGENTA + """
Welcome to the Menu-Based Program!
Please select an option:
1. Print Pattern
2. Filter Numbers
3. Help
4. Exit
""")
        option = input(Fore.CYAN + "Option: ")  
        
        if option == '1':
            print_pattern()
        elif option == '2':
            filter_numbers()
        elif option == '3':
            show_help()
        elif option == '4':
            print(Fore.GREEN + "Exiting the program. Goodbye!") 
            break
        else:
            print(Fore.RED + "Invalid option, please try again.")  

if __name__ == "__main__":
    main()
