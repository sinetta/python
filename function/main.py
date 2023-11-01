import master
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
choice=int(input('''1.addition
                 2.subtraction
                 3.multiplication
                 4:division'''))
if choice==1:
    master.add(num1,num2)
elif choice==2:
    master.diff(num1,num2)
elif choice==3:
    master.pro(num1,num2)
elif choice==4:
    master.div(num1,num2)