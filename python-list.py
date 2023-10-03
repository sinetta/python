# a=10
# b=20

# if a>b:
#     print("a is greater")
# elif a==b:
#     print("they are equal")
# else:
#     print("b is greater")

a=float(input("enter the amount:"))
if a>=100:
    amount=((10/100)*a)
    print(amount)
elif a>=50 and a<=99.9:
    amount=((5/100)*a)
    print(amount)
else:
    print(a)

# year=int(input("enter a year:"))
# if (year%4)==0 or (year%100)!=0 and (year%400)==0:
#     print("leap year")
# else:
#     print("not a leap year")
    
# temp=float(input("enter the temperature:"))
# unit=input("enter the unit in celsius or fahrenheit:")
# if unit=="celsius":
#     temp=(temp*1.8)+32
#     print(temp,"fahrenheit")
# elif unit=="fahrenheit":
#     temp=(temp-32)*1.8
#     print(temp,"celsius")
# else:
#     print("enter a valid unit")

secret_number=79
guess=int(input("enter a number between 1-100:"))
if guess>secret_number:
    print("too high")
elif guess<secret_number:
    print("too low")
else:
    print("correct")



    