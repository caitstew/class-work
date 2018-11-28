pizzas = ["pepperoni", "cheese", "veggie"]

for pizza in pizzas:
	print("I love " + pizza +" pizza!\n")
print("I really love all kinds of pizza!")

friend_pizzas = pizzas[:]
pizzas.append("garlic")
friend_pizzas.append("barbeque chicken")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
	
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)

