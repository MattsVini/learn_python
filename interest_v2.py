principle = 0
rate = 0
time = 0
number_period = 0
flag = 1
while flag:
    while principle <= 0:
        principle = float(input("Enter the with principal balance: "))
        if principle <= 0:
            print(f"You typed: {principle}. Need be bigger than zero")

    print(f"initial amount balance: {principle}")

    while number_period <= 0:
        number_period = int(input("How many for period: 1 = per year, 30 = per month or 365 = daily"))
        if number_period <= 0 and not type(principle) is int:
            print(f"You tiped:{number_period}. It's invalid, need be bigger than 0")

    print(f"Your period: {number_period}")

    rate = float(input("Rate: "))
    result_rate_elapsed = 1 + (rate/100)/number_period
    while time <= 0:
        time = int(input("How much times? "))
        if time <= 0 and not type(time) is int:
            print(f"You tiped {time}. Need be bigger than zero")
    result_final = principle * (result_rate_elapsed ** time)
    print(f"Initial principal balance: ${principle:.2f}\nInterest rate: ${rate:.2f}\nperiods elapsed: {number_period}\nTimes:{time}\nCurrent balance with interes rate: ${result_final:.2f}")
    flag = int(input("\n\n You would like to restart? Type 1 for yes / Type 0 for not "))
