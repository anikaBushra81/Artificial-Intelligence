# Change Item Value
List1=["cow","dog","bird"]
List1[2]="horse"
print(List1)

# Change a Range of Item Values
List2=["Rose","lily","lotus","water lily","marigold","jasmine"]
List2[2:4]=["orchid","tulip"]
print(List2)
# insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly


# Insert Items
list3=["apple","mango","banana"]
list3.insert(1,"watermelon")
print(list3)