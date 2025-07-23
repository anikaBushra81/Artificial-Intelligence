# list are used to store multiple items in a single variable

# list is a build in datatype

# Lists are one of 4 built-in data types in Python used to store collections of data,
#  the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets

#  list is changeable, meaning that we can change, add, and remove items in a list after it has been created.



thislist=["apple","mango","dragon"]
print(thislist)

# allow duplicates
# Since lists are indexed, lists can have items with the same value

list1=["apple","banana","apple"]
print(list1)

# list length
# it determine how many items a list has
print(len(list1))

# list() constructor
#  list() constructor use when creating a new list
a=list(("apple","banana","apple"))
print(a)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# 1.List : is a collection which is ordered and changeable. Allows duplicate members.
# 2.Tuple : is a collection which is ordered and unchangeable. Allows duplicate members.
# 3.Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# 4.Dictionary: is a collection which is ordered** and changeable. No duplicate members.