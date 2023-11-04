from master import *
while True:
    print('''
    1)create account
    2)view account
    3)add balance
    4)withdraw balance
    5)quit   ''')
    opt=int(input("enter your choice:"))
    if opt==1:
       application(bank,new,account_no,balance)
    elif opt==2:
        account(new)
    elif opt==3:
      newbalance(new,acc)
    elif opt==4:
       withdraw(new,acc)
    elif opt==5:
       quit()