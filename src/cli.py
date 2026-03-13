# WARNING: template code, may need edits
"""Command-line interface for the calculator."""

import sys
from src.calculator import Calculator
from src.operations import DivisionByZeroError


def print_menu():
    """Display the calculator menu."""
    print("\n" + "="*50)
    print("Python Calculator")
    print("="*50)
    print("Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (^)")
    print("  6. Modulo (%)")
    print("  7. View History")
    print("  8. Clear History")
    print("  9. Exit")
    print("="*50)


def get_number_input(prompt: str) -> float:
    """Get a valid number from user input.
    
    Args:
        prompt: The prompt to display
        
    Returns:
        A valid number
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    """Run the calculator CLI."""
    calc = Calculator()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == "9":
            print("\nThank you for using Python Calculator!")
            sys.exit(0)
        
        if choice == "7":
            history = calc.get_history()
            if history:
                print("\n--- Calculation History ---")
                for i, operation in enumerate(history, 1):
                    print(f"{i}. {operation}")
            else:
                print("\nNo history available.")
            input("\nPress Enter to continue...")
            continue
        
        if choice == "8":
            calc.clear_history()
            print("\nHistory cleared.")
            input("\nPress Enter to continue...")
            continue
        
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("\nError: Invalid choice. Please select 1-9.")
            input("\nPress Enter to continue...")
            continue
        
        # Get operands
        a = get_number_input("Enter first number: ")
        b = get_number_input("Enter second number: ")
        
        try:
            if choice == "1":
                result = calc.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
            elif choice == "2":
                result = calc.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
            elif choice == "3":
                result = calc.multiply(a, b)
                print(f"\nResult: {a} * {b} = {result}")
            elif choice == "4":
                result = calc.divide(a, b)
                print(f"\nResult: {a} / {b} = {result}")
            elif choice == "5":
                result = calc.power(a, b)
                print(f"\nResult: {a} ^ {b} = {result}")
            elif choice == "6":
                result = calc.modulo(a, b)
                print(f"\nResult: {a} % {b} = {result}")
        except DivisionByZeroError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
