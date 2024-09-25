print("Welcome to the Trip Cost Calculator!")
#Input from user
days = float(input("How many days will you stay?"))
hotel = float(input("How much does hotel cost per night? $"))
flight = float(input("How much does flight cost? $"))
rental_car = float(
    (input("If you need rental car please enter the price otherwise enter zero. $"))
)
other_expense = float(input("Enter other expenses $"))
# Calculation of total cost
total = round((days * hotel) + flight +(days * rental_car) + other_expense,2)
print(f"Total Cost: ${total}")
