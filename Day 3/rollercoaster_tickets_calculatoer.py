print("Welcome to the rollercoaster")

height=int(input("Please enter your height in cm: "))
bill=0
if height>=120:

    age=int(input("Please enter your age: "))
    if age<= 12:
        print("Child tickets are $5.")
        bill=5
    elif age<= 18:
        print("Youth tickets are $7.")
        bill=7
    elif age >= 45 and age <= 55:
        print("you get tickets for free")
    else:
        print("Adults tickets are $12.")
        bill=12
    pics_takes=input("Do you want a pic to be taken if (Yes) enter y if (No) enter no: ")
    if pics_takes == "y":
        bill+=3
    print(f"Your final bill sums up to the total of ${bill}")

else:
    print("Sorry you can not enter the ride.")
