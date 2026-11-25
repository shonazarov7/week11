menus = {1: 150000, 2: 200000, 3: 280000}
def check_number(text, low, high):
    text=text.strip()
    try:
        number=int(text)
    except ValueError: 
        ("please enter a whole number")
    if number<low or number>high:
        raise ValueError ("enter a number from 1 to 30")
    return number
def ask_number(question, low, high):
    