print("Welcome to our pizza delivery program.")
size=input("What sie do you want your pizza to be:\n if (Small) enter S, if (Medium) enter M and if (Large) enter L")
pepperoni=input("Do you want pepperoni if (Yes) enter y if (No) enter no")
extra_cheese=input("Do you want extra cheese if (Yes) enter y if (No) enter no")
bill=0

if size=="S":
    print("Your pizza is small.")
    bill=15
    if pepperoni == "y":
        bill += 2
elif size=="M":
    print("Your pizza is medium.")
    bill=20
    if pepperoni == "y":
        bill += 3
elif size=="L":
    print("Your pizza is large.")
    bill=25
    if pepperoni == "y":
        bill += 3
else:
    print("Enter again you enter was invalid")


if extra_cheese=="y":
    bill+=1

print(f"your total order comes to {bill}")