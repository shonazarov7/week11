rates = {"USD": 12000, "EUR": 14000, "RUB": 150}
def convert(amount, currency, rates):
    if amount<=0:
        raise ValueError ("amount must be positive")
    return amount*rates[currency]
requests = ["100 USD", "50 EUR", "2000 RUB", "30 GBP", "abc USD", "-20 EUR", "0 USD"]
total = 0
for request in requests:
    words = request.split()
    currency=words[1]
    try:
        amount=int(words[0])
        soum=convert(amount, currency, rates)
        print(f"{amount} {currency} = {soum} soum")
        total+=soum
    except ValueError:
        print(f"{request}: wrong amount")
    except KeyError:
        print(f"{request}: unknown currency")
print(f"Total: {total} soum")