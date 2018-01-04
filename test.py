
from master import basic_maths
from mat_tables import tables

myObject = basic_maths()
print ("Enter the first integer:")
a = int(raw_input())
print ("Enter the second integer:")
b = int(raw_input())
print ("Sum of the 2 integers is : %d" % (myObject.addTwoNumbers(a,b)))
print ("Multiplication of the 2 integers is : %d" % (myObject.multiplyTwoNumbers(a,b)))

print ("Enter the number you want the multiplcation tables for:")
mul_tab = int(raw_input())
tablesObj = tables()
tablesObj.generate_table(mul_tab)