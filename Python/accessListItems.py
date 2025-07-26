# "----Access list items------"
# List items are indexed and you can access them by referring to the index numbe
a=[1,2,3,4]
print(a[3])


# "----negative indexing------"
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
print(a[-3])


#---"Range of Indexes"----
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

b=[2,3,4,5,6,7,8,1]
# position 1 theke position 6 porjonto print korbe
print(b[1:7])

# position 0 theke position 2 porjonto output a dekhabe
print(b[:3])

print('end val: ', b[len(b)-1])
print('end val: ', b[-1])

print(b[-4:-1])

#check if item exists
c=["cow","dog","bird","horse"]
if "bird" in c:
    print("Yes bird is here")