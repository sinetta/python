# a=[2,9,4,3,5,1,7,6,8]
# a.sort()
# print(a[-2])
# print(a[1])

# b=list(input("enter a list"))

# b.sort()
# print(b[-1])
# print(b[1])


a= int(input("enter  number of elements:"))
b=[]
for i in range(a):
    c=int(input("enter the element:"))
    b.append(c)
b.sort()
print(b[-2])
print(b[1])
