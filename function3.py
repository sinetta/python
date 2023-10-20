student_details={}
details=[]
teacher=[]
students=[]
regst_no=1001
while True:
    print('''
    1)enter details
    2)view details
    3)teacher's details
    4)view
    5)quit
    ''')
    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter your name:")
        student_details["name"]=name
        age=int(input("enter your age:"))
        student_details["age"]=age
        student_details["regst_no"]=regst_no
        regst_no+=1
        details.append(student_details.copy())
    elif choice==2:
        for i in details:
            for j,k in i.items():
                print(j,":",k)        
    elif choice==3:
        name=input("enter your name:")
        teacher.append(name)
        # dept=input("enter the dept:")
        # teacher["dept"]=dept
    elif choice==4:
        st_name=input("enter the name:")
        for i in details:
            students.append(i["name"])
        if st_name in students:
            for i in details:
                if i["name"]==st_name:
                    for j in teacher:
                        i["teacher"]=j
                    print(details)
    elif choice==5:
        exit()
    



        

    
        
        
                

        



        

           
    
        
         
             
                        

           
            
           

        
            
            
            
    
             
       

    
        
    
    


