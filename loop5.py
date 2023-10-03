# i=0
# while i<9:
#     print(i)
#     i+=1
choice='y'
list=[]
while choice=='y':
    print('''
        1)add
        2)delete
        3)update
        4)display
        5)quit
          ''')
    option=input("enter your choice:")
    if option=='1':
        a=input("enter the activties:")
        list.append(a)
    elif option=='2':
        a=input("enter the activity to delete:")
        list.remove(a)
    elif option=='3':
        a=input("enter the activity to update:")
        b=int(input("enter the position:"))
        list[b]=a
    elif option=='4':
        for i in list:
            print(i)
    elif option=='5':
        exit()
    else:
        print("invalid choice")
# sum=0
# num1=int(input("enter the limit:"))
# for i in range(num1):
#     a=int(input("enter the element:"))
#     sum+=a
# print(sum)

list=[10,20,30,20,50]
for i in set(list):
   a=list.count(i)
   print(i, a)

    



     


    
    

 
