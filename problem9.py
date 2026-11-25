menus = {1: 150000, 2: 200000, 3: 280000}
def check_number(text, low, high):
    text=text.strip()
    try:
        number=int(text)
    except ValueError: 
        raise ValueError ("please enter a whole number")
    if number<low or number>high:
        raise ValueError (f"enter a number from {low} to {high}")
    return number
def ask_number(question, low, high):
    while True:
        answer=input(question)
        try:
            return check_number(answer,low,high)
        except ValueError as error:
            print(f"Error {error}")
day=ask_number("Day of the month(1-30):",1,30)
guests=ask_number("Number of guests(50-500)",50,500)
menu=ask_number("Which menu(1-3)? ",1,3)
total_price = guests * menus[menu]
deposit = total_price * 30 // 100
print(f"Booking: day {day}, {guests} guests, menu {menu}")
print(f"Total price: {total_price} soum")
print(f"Deposit: {deposit} soum")
        