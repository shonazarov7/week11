fees = {5: 30000, 10: 50000, 21: 80000}
def entry_fee(age, distance, fees):
    if age<16:
        raise ValueError ("runners must be at least 16")
    if distance not in fees:
        raise ValueError (f"there is no {distance} km race") 
    fee=fees[distance]
    if age>=60:
        fee=fee/2
    return fee
runners = [["Aziz", 19, 10], ["Malika", 15, 5], ["Jasur", 25, 42], ["Dilnoza", 64, 21], ["Sardor", 33, 5]]
registered_count = 0
total_fees = 0
for name, age, distance in runners:
    try:
        fee = entry_fee(age, distance, fees)
        print(f"{name}: {fee} soum")
        registered_count += 1
        total_fees += fee
    except ValueError as error:
        print(f"{name}: not registered, {error}")
print(f"Registered runners: {registered_count}")
print(f"Total fees: {total_fees} soum")
   
    
