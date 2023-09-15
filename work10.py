# set

s={1,2,1,"abc",6.5}
print(s)
a={22,56,77,56,77,"d","fg","dd"}
print(a)

# # add items

s={1,2,1,"abc",6.5}
s.add(20)
print(s)
s.update([7,8])
print(s)
s.update("keys","light")
print(s)
s.update(["keys","light"])
print(s)
s.remove("keys")
print(s)

# dictionary
s={"name":"anu","age":22,"roll.no:":22}
print(s)
print(s["name"])
s["name"]="kunju"
print(s)
s.update({"place":"adoor"})
print(s)