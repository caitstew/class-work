hours = float(input("Enter hours worked: "))
rate = float(input("Enter a pay rate without $: "))
earnings = (round(hours * rate,2)) #do this to control place
earnings = str(earnings)
print("You earned $" + earnings + "!")
