bank={}
new=[]
account_no=1001
balance=0
acc=[]
def application(bank,balance,new,account_no):
    name=input("enter your name:")
    bank["name"]=name
    age=int(input("enter your age:"))
    bank["age"]=age
    contact_no=int(input("enter your contact:"))
    bank["contact_no"]=contact_no
    bank["account_no"]=account_no
    account_no+=1 
    bank["balance"]=balance
    new.append(bank.copy())
def account(new):
    for i in new:
            print('-'*15)
            for key , value in i.items():
                print(key,':',value)
            print('-'*15)
def newbalance(new,acc):
    acc_no=int(input("enter the acc_no:"))
    amount=int(input("enter the amount:"))
    for i in new:
        acc.append(i["account_no"])
        print(acc)
        if acc_no in acc:
            for i in new:
               if i["account_no"]==acc_no:
                   i["balance"]+=amount
        else:
            print("no account found")
def withdraw(new,acc):
    acc_no=int(input("enter the acc_no:"))
    amount=int(input("enter the amount:"))
    for i in new:
        acc.append(i["account_no"])
        print(acc)
        if acc_no in acc:
            for i in new:
               if i["account_no"]==acc_no:
                    if i["balance"]>=amount:
                       i["balance"]-=amount
                    else:
                        print("not possible")
        else:
            print("no account found")
def quit():
     exit()