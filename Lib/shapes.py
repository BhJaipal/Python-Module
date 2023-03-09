import math
class Cuboid:
    def __init__(self, leng, brea, hei):
        self.leng = leng;
        self.brea= brea;
        self.hei = hei;
    def TotalSurfaceArea(self):
        return 2*(self.leng*self.brea + self.brea*self.hei + self.leng*self.hei);
    def LateralSurfaceArea(self):
        return 2*(self.leng +self.brea) *self.hei;
    def Volume(self):
        return self.leng * self.brea * self.hei;
    def lengthofDiagonal(self):
        return math.sqrt(self.leng**2 + self.brea**2 + self.hei**2);
    def execution(self):
        print(f"Total Surface Area: {self.TotalSurfaceArea()}");
        print(f"Lateral Surface Area: {self.LateralSurfaceArea()}")
        print(f"Volume: {self.Volume()}");
        print(f"length of Diagonal: {self.lengthofDiagonal()}");

class Cube():
    def __init__(self, side):
        self.side= side;
    def TotalSurfaceArea(self):
        return 6*(self.side ** 2);
    def LateralSurfaceArea(self):
       return 4*(self.side ** 2);
    def Volume(self):
        return self.side **3;
    def lengthofDiagonal(self):
        return self.side* 1.73;
    def execution(self):
        print(f"Lateral Surface Area: {self.LateralSurfaceArea()}");
        print(f"Total Surface Area: {self.TotalSurfaceArea()}");
        print(f"Volume: {self.Volume()}");
        print(f"length of Diagonal: {self.lengthofDiagonal()}");

class Sphere:
    def ____init__(self, radius):
        self.radius = radius;
    def SurfaceArea (self):
        return 4 * 3.14 * (self.radius**2);
    def Volume(self):
        return 1.67 * 3.14 * (self.radius**3);
    def execution(self):
        print(f"Surface Area: {self.SurfaceArea()}");
        print(f"Volume: {self.Volume()}");

class Cylinder:
    def __init__(self, radius, height):
        swlf.radius = radius;
        swlf.heigth = height;
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
