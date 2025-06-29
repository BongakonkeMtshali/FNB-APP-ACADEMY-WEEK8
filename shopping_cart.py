


foods = []
prices = []
total = 0

while True:
    food = input("Enter a Food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)

print("\n-------YOUR CART -------\n")

for food in foods:
    print(food)

print("\nTotal Price: ")
for price in prices:
    total += price

print(f"Your total is: R{total:.2f}")
