records = ["120", "95", "abc", "110", " 130 ", "", "8O"]
def valid_numbers(records):
    numbers=[]
    for record in records:
        try:
            number=int(record)
            numbers.append(number)
        except ValueError:
            pass
    return numbers
day=0
for record in records:
    day=day+1
    try:
        kg=int(record)
        print(f"Day {day}: {kg} kg")
    except ValueError:
        print(f"Day {day}: wrong record '{record}'")
numbers=(valid_numbers(records))
print(f"Correct record: {len(numbers)}")
print(f"Total: {sum(numbers)}")
print(f"Best day: {max(numbers)}")

    
