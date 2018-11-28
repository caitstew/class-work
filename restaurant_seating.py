prompt = input("How many people are in your dinner group? ")
print("You listed " + prompt + " people.")
prompt = int(prompt)
if prompt >= 9:
	print("\nYou'll have a bit of a wait for a table.")
else: 
	print("\nYour table is ready.")