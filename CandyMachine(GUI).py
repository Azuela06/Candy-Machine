from tkinter import *
from tkinter import messagebox

# ********Main Window********
main = Tk()
main.title("Saur Sweet")
main.geometry("400x530")
main.configure(bg= "#E1C79B")
main.iconbitmap(r'favicon.ico')
bg = PhotoImage(file='logo2.png')
setBg = Label(main, image=bg, bg="#E1C79B").place(x=0,y=80, relheight=1, relwidth=1)
title = Label(main, text="Saur Sweet", font=("Bell Gothic Std Black",20, "italic", "bold"),
fg = "#40362c",bg = "#E1C79B",padx=5, pady=5).place(x = 125, y = 20)
title = Label(main, text="Welcome to Saur Sweet!", font=("Rosewood Std Fill",12, "bold"), 
fg = "#40362c",bg = "#E1C79B").place(x = 114, y = 60)
title = Label(main, text="Click on the chosen item you desire.", font=("Rosewood Std Fill",11), 
fg = "#40362c",bg = "#E1C79B",).place(x = 90, y = 95)
#********Classes***********
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
#*******Functions*********
def Exit2():        #for reseting the message after exiting the mini stores window
    window1.destroy()
    info.set(' ')
    paymentVar.set(' ')

def Exit():         #for destroyingthe main window
    main.destroy()

def viewBalance(pay):       #Balance Check
    balance = pay.currentBalance()
    bal.set(f'The balance the store currently have is {balance}.')
    name = Label(main, textvariable=bal, font=("Bell Gothic Std Black",11, "bold"),
    fg = "#40362c",bg = "#E1C79B").place(x = 50, y = 300)

def sellProduct(item, pay):     #Execution of the main code
        amount = payment.get()
        try:
            cost = item.getProductCost()
            product = item.getCount()
            if product > 0:
                custPay = int(amount)
                if custPay >= cost:
                    change = custPay - cost
                    info.set(f'Your change is {change}. Enjoy your delicacy!')
                    pay.acceptAmount(cost)
                    item.makeSale()
                    return 
                else:
                    toPay = cost - custPay
                    messagebox.showerror("Aww, Snap!","Your payment is deemed insufficient.")
                    info.set(f"You still need {toPay} cents to buy the delicacy.")
                    return
            else:
                messagebox.showinfo("Aww, Snap!","""Sorry the delicacy you 
                wanted is already sold out""")
                return
        except:
            messagebox.showerror("Error", "There's something wrong.")
    
def getCandy():     #window and selling of the candy
    global payment
    global window1
    window1 = Toplevel()
    window1.title("Candy Store")
    window1.geometry("270x270")
    window1.configure(bg= "#d9af80")
    name = Label(window1, text = "The Candy is worth 50 cents", font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 40, y = 30)
    name = Label(window1, text = "Enter your payment: ", font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 50, y = 60)
    payment = Entry(window1, textvariable = paymentVar,width = 15, bd = 2, font = ("Rosewood Std Fill",12), bg="#e0b87b")
    payment.place(x=60, y=90)
    okBtn = Button(window1, text="SUBMIT", font=("Courier New", 10, "bold"), 
    fg = "#3b332e", bg="#a1885a", width= 7, bd = 3, command = lambda: sellProduct(candy,cash)).place(x=50, y=150)
    name = Label(window1, textvariable=info, font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 10, y = 120)
    cancelbtn = Button(window1, text="EXIT", font=("Courier New", 10, "bold"), 
    fg = "#3b332e", bg="#a1885a", width= 7, bd = 3, command = Exit2).place(x=150, y=150)
    
def getChips():     #window and selling of the chips
    global payment
    global window1
    window1 = Toplevel()
    window1.title("Chips Store")
    window1.geometry("270x270")
    window1.configure(bg= "#d9af80")
    name = Label(window1, text = "The Chips is worth 50 cents", font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 40, y = 30)
    name = Label(window1, text = "Enter your payment: ", font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 50, y = 60)
    payment = Entry(window1, textvariable = paymentVar,width = 15, bd = 2, font = ("Rosewood Std Fill",12),bg="#e0b87b")
    payment.place(x=60, y=90)
    okBtn = Button(window1, text="SUBMIT", font=("Courier New", 10, "bold"), 
    fg = "#3b332e", bg="#a1885a", width= 7, bd = 3, command = lambda: sellProduct(chips,cash)).place(x=50, y=150)
    name = Label(window1, textvariable=info, font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 10, y = 120)
    cancelbtn = Button(window1, text="EXIT", font=("Courier New", 10, "bold"), 
    fg = "#3b332e", bg="#a1885a", width= 7, bd = 3, command = Exit2).place(x=150, y=150)

def getGum():     #window and selling of the gum
    global payment
    global window1
    window1 = Toplevel()
    window1.title("Gum Store")
    window1.geometry("270x270")
    window1.configure(bg= "#d9af80")
    name = Label(window1, text = "The Gum is worth 50 cents", font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 40, y = 30)
    name = Label(window1, text = "Enter your payment: ", font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 50, y = 60)
    payment = Entry(window1, textvariable = paymentVar,width = 15, bd = 2, font = ("Rosewood Std Fill",12),bg="#e0b87b")
    payment.place(x=60, y=90)
    okBtn = Button(window1, text="SUBMIT", font=("Courier New", 10, "bold"), 
    fg = "#3b332e", bg="#a1885a", width= 7, bd = 3, command = lambda: sellProduct(gum,cash)).place(x=50, y=150)
    name = Label(window1, textvariable=info, font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 10, y = 120)
    cancelbtn = Button(window1, text="EXIT", font=("Courier New", 10, "bold"), 
    fg = "#3b332e", bg="#a1885a", width= 7, bd = 3, command = Exit2).place(x=150, y=150)

def getCookie():     #window and selling of the cookie
    global payment
    global window1
    window1 = Toplevel()
    window1.title("Cookie Store")
    window1.geometry("270x270")
    window1.configure(bg= "#d9af80")
    name = Label(window1, text = "The Cookie is worth 50 cents", font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 40, y = 30)
    name = Label(window1, text = "Enter your payment: ", font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 50, y = 60)
    payment = Entry(window1, textvariable = paymentVar,width = 15, bd = 2, font = ("Rosewood Std Fill",12),bg="#e0b87b")
    payment.place(x=60, y=90)
    okBtn = Button(window1, text="SUBMIT", font=("Courier New", 10, "bold"), 
    fg = "#3b332e", bg="#a1885a", width= 7, bd = 3, command = lambda: sellProduct(cookies,cash)).place(x=50, y=150)
    name = Label(window1, textvariable=info, font=("Rosewood Std Fill",10, "bold"),
    fg = "#40362c",bg = "#d9af80").place(x = 10, y = 120)
    cancelbtn = Button(window1, text="EXIT", font=("Courier New", 10, "bold"), 
    fg = "#3b332e", bg="#a1885a", width= 7, bd = 3, command = Exit2).place(x=150, y=150)
#********items**********
candy = Dispenser()
chips = Dispenser()
gum = Dispenser()
cookies = Dispenser()
cash = Cash_Register()
#********Entries/Message*******
paymentVar = StringVar()
info = StringVar()
bal = StringVar()
#********Buttons*********
imgCndy = PhotoImage(file='candy.png')
imgChp = PhotoImage(file='chip.png')
imgGum = PhotoImage(file='gum.png')
imgCki = PhotoImage(file='cookie.png')
imgExt = PhotoImage(file='exit.png')
imgBal = PhotoImage(file='balance.png')
candyBtn = Button(main, image=imgCndy, bg="#E1C79B", borderwidth=0, command=getCandy).place(x = 100, y = 128)
chipBtn = Button(main, image=imgChp, bg="#E1C79B", borderwidth=0,command=getChips).place(x = 220, y = 128)
gumBtn = Button(main, image=imgGum, bg="#E1C79B", borderwidth=0,command=getGum).place(x = 100, y = 180)
cookieBtn = Button(main, image=imgCki, bg="#E1C79B", borderwidth=0,command=getCookie).place(x = 220, y = 180)
exitBtn = Button(main, image=imgExt, bg="#E1C79B", borderwidth=0, command= Exit).place(x = 100, y = 240)
balBtn = Button(main, image=imgBal, bg="#E1C79B", borderwidth=0, command= lambda: viewBalance(cash)).place(x = 220, y = 240)
#********execution*********
main.mainloop()