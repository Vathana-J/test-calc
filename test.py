from master import master_cls
myObject = master_cls()
print ("Enter the first integer:")
a = int(raw_input())
print ("Enter the second integer:")
b = int(raw_input())
print ("Sum of the 2 integers is : %d" % (myObject.addTwoNumbers(a,b)))