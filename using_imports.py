# --- Importing standard and third-party modules ---
import random          # for random numbers
import math            # for math functions
import os              # for interacting with the operating system
import datetime        # for working with dates and times
import statistics      # for calculating averages and more
import matplotlib.pyplot as plt  # for creating visual charts

# --- Importing your own module ---
import hello_world

# --- Using random ---
number = random.randint(0, 10)
print(f"Random number between 0 and 10: {number}")

# --- Using math ---
square_root = math.sqrt(number)
print(f"The square root of {number} is approximately {square_root:.2f}")

# --- Using os ---
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# --- Using datetime ---
current_time = datetime.datetime.now()
print(f"The current date and time is: {current_time}")

# --- Using statistics ---
data = [random.randint(1, 100) for _ in range(10)]
mean_value = statistics.mean(data)
print(f"Random data: {data}")
print(f"Average value: {mean_value:.2f}")

# --- Using your custom module ---
hello_world.hello_world()

# --- Using matplotlib for a simple chart ---
plt.figure(figsize=(6, 4))
plt.plot(data, marker='o', color='teal')
plt.title("Random Data Chart")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
