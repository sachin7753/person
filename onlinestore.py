price = {"Lemonade": 10, "Coke": 20, "Fanta": 20, "Water": 5, "string": 2, "sprit":15}
shopping_basket = {}

print("Welcome to the online drink store!\nThese are the drinks we offer\n1. Lemonade:rs 10\n2. Coke:rs 20\n3. Fanta:rs 20\n4. Water:rs 5\n5.string=rs 2\n6.sprit:rs 15")

buy_another_flag = 1
total_cost, total = 0, 0

while buy_another_flag != 0:
    option = int(input("Which drink would you like to purchase?: "))

    if option == 1:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 10
        print("The price is: " + str(total))
    elif option == 2:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 20
        print("The price is: " + str(total))
    elif option == 3:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 20
        print("The price is: " + str(total))
    elif option == 4:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 5
        print("The price is: " + str(total))
    elif option == 5:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 2
        print("The price is: " + str(total))
    elif option == 6:
        qnty = int(input("Enter the quantity: "))
        total = qnty * 15
        print("The price is: " + str(total))    

    total_cost += total

    buy_another_flag = int(input("Would you like another item? enter Yes (1) or No (0):"))
    print("The total price of your basket is: ", total_cost)
