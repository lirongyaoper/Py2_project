class MyDate:
     def __int__(self,year,month,day):
         self.year = year
         self.month = month
         self.day = day

     def __str__(self):
         print("str is called")
         return f"{self.year}-{self.month}-{self.day}"

     def __repr__(self):
         print("repr is called")
         return f"MyDate:{self.year}-{self.month}-{self.day}"

     def __eq__(self,other):
         print(f'__eq__')
         if not isinstance(other,MyDate):
             return False
         return self.year == other.year and self.month == other.month and self.day == other.day


def main():
    my_date_1 = MyDate(2022,11,3)
    my_date_2 = MyDate(2022,11,3)
    print(my_date_1)
    print(my_date_1 is my_date_2)
    print(my_date_1 == my_date_2)

if __name__ =='__main__':
    main()