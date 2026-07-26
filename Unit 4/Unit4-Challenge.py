print()
print("The Smart ATM Withdrawal Simulator")
print("----------------------------------")

balance = 500

withdrawal = float(input("How much would you like to withdraw?: R "))

if withdrawal <= balance and withdrawal >= 1:
    total_left = round(balance - withdrawal, 2)
    print("Withdrawal successful!")
    print(F"Remaining Balance: R{total_left}")
elif withdrawal <= 0:
    print("Invalid Amount.")
    print("You must withdraw more than R0")
else:
    print("Declined! Insufficient funds!")