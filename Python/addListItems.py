# Append items
# item add end of the list
list1=["bushra","Akhi"]
list1.append("lamia")
print(list1)

# insert items
# insert a list item at a specified index
list1.insert(1,"sathi")
print(list1)

# extend list
# append elements from another list to the current list, use the extend() method.
list2=["apple","banana","mango"]
a=["bird","butterfly","cat"]
list2.extend(a)
print(list2)

# Add any iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
list3=["rose","lily"]
c=("jesmin","orchid")
list3.extend(c)
print(list3)

