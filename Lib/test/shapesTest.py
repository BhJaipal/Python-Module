from Lib.main import *
from Lib.shapes import *

rad: int= 21;
Sphere(rad).execution()
"""
Surface area: 5538.96
Volume: 48562.8318
"""

print()
cuboidObj: Cuboid = Cuboid(4.2, 6.9, 3.4)
print(f"Length of Diagonal: {new_math.round(cuboidObj.lengthofDiagonal())}")
# Length of Diagonal: 8.7641

print()
print(new_math.round(Cylinder(7, 5.7).TotalSurfaceArea()))
# 558.292
