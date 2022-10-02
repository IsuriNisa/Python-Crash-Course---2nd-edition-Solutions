pizzas = ['Vegi Pizza', 'Cheese Pizza', 'Paneer Pizza']
friend_pizzas = pizzas[:]

# add a new item to pizzas
pizzas.append('Chicken Pizza')
# add a new item to friend_pizzas
friend_pizzas.append('Sausage Pizza')

# print pizzas
print(" My favorite pizzas are:")
for i in pizzas:
    print(i)
print("\n")
# print friend's list
print("My favorite pizzas are:")
for j in friend_pizzas:
    print(j)