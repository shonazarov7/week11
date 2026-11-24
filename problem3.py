cost=20000
def ticket_price(tickets):
    if tickets<1 or tickets>4:
        raise ValueError ("you can buy from 1 to 4 tickets")
    return tickets*cost
tickets=int(input("Number of tickets: "))
try:
    price=ticket_price(tickets)
    print(f"Price: {price} soum")
except ValueError as error:
    print("Error:", error)