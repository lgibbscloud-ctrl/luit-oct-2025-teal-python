import random
import string

ec2_amount = int(input("How many instances do you need names for?\n"))
department = input("What is the name of you department?\n")

def generate_random_characters():
  return (''.join(random.choices(string.ascii_letters + string.digits, k=5)))

print("Here are your names:")

for x in range(ec2_amount):
  result = generate_random_characters()
  print(department + "_" + result)

