from master import basic_maths

#Inherit the methods and variables from basic_maths class
class tables(basic_maths):
    rows = 10

# Generate multiplication table for 10 rows
    @classmethod
    def generate_table(cls,a):
        while (cls.rows):
            cls.rows = cls.rows-1
            n = 10-cls.rows
            print ("%d X %d = %d" %(n,a,cls.multiplyTwoNumbers(a,n)))
            return cls.generate_table(a)

