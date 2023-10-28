student_details={}
details=[]
teacher=[]
students=[]
fees=12000
while True:
    print('''
    1)enter details of student
    2)view details
    3)enter detaiils of teacher
    4)assign
    5)fees     
    6)incharge
    7)display
    ''')
    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter the name:")
        student_details["name"]=name
        age=int(input("enter the age:"))
        student_details["age"]=age
        std=int(input("enter the class:"))
        student_details["class"]=std
        details.append(student_details.copy())
    elif choice==2:
        for i in details:
            print('-'*15)
            for j,k in i.items():
                print(j,":",k)
            print('-'*15)
    elif choice==3:
        name=input("enter the name:")
        teacher.append(name)
    elif choice==4:
        st_class=int(input("enter the class:"))
        for i in details:
            students.append(i["class"])
            if st_class in students:
                for i in details:
                    if i["class"]==st_class:
                        i["teacher"]=teacher[0]
                    else:
                        i["teacher"]=teacher[1]
        print(details)
    elif choice==5:
        st_name=input("enter the name:")
        cls=int(input("enter the class:"))
        for i in details:
            students.append(i["name"])
        amount=int(input("enter the amount:"))
        if st_name and cls in students:
            for i in details:
                if st_name==i["name"] and cls==i["class"]:
                    i["paid"]=amount
                    i["balance"]=fees-amount
                    if i["balance"]==0:
                        i["balance"]="fees completed"
            print(details)
        else:
            print("student not found")

    elif choice==6:
        tea_name=input("enter teacher's name:")
        if tea_name in teacher:
            for i in details:
                if i["teacher"]==tea_name:
                    print(i["name"])   
        else:
            print("not found")
    elif choice==7:
        for i in details:
            print('-'*15)
            print("name :",i["name"])
            print("paid fees :",i["paid"])
            print("balance :",i["balance"])
            print('-'*15)

        
        

        
            

        
        
        

        
        


        
        
                    
            



                    





