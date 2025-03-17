# assignment: programming assignment 2
# author: Shreya Hiremath
# date: 07/12/2022
# file: shop.py implements a vending machine
# input: strings and numbers (integers)
# output: interactive messages (strings)

print("Vending Machine")
while True:
    # step 1: print the menu and get the user's choice
    # step 2: depending on the user's choice, update product_price and product_name (variables that keep track of the user's choice), 
    # or quit the program, or reprint the menu


    choice = input ( """Please enter what product you want to buy[1-3] or select quit[4]: 
1. A bottle of water - $1.99 
2. A bottle of orange juice - $2.15 
3. A bottle of iced tea - $2.49 
4. Quit \n""" )

    
    if choice == '1':
        product_price = 199
        
        

    elif choice == '2':
        product_price = 215
        

    elif choice == '3':
        product_price = 249

            
    elif choice == '4':
        print("Goodbye!")
        quit

        break
        

    else:
    
        print( "You made the wrong choice!")

        continue

        

    # step 3: ask for deposit

   


    deposit = 0

    while deposit < product_price:

        n1 = float(input("Please deposit money (in cents): \n"))

        deposit = deposit + n1


    if choice == '1':
        print("You bought a bottle of water. \n")

        

    if choice == '2':
        print("You bought a bottle of orange juice. \n")

        

    if choice == '3':
        print("You bought a bottle of iced tea. \n")
            

        
        

  

        
    # step 4: calculate change, we use a greedy algorithm (approach) to get the minimum number of coins 
    change = deposit - product_price

    if change > 0:
        print("Your change is: ")
        
    dollars = change // 100   # get the quotient Quotient - Wikipedia (Links to an external site.)
    change = change % 100     # get the remainder Remainder - Wikipedia (Links to an external site.)
    quarters = change // 25
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    change = change % 5
    cents = change
    # step 5: print the selected product and change



    if dollars > 0:
        print("Dollars - " , int(dollars))

    if quarters > 0:
        print("Quarters - " , int(quarters))

    if dimes > 0:
        print("Dimes - " , int(dimes))

    if nickels > 0:
        print("Nickels - " , int(nickels))

    if cents > 0:
        print("Cents - " , int(cents))
        
