
class Cash_Register:
    def __init__(self, cashOnHand = 500): 
        if cashOnHand < 0:
            self.cashOnHand = 500
        else:
            self.cashOnHand = cashOnHand

    def currentBalance(self):
        return self.cashOnHand

    def acceptAmount(self, payment):
        self.cashOnHand += payment

class Dispenser:
    def __init__(self, cost = 50, numberOfItems = 50):
        self.cost = cost
        self.items = numberOfItems

    def getCount(self):
        return self.items

    def getProductCost(self):
        return self.cost

    def makeSale(self):
        self.items -= 1

class Candy:
    def showSelection(self):
        global choice
        choice = (int(input(''' **** Welcome to Sweet's Candy Shop **** 
        To select an item enter
        1. Candy
        2. Chips
        3. Gum
        4. Cookies
        0. View Balance
        9. Exit
        Enter a choice: ''')))

    def sellProduct(self, item, pay):
        cost = item.getProductCost()
        product = item.getCount()
        if product > 0:
            print(f'The chosen item still has {product} left inside the inventory.')
            payment = int(input(f'The chosen item costs {cost} cents, how much money do you have in hand?: '))
            try:
                print(f"I received {payment}.")
            except ValueError:
                print("The inputted value should be an Integer")
            if payment < cost:
                print(f'The payment we received was unsufficient, you still need {cost - payment} cents to buy the product.')
                proceed = input('Would you ike to add more money?(yes/no): ').upper()
                if proceed == 'YES':
                    add = int(input("Add a new value: "))
                    payment += add
                    change = payment - cost
                    print(f'Your change is {change}. Thank You!')
                    pay.acceptAmount(cost)
                    item.makeSale()
                else:
                    print("Thank you for visiting the shop!")
            else:
                change = payment - cost
                print(f'Your change is {change}. Thank You!')
                pay.acceptAmount(cost)
                item.makeSale()
        else:
            print(f'The chosen item is already sold out')

    def chosenProduct(self):
        candy = Dispenser()
        chips = Dispenser()
        gum = Dispenser()
        cookies = Dispenser()
        cash = Cash_Register()
        try:
            store = 'YES'
            while store == 'YES':
                self.showSelection()
                if choice == 1:
                    self.sellProduct(candy,cash)
                    store = input("Would you like to buy another?(yes/no): ").upper()
                elif choice == 2:
                    self.sellProduct(chips,cash)
                    store = input("Would you like to buy another?(yes/no): ").upper()
                elif choice == 3:
                    self.sellProduct(gum,cash)
                    store = input("Would you like to buy another?(yes/no): ").upper()
                elif choice == 4:
                    self.sellProduct(cookies,cash)
                    store = input("Would you like to buy another?(yes/no): ").upper()
                elif choice == 0:
                    print(f'The current balance is {cash.currentBalance()}')
                    store = input("Would you like to buy a product?(yes/no): ").upper()
                else:
                    print('Thank you for visiting the store!')
                    break
        except ValueError:
            print("The value should be an integer")

accessCandy = Candy()
accessCandy.chosenProduct()
                

