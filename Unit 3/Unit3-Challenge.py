print()
print("The South African Fuel Cost Calculator.")
print("---------------------------------------")
print("")

km = float(input("How many kilometers(km) are you driving: "))
current_price = float(input("What is the current petrol price per litre(L): R"))

litres_needed = km / 10

total_cost = round(litres_needed * current_price, 2)

print(f"Your Total Cost is: R{total_cost}")

