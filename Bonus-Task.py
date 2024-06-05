from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class RunningSumCalculator:
    def __init__(self, nums):
        self.nums = nums

    def calculate_running_sum(self):
        running_sum_list = []
        current_sum = 0
        for num in self.nums:
            current_sum += num
            running_sum_list.append(current_sum)
        return running_sum_list

def get_user_input():
    while True:
        try:
            user_input = input(Fore.CYAN + "Enter the numbers separated by spaces: ").strip()
            nums = list(map(int, user_input.split()))
            if not nums:  # Check if the list is empty
                raise ValueError
            return nums
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a list of integers separated by spaces.")

def ask_continue():
    while True:
        continue_choice = input(Fore.CYAN + "Do you want to continue? (y/n): ").strip().lower()
        if continue_choice in ['y', 'n']:
            return continue_choice
        else:
            print(Fore.RED + "Invalid choice. Please enter 'y' for yes or 'n' for no.")

def main():
    print(Fore.MAGENTA + "Welcome to the Running Sum Calculator!")
    
    while True:
        nums = get_user_input()
        calculator = RunningSumCalculator(nums)
        running_sum_result = calculator.calculate_running_sum()
        print(Fore.GREEN + "Running Sum: " + str(running_sum_result))
        
        continue_choice = ask_continue()
        if continue_choice == 'n':
            print(Fore.GREEN + "Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
