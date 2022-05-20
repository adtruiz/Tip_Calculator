print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
billTip = int(input("What percentage tip would you like to give? 10, 12, or 12? "))
splitPeople = int(input("WHow many people to split the bill? "))

payAmount = "{:.2f}".format((totalBill + (totalBill * (billTip / 100)))/splitPeople)


print(f"Each person should pay: ${payAmount}")