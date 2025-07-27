#loop through a list
# oop through the list items by using a for loop
list1=["apple", "banana","mango"]
for x in list1:
    print(x)
print("\n")

# Loop Through the Index Numbers
# loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
list2=["apple", "banana","mango"]
for i in range(len(list2)):
    print(list2[i])
print("\n")


# Using a While Loop
list3=["apple", "banana","mango"]
i=0
while i<len(list3):
    print(list3[i])
    i=i+1
print("\n")

# Looping Using List Comprehension
list4=["apple", "banana","mango"]
[print(x)for x in list4]
print("\n")