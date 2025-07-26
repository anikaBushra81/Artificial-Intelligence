# Remove Specified Item
# If there are more than one item with the specified value, the remove() method removes the first occurrence
list1=["apple", "banana", "cherry", "banana"]
list1.remove("banana")
print(list1)

# Remove Specified Index
list2=["apple", "banana", "dragon", "banana"]
list2.pop(0)
print(list2)

# If you do not specify the index, the pop() method removes the last item.
list3=["apple", "banana", "dragon", "banana"]
list3.pop()
print(list3)


# "del" keyword also removes the specified index
list4=["apple", "banana", "dragon", "banana"]
del list4[2]

#clear the list
# The clear() method empties the list.
# The list still remains, but it has no content
list5=["apple", "banana", "dragon", "banana"]
list5.clear()
print(list5)