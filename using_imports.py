# --- Importing standard and third-party modules ---
import random          # Built-in module for generating random numbers
import math            # Built-in module for mathematical operations
import os              # Provides functions for interacting with the operating system
import datetime        # Handles dates and times
import statistics      # Provides functions for statistical calculations
import matplotlib.pyplot as plt  # Popular third-party library for creating charts and graphs

# --- Importing your own module ---
import hello_world     # Custom module that contains a function named hello_world()

# --- Using random ---
number = random.randint(0, 10)   # Generate a random integer between 0 and 10
print(f"Random number between 0 and 10: {number}")  # Print the random number

# --- Using math ---
square_root = math.sqrt(number)  # Calculate the square root of the random number
print(f"The square root of {number} is approximately {square_root:.2f}")  # Display the result, rounded to 2 decimals

# --- Using os ---
current_directory = os.getcwd()  # Get the current working directory path
print(f"Current working directory: {current_directory}")  # Print the directory path

# --- Using datetime ---
current_time = datetime.datetime.now()  # Get the current date and time
print(f"The current date and time is: {current_time}")  # Print the current date and time

# --- Using statistics ---
data = [random.randint(1, 100) for _ in range(10)]  # Create a list of 10 random integers between 1 and 100
mean_value = statistics.mean(data)  # Calculate the average (mean) of the list
print(f"Random data: {data}")  # Display the random data list
print(f"Average value: {mean_value:.2f}")  # Display the mean, rounded to 2 decimals

# --- Using your custom module ---
hello_world.hello_world()  # Call the hello_world() function from your custom module

# --- Using matplotlib for a simple chart ---
plt.figure(figsize=(6, 4))  # Create a new figure window with a width of 6 and height of 4 inches
plt.plot(data, marker='o', color='teal')  # Plot the data points with teal circles connected by lines
plt.title("Random Data Chart")  # Add a title to the chart
plt.xlabel("Index")  # Label the x-axis
plt.ylabel("Value")  # Label the y-axis
plt.grid(True)  # Add a grid to the chart for readability
plt.show()  # Display the chart on the screen
