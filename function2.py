bank={}
new=[]
account_no=1001
balance=0
while True:
    print('''
    1)create account
    2)view account
    3)add balance
    4)withdraw balance
    5)quit   ''')
    opt=int(input("enter your choice:"))
    if opt==1:
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
    elif opt==2:
        # print(new)
        
        for i in new:
            print('-'*15)
            for key , value in i.items():
                print(key,':',value)
            print('-'*15)
    elif opt==3:
        acc_no=int(input("enter the acc_no:"))
        amount=int(input("enter the amount:"))
        acc=[]
        for i in new:
            acc.append(i["account_no"])
        print(acc)
        if acc_no in acc:
            for i in new:
               if i["account_no"]==acc_no:
                   i["balance"]+=amount
        else:
            print("no account found")
    elif opt==4:
        acc_no=int(input("enter the acc_no:"))
        amount=int(input("enter the amount:"))
        acc=[]
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
    elif opt==5:
        exit()
    

            



            

            

                