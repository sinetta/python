#1 
# a=[2,7,6]
# target=8
# b=[]
# if a[0]+a[1]==target:
#     b.append(0)
#     b.append(1)
#     print(b)
# elif a[1]+a[2]==target:
#     b.append(1)
#     b.append(2)
#     print(b)
# elif a[0]+a[2]==target:
#     b.append(0)
#     b.append(2)
#     print(b)

# a=[2,7,1,5]
# target=12
# b=[]
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==target:
#             b.append(i)
#             b.append(j)
#             print(b)

#  9
# num=int(input("enter the number:")) 
# num2=num
# a=0
# while num>0:
#     n=num%10
#     a=a*10+n
#     num=num//10
# if a==num2:
#     print("true")
# else:
#     print("false")

#  27
# array=[2,4,7,2,6,3,7]
# value=2
# for i in array:
#     if i==value:
#         array.remove(i)
# print(len(array))

# 21
# num1=[2,4,5,6]
# num2=[1,3,6,7]
# num=num1+num2
# num=sorted(num)
# print(num)

# 5
# num=[1,2,6,6,8,8]
# a=set(num)
# b=list(a)
# print(len(b))
# b.sort()
# print(b)

# 58
# str="hello everyone"
# str1=str.split()
# str2=str1[-1]
# print(len(str2))

# 7
# list=[5,6,7,8]
# a=list[::-1]
# print(a)

# 26
# num=[1,3,4,5,3]
# num1=set(num)
# if num==num1:
#     print("false")
# else:
#     print("true")

# 14
# str=["sunlight","sunshine","sunrise"]

# 434
# str="hello, my name is Anu"
# str1=str.split()
# print(len(str1))

# 392
# str1="aeg"
# val="bcegra"
# for i in str1:
#    a=0
# if i in str1:
#     print("true")
# else:
#     print("false")

# 414 
# num=[2,4]
# num.sort()
# num1=num[-1]
# print("first distinct maximum is:",num1)
# num2=num[-2]
# print("second distinct maximum is",num2)
# if len(num)==2:
#     print("max=",num[-1])
# else:
#     num3=num[-3]
#     print("third distinct maximum is",num3)
            
# 415
str1="14"
str2="132"
str3=list(str1)
print(str3)




