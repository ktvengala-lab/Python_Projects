print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to spilt the bill? "))
tip_as_percent = tip_percentage/100
total_tip_amount = total_bill*tip_as_percent
total_bill_with_amount = total_tip_amount + total_bill
bill_per_person = total_bill_with_amount/number_of_people
final_amount = round(bill_per_person, 2)
total_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay :${total_amount}")