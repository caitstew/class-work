prompt = input("Please provide a number: ")
prompt = int(prompt)
if prompt % 10 == 0: #not sure why need double equal sign
	print("You chose a multiple of ten!")
else:
	print("You did not choose a multiple of ten.")