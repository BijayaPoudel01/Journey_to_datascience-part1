#making atm machine.
balance = 50000
pincode = 1122
i = 0
limit = 3
while i < limit:
    pin = int(input("enter your pin code"))
    if pin == pincode:
        print("you have sucessfully entered atm machine")
        while True:
            print(("1.check balance"))
            print(("2.deposite balance"))
            print(("3.withdraw balance"))
            print("4.exit")
            print("5.change pin")
            choice=input("enter your choice:")
            if choice=="1":
                print(f"your balance is{balance}")
            elif choice=="2":
                amount=float(input("entr your deposit amount:"))
                if amount<=0:
                    print("invalid amount")
                else:
                    balance += amount
                    print(f"your new balance is{balance}")
            elif choice=="3":
                amount=float(input("enter your withdraw amount:"))
                if amount>balance:
                    print("insuffient balance")
                else:
                    balance-=amount
                    print(f"your new balance is:{balance}")
            elif choice=="4":
                print("thanks for visiting")
            elif choice=="5":
                old_pin=(int(input("enter your old pin")))
                new_pin=(int(input("enter your new pin")))
                type_again_newpin=(int(input("enter again")))
                if new_pin==type_again_newpin:
                    print("your new pin is set")
                else:
                    ("your pin doesnot match")

        break
    else:
        i+=1
        print(f"your pin is incorrect.you have left attempts={limit-i}")
if i ==limit:
    print("your account is temperorially blocked.try after 5 minutes.")
