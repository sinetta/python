x="i am from outside world"

def local_scope():
    x="i am inside local scope "
    print(x)

def scope():
    print(x)

def global_scope():
    global x
    x='i am global scope'
    print(x)


print(x)
local_scope()
scope()
global_scope()

scope()
print(x)
local_scope()

