

# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
if name.strip() == "":
  print("Invalid name.")
  name = input("Enter passenger name: ")
  
distance = float(input("Enter distance (km): "))
if not (0 <= int(distance)):
   print("Distance has to be more than 0. Please try again.")
   distance = float(input("Enter distance (km): "))

try:
  passengers = int(input("Enter number of passengers: "))
  if not passengers.isaldigit():
    print("Please input it in numbers/whole number.")
    passengers = int(input("Enter number of passengers: "))
except ValueError:
  print("Please input it in numbers/whole number.")
  passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number


