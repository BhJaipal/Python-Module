from Lib.main import *

nm: new_math = new_math;
print(f"Cube root of entered number is {nm.round(nm.cbrt(int(input('Enter a integer: '))))}")
"""
Enter a number: 1728
Cube root of entered number is 12
"""

print()
print(f"Logarithm addition of both numbers is {nm.logadd(int(input('Enter first number: ')), int(input('Enter second number: ')))}")
"""
Enter first number: 2
Enter second number: 3
Logarithm addition of both numbers is 0.7781 
"""

print()
print(f"Logarithm subtraction of both numbers is {nm.logsub(int(input('Enter first number: ')), int(input('Enter second number: ')))}")
"""
Enter first number: 3
Enter second number: 6
Numbers are swamped 
Logarithm subtraction of both numbers is 0.3010
"""

print()
notation.postfix("85+36-*")
# -39

notation.prefix('-9+43')
# 2

print()
matList= [[5, 3, 7], [4,7,2], [3,2,6]]
print(f"Matrix form of matrix list {matList} is: ")
matrix.matrix(matList)
print(f"\nTranspose of matrix list {matList} is: ")
matrix.mat_trans(matList)
print(f"\nDeterminant of matrix list {matList} is: ")
matrix.determin(matList)
"""
Matrix form of matrix list [[5, 3, 7], [4, 7, 2], [3, 2, 6]] is:
5  3  7
4  7  2
3  2  6

Transpose of matrix list [[5, 3, 7], [4, 7, 2], [3, 2, 6]] is:
5  4  3
3  7  2
7  2  6

Determinant of matrix list [[5, 3, 7], [4, 7, 2], [3, 2, 6]] is:
45
"""