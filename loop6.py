choice='y'
bank=[]
new_customer={}
while choice=='y':
    print('''
    1)add
    2)display     
    3)quit
          ''')
    option=int(input("enter your choice:"))
    if option==1:
        name=input("enter the name of employe:")
        new_customer["name"]=name
        age=int(input("enter the age:"))
        new_customer["age"]=age
        contact=int(input("enter the contact number:"))
        new_customer["contact no:"]=contact
        account=int(input("enter the account no:"))
        new_customer["acc no:"]=account
        new_customer["balance"]=0

        bank.append(new_customer.copy())
    if option==2:
        print(bank)
    