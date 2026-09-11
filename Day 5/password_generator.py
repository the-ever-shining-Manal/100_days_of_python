import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
print("=========================================================")
num_letters=int(input('How many letters would you like in your password?\n'))
num_symbols=int(input('How many symbols would you like in your password?\n'))
num_numbers=int(input('How many numbers would you like in your password?\n'))
random_letters=[]
random_symbols=[]
random_numbers=[]

for i in range(num_letters):
    random_letters.append(random.choice(letters))
    i+=1
if num_symbols!=0:
    for i in range(num_symbols):
        random_symbols.append(random.choice(symbols))
if num_numbers!=0:
    for i in range(num_numbers):
        random_numbers.append(random.choice(numbers))

total_pass=random_letters+random_symbols+random_numbers
user_password=total_pass.copy()
random.shuffle(user_password)




print(total_pass)
print(user_password)
print(''.join(user_password))