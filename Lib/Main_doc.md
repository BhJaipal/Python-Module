## New_Math

### Round
**This function is for getting approximation** 

When decimal value of num is between 
0.25-0.85, it will print as they are.

```python
>>> from Lib.main import *
>>> num= 7.4
>>> new_math.round(num)
7.4
```

If decimal value of num is lower than 
0.25, it will print their floor value.

```python
>>> from Lib.main import *
>>> num2= 2.1
>>> new_math.round(num2)
2
```

If decimal value of num is greater than 0.85,
it will print their ceiling value
```python
>>> from Lib.main import *
>>> num3= 6.87 
>>> new_math.round(num3)
7
```

### Cbrt
**This function is for getting Cuberoot of given number**

```python
>>> from Lib.main import *
>>> new_math.cbrt(1728)
12
```
### Logadd
**This function is for getting addition of log values**

```python
>>> from Lib.main import *
>>> new_math.logadd(2,3)
0.7781
```

### Logsub
**This function is for getting subtraction of log values**

```python
>>> from Lib.main import *
>>> new_math.logsub(9,3)
0.4771
```

### About New_Math
**It is an attribute of Lib.main, it made for fulfillment of requirements, programmers require in math module**

## Matrix

### Matrix
**This function is for getting matrix form of a list, tuple, or sets**

```python
>>> from Lib.main import *
>>> matrix.matrix([[2,5,7],[3,2,6],[4,7,2]])
2 5 7
3 2 6
4 7 2
```

### Mat_trans
**This function is for getting transpose of matrix form of list, tuple or set**

```python
>>> from Lib.main import *
>>> matrix.mat_trans([[2,5,7],[3,2,6],[4,7,2]])
2 3 4
5 2 7
7 6 2
```

### determin
**This function is for getting determinant of a matrix form of list, tuple or set**

```python
>>> from Lib.main import *
>>> matrix.determin([[2,5,7],[3,2,6],[4,7,2]])
105
```

### About Matrix 
**Matrix is an attribute of Lib.main, it is for making matrix, transpose of matrix and determinant of list, tuple or set**

## Notation

### Prefix 
**This function is for getting solution of a given Prefix format question, question should be given in string data type**

```python
>>> from Lib.main import *
>>> notation.prefix("+25")
7
>>> notation.prefix("/93")
3
```

### Postfix
**This function is for getting solution of a given Postfix format question, question should be given in string data type**

```python
>>> from Lib.main import *
>>> notation.postfix("97-")
2
>>> notation.postfix("23*")
6
```

### About Notation
**Notation is an attribute of Lib.main, it is made for getting solution of questions given in Prefix or Postfix equation and is complete in 0.3.9**
