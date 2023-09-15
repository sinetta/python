# questions(set)
fruits={"apple","banana","cherry"}
fruits.add("pear")
print(fruits)
fruits.update({"mango","melon"})
print(fruits)
fruits.update({1,2,3})
print(fruits)
fruits.remove("cherry")
print(fruits)
s={1,2,3}
fruits.update(s)
print(fruits)
fruits.clear()
print(fruits)

# questions(dict)

d={"name":"rekha","age":23}
d.update({"place":"kochi"})
print(d)
d.pop("age")
print(d)
x=d.keys()
print(x)
s=d.values()
print(s)
d.clear()
print(d)
