sodas = ["coke", "sprite", "pepsi", "faygo"]
print("I am compiling a list of sodas. I currently have the sodas:\n ")
for soda in sodas:
	print(soda)
print("\n")

sodas.append(input("We can make this list longer! Please input a new soda and I will generate the new list: "))
for soda in sodas:
	print(soda)

