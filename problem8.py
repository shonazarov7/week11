def read_quantity(text):
    try:
        quantity=int(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a whole number")
    if quantity<1:
        raise ValueError("quantity must be at least 1")
    return quantity
def order_price(order, prices):
    parts=order.split("x")
    if len(parts)!=2:
        raise ValueError ("use the format 'item x quantity'")
    item=parts[0].strip().lower()
    if item not in prices:
        raise ValueError (f",we do not sell {item}")
    quantity=read_quantity(parts[1])
    return prices[item]*quantity
prices = {"suzani": 400000, "plate": 120000, "hat": 90000}
orders = ["plate x 2", "Suzani x 1", "carpet x 1", "hat x two", "plate x 0", "hat 3", "hat x 3"]
total=0
wrong_orders=0
for order in orders:
    try:
        price=order_price(order,prices)
        print(f"{order}:{price} soum")
        total+=price
    except ValueError as error:
        print(f"{order}:error {error}")
        wrong_orders+=1
print(f"Total: {total} soum")
print(f"Wrong orders: {wrong_orders}")
