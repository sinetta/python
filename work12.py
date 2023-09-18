# conditional statements

# a=15
# if a>0:
#     print("positive")
# else:
#     print("negative")

# b=int(input("enter a number:"))
# if b>0:
#     print("positive")
# else:
#     print("negative")

# c=int(input("enter a number:"))
# if (c%2==0):
#     print("number is even")
# else:
#     print("number is odd")
         
# d=input("enter a string:")
# if d.isalpha()==True:
#     print("d is a string")
# else:
#     print("d is not a string")

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# if a>b:
#     print( a,"is largest")
# else:
#     print(b,"is largest")

# x=int(input("enter your age:"))
# if (x<=18):
#     print("you are a minor")
# elif (x>18 and x<65):
#     print("you are an adult")
# else:
#     print("you are a senior citizen")

# x=int(input("enter first number:"))
# y=int(input("enter second number:"))
# if(x%y==0):
#     print(x,"is divisible by",y)
# else:
#     print(x,"is not divisible by",y)

# m=int(input("enter first number:"))
# n=int(input("enter second number:"))
# s=m+n
# if(s%2==0):
#     print(s,"is even")
# else:
#     print(s,"is odd")

x=input("enter a letter:")
v=("a","e","i","o","u","A","E","I","O","U")
if x in v:
    print(x,"is a vowel")
else:
    print(x,"is a consonant")
