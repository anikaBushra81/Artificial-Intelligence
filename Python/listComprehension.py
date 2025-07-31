# list comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
fruits=["apple","banana","cherry","mango","kiwi"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
print("\n")

# With list comprehension you can do all that with only one line of code:
names=["anika","bushra","akhi","lamia"]
newlist1=[x for x in names if "m" in x]
print(newlist1)