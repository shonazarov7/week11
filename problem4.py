cost=25000
while True:
    number=input("How many portions? ")
    try:
        portions=int(number)
        if portions>1:
            break
        else:
            print("Please order at least 1 portion.")
    except ValueError:
        print("Please enter a whole number.")
total=cost*portions
print(f"{portions} portions of shivit oshi: {total} soum")
