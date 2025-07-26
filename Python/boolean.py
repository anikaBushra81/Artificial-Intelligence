class myClass():
    def __len__(self):
        return 0
    def sum(self, a):
        return a+5
myObj=myClass()
print(bool(myObj))
print(myObj.sum(5))

# __len__() ..is a special method that tells Python how to determine the length of your object
# when we write somthing like len(myObj)
# python internally looks for tis method
# myObj.__len__()
# So if you define it in your class, Python will know how to calculate the "length" of your object