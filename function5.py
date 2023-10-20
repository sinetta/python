student_details={}
details=[]
teacher=[]
students=[]
while True:
    print('''
    1)enter details of student
    2)view details
    3)enter detaiils of teacher
    4)assign
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
            for j,k in i.items():
                print(j,":",k)
    elif choice==3:
        name=input("enter the name:")
        teacher.append(name)
    elif choice==4:
        std_no=int(input("enter the class:"))
        for i in details:
            students.append(i["class"])
        if std_no in students:
            for i in details:
                if i["class"]==std_no:
                    





