print("Welcome to the tip calculator!")
bill=float(input("what wwas your total bill?$ "))
tip_percentage=int(input("how much would you like to tip? 10, 12, or 15? "))/100
number_of_people=int(input("how many people? "))
final_bill_for_each_one=round(((bill+bill*tip_percentage) / number_of_people),2)
print(f"Each person should pay: {final_bill_for_each_one}")

