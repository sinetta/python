password=input("enter a password")
if len(password)>=8:
    if password.isdigit:
        alpha=True
    if password.isalnum:
         symbol=True
    if password.islower:
         lower=True
    if password.isupper:
         upper=True
if alpha and symbol and lower and upper:
     print("password is validated")
else:
     print("not validated")
