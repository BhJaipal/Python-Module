# Lib.main

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

# Lib.shapes

## Cuboid

```python
import math 
class Cuboid:
    def __init__(self, length: float, brea: float, hei: float):
        self.length = len;
        self.brea= brea
        self.hei = hei;
    def TotalSurfaceArea(self):
        return 2*(self.length*self.brea + self.brea*self.hei + self.length*self.hei); 
    def LateralSurfaceArea(self):
        return 2*(self.length + self.brea)* self.hei;
    def Volume(self):
        return self.length * self.hei * self.brea;
    def lengthofDiagonal(self):
        return math.sqrt(math.pow(self.length, 2) + math.pow(self.brea, 2) + math.pow(self.hei, 2));
    def execution(self):
        print(f"Total Surface area: {self.TotalSurfaceArea()}")
        print(f"Lateral Surface area: {self.LateralSurfaceArea()}")
        print(f"Volume: {self.Volume()}")
        print(f"Length of Diagonal: {self.lengthofDiagonal()}")
```

**It has a constructor**

**It is used to get Total Surface area, Lateral Surface area, Volume, length of Diagonal and a execution method**

### __init__

It takes length, breadth and height of Cuboid 
```python 
from Lib.shapes import *;
len: float = 9;
brea: float= 8;
hei: float = 7;
cuboid: Cuboid = Cuboid(len, brea, hei);
```

### TotalSurfaceArea

it returns Total Surface area of Cuboid which is $$2×(l×b + l×h + h×b)\$$
```python
print(cuboid.TotalSurfaceArea())
```
`382`

### LateralSurfaceArea()

it returns Lateral Surface area of Cuboid which is $$2×(l + b)× h\$$
```python
print(cuboid.LateralSurfaceArea())
```
`238`

### Volume 

it returns Volume of Cuboid which is $$l×b×h\$$
```python
print(cuboid.Volume())
```
`504`

### lengthofDiagonal

it return length of Diagonal of Cuboid which is $$\sqrt{l&sup2; + b&sup2; + h&sup2;}\$$
```python
print(cuboid.lengthofDiagonal())
```
`13.92`

### execution

it prints the value returned by TotalSurfaceArea, LateralSurfaceArea, Volume, lengthofDiagonal 
```python
cuboid.execution()
```
```
Total Surface area: 382
Lateral Surface area: 238
Volume: 504
Length of Diagonal: 13.92
```

## Cube 

```python
class Cube:
    def __init__(self, side: float):
        self.side = side;
    def TotalSurfaceArea(self):
        return 6* self.side * self.side; 
    def LateralSurfaceArea(self):
        return 4* self.side* self.side;
    def Volume(self):
        return self.side * self.side * self.side;
    def lengthofDiagonal(self):
        return self.side* 1.73;
    def execution(self):
        print(f"Total Surface area: {self.TotalSurfaceArea()}")
        print(f"Lateral Surface area: {self.LateralSurfaceArea()}")
        print(f"Volume: {self.Volume()}")
        print(f"Length of Diagonal: {self.lengthofDiagonal()}")
```

**It has a constructor**

**It is used to get Total Surface area, Lateral Surface area, Volume, length of Diagonal and a execution method**

### __init__

It takes side of Cube

```python 
from Lib.shapes import *;
side: float= 8;
cube: Cube = Cube(side);
```

### TotalSurfaceArea

it returns Total Surface area of Cube which is $$6 × a&sup2;\$$

```python
print(cube.TotalSurfaceArea())
```

`384`

### LateralSurfaceArea()

it returns Lateral Surface area of Cube which is $$4 × a&sup2;\$$

```python
print(cube.LateralSurfaceArea())
```
`256`

### Volume 

it returns Volume of Cube which is $$a&sup3;\$$

```python
print(cube.Volume())
```

`512`

### lengthofDiagonal

it return length of Diagonal of Cube which is $$a × sqrt{3}\$$

```python
print(cube.lengthofDiagonal())
```
`13.84`

### execution

it prints the value returned by TotalSurfaceArea, LateralSurfaceArea, Volume, lengthofDiagonal
```python
cube.execution()
```
```
Total Surface area: 384
Lateral Surface area: 256
Volume: 512
Length of Diagonal: 13.84
```

Sphere

```python
class Sphere:
    def __init__(self, radius: float):
        self.radius = radius;
    def SurfaceArea (self):
        return 4 * 3.14 * (self.radius**2);
    def Volume(self):
        return 1.67 * 3.14 * (self.radius**3);
    def execution(self):
        print(f"Surface Area: {self.SurfaceArea()}");
        print(f"Volume: {self.Volume()}");
```

**It has a constructor**

**It is used to get Surface area, Volume and a execution method**

### __init__

It takes radius of Sphere
```python
from Lib.shapes import *;
radius: float= 7;
sphere: Sphere = Cube(side);
```

### SurfaceArea

it returns Surface area of Sphere which is $$4 × π × r&sup2;\$$
```python
print(sphere.TotalSurfaceArea())
```

`615.44`

### Volume 

it returns Volume of Sphere which is $$4/3 × π × r&sup3;\$$

```python
print(sphere.Volume())
```
`1798.6234`

### execution

it prints the value returned by SurfaceArea, Volume
```python
sphere.execution()
```

```
Surface area: 615.44
Volume: 1798.6234
```

## Cylinder

```python
class Cylinder:
    def __init__(self, radius: float, height: float):
        self.radius = radius;
        self.height = height;
    def TotalSurfaceArea(self):
        return 2* 3.14 * self.radius * (self.height + self.radius);
    def CurvedSurfaceArea(self):
        return 2* 3.14 * self.radius * self.height;
    def Volume(self):
        return 3.14 * (self.radius**2) * self.height;
    def execution(self):
        print(f"Total Surface Area: {self.TotalSurfaceArea()}");
        print(f"Curved Surface Area: {self.CurvedSurfaceArea()}");
        print(f"Volume: {self.Volume()}");
```

**It has a constructor**

**It is used to get Total Surface area, Curved Surface area, Volume and a execution method**

### __init__

It takes radius and height of Cylinder
```python 
from Lib.shapes import *;
radius: float= 7;
height: float= 3;
cylinder: Cylinder = Cylinder(radius, height);
```

### TotalSurfaceArea

it returns Total Surface area of Cylinder which is $$2 × π × r × (h + r)\$$
```python
print(cylinder.TotalSurfaceArea())
```
`439.6`

### CurvedSurfaceArea

it returns Curved Surface area of Cylinder which is $$2 × π × r × h\$$
```python
print(cylinder.CurvedSurfaceArea())
```
`131.88`

### Volume 

it returns Volume of Cylinder which is $$π × r&sup2; × h\$$
```python
print(cylinder.Volume())
```
`461.58`

### execution

it prints the value returned by TotalSurfaceArea, CurvedSurfaceArea, Volume
```python
sphere.execution()
```
```
Total Surface area: 439.6
Curved Surface area: 131.88
Volume: 461.58
```
