# sort the list alphabetically
# sort() method that will sort the list alphanumerically, ascending, byy default
list1=["apple","pineapple","banana","mango"]
list1.sort()
print(list1)
print("\n")

# sort the list numerically
list2=[10,2,33,3,80]
list2.sort()
print(list2)
print("\n")

# sort the list descending
# To sort descending, use the keyword argument reverse = True
list3=["pineapple","apple","papaya","banana"]
list3.sort(reverse=True)
print(list3)
print("\n")

# customize sort function
# customize your own function by using the keyword argument "key = function"
def myfun(n):
    return abs(n-50)
listtt=[1,30,4,1000]
listtt.sort(key=myfun)
print(listtt)
print("\n")

# case insenitive sort
# by default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
list4=["bird","Horse","dog","Cat"]
list4.sort()
print(list4)
print("\n")

# we can use built-in functions as key functions when sorting a list.
# if you want a case-insensitive sort function, use str.lower as a key function
list5=["lily","rainlily","sunflower","Rose"]
list5.sort(key=str.lower)
print(list5)
print("\n")

# reverse order
list6=["pineapple","apple","papaya","banana"]
list6.reverse()
print(list6)
print("\n")

