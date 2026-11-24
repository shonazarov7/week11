amount=input("How many melons?: ")
cost=15000
try:
    number=int(amount)
    total=cost*number
    print(f"Total :{total} soum" )
except ValueError:
    print("Please enter a whole number.")
print("Thank you!")