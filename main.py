# # import ทั้งหมดทุกฟังก์ชัน Module
# import numbers

#import มาบางฟังก์ชัน
#from numbers import Factorial, Fibonacci
#import ทั้งหมดทุกฟังก์ชัน
#from numbers import*

# import และเปลี่ยนชื่อฟังก์ชัน (นามแฝง)alias
from number import Factorial as fa, Fibonacci as fi

# เรียกใช้งาน
# print(numbers.Factorial(5))
# print(numbers.Fibonacci(100))

print(fa(4))
print(fi(100))
