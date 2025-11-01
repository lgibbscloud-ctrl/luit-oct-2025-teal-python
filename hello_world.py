"""
hello_world.py
---------------
A simple Python module that prints a friendly greeting.
Demonstrates defining a function, using a main guard,
and including type hints for clarity.
"""

def hello_world() -> None:
    """
    Print a simple 'Hello World' message to the console.

    Returns:
        None
    """
    print("Hello World")  # Output greeting to the console


# The following condition ensures the code only runs
# when this file is executed directly, not when imported as a module.
if __name__ == "__main__":
    hello_world()  # Call the function to display the greeting

    