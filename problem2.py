distance=30
time=input("How many hours the trip took?: ")
try:
    hours=float(time)
    speed=(distance/hours)
    print(f"Average speed: {speed} km/h")
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("Time cannot be zero.")
