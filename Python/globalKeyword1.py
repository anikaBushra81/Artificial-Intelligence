# To change the value of a global variable inside a function,
#  refer to the variable by using the global keyword
x="Anika"
def myFun():
    global x
    x="Bushra"
myFun()
print("hello "+x)