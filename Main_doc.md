## New_Math

### Round
**This function is for getting approximation** 

When decimal value of num is between 
0.25-0.8, it will print as they are.

```
>>>from Lib.main import *
>>>num= 7.4
>>>new_math.round(num)
7.4
```

If decimal value of num is lower than 
0.25, it will print their floor value.

```
>>>from Lib.main import *
>>>num2= 2.1
>>>new_math.round(num2)
2
```

If decimal value of num is greater than 0.8,
it will print their ceiling value
```
>>>from Lib.main import *
>>>num3= 6.8 
>>>new_math.round(num3)
7
```

### Cbrt
**This function is for getting Cuberoot of given number**

```
>>>from Lib.main import *
>>>new_math.cbrt(1728)
12
```
### Logadd
**This function is for getting addition of log values**

```
>>>from Lib.main import *
>>>new_math.logadd(2,3)
0.7781
```

### Logsub
**This function is for getting subtraction of log values**

```
>>>from Lib.main import *
>>>new_math.logsub(9,3)
0.4771
```

### About New_Math
**It is a attribute of Lib.main, it made for fulfillment of requirements, programmers require in math module**

## Matrix

### matrix
**This function is for getting matrix form of a list, tuple, and sets**

```
>>>from Lib.main import *
>>>matrix.matrix([2,5,7],[3,2,6],[4,7,2]]
2 5 7
3 2 6
4 7 2
```

