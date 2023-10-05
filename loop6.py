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
    4)quit
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
        acc_no=int(input("enter the account number:"))
        a=int(input("enter the amount to add:"))
        for i in bank:
            if i==acc_no:
              new_customer["balance"]=balance+a

    

    