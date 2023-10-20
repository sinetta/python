choice='y'
bank=[]
new_customer={}
account_no=1
while choice=='y':
    print('''
    1)add
    2)display  
    3)add balance     
    4)withdraw
    5)quit
          ''')
    option=int(input("enter your choice:"))
    if option==1:
        name=input("enter the name of customer:")
        new_customer["name"]=name
        age=int(input("enter the age:"))
        new_customer["age"]=age
        contact=int(input("enter the contact number:"))
        new_customer["contact no:"]=contact
        new_customer["acc no:"]=account_no
        balance=0
        new_customer["balance"]=balance

        bank.append(new_customer.copy())
        account_no+=1
        
    elif option==2:
        print(bank)
    elif option==3:
        acc_no=int(input("enter the acc_no:"))
        amount=int(input("enter the amount:"))
        acc=[]
        for i in bank:
            acc.append(i["account_no"])
        print(acc)
        if acc_no in acc:
            for i in bank:
               if i["account_no"]==acc_no:
                   i["balance"]+=amount
        else:
            print("no account found")
    elif option==4:
        acc_no=int(input("enter the acc_no:"))
        amount=int(input("enter the amount:"))
        acc=[]
        for i in bank:
            acc.append(i["account_no"])
        print(acc)
        if acc_no in acc:
            for i in bank:
               if i["account_no"]==acc_no:
                    if i["balance"]>=amount:
                       i["balance"]-=amount
                    else:
                        print("not possible")
        else:
            print("no account found")
    elif option==5:
        exit()

    

    