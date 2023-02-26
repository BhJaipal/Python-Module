import math
from Lib.main import new_math
class Cuboid:
    def __init__(self, length, brea, hei):
        self.length = length;
        self.brea= brea;
        self.hei= hei;
    def cuboid_tsa(self):
        return 2* (self.length * self.brea + self.brea * self.hei+ self.length * self.hei);
        # Total Surface area of Cuboid = 
        #              2 * (l*b + b*h + l*h)

    def cuboid_lsa(self):
        return 2* self.hei*(self.length+self.brea);
        # Lateral Surface area of Cuboid = 
        #                     2 * (l + b) *h
        
    def cuboid_volume(self):
        return self.length * self.hei * self.brea;
        # Volume of Cuboid = l*b*h
        
    def cuboid_diagonal(self):
        return new_math.round(math.sqrt(math.pow(self.length,2) + math.pow(self.brea,2) + math.pow(self.hei, 2)));
        # Diagonal of Cuboid = 
        #   square root of (l^2 + b^2 + h^2)
        
    def execu(self):
        print("*************** Cuboid ***************");
        print("Total Surface area of Cuboid: ", self.cuboid_tsa());
        print("Lateral Surface area of Cuboid: ", self.cuboid_lsa());
        print("Volume of Cuboid: ", self.cuboid_volume());
        print("Diagonal of Cuboid: ", self.cuboid_diagonal());
        print("**************************************");

class Cube:
    def __init__(self, side):
        self.side= side;
    
    def cube_volume(self):
        return math.pow(self.side,3);
        # Volume of Cube = a ^ 3
    
    def cube_lsa(self):
        return 4* self.side**2;
        # Lateral Surface area of Cube = 
        #                           4 * a^2
    
    def cube_tsa(self):
        return 6* self.side**2;
        # Total Surface area of Cube = 
        #                           6 * a^2
    
    def cube_diagonal(self):
        return self.side* 1.732;
        # Diagonal of Cube = a * 1.732
    
    def execu(self):
        print("*************** Cube ***************");
        print("Total Surface area of Cube: ", self.cube_tsa());
        print("Lateral Surface area of Cube: ", self.cube_lsa());
        print("Volume of Cube: ", self.cube_volume());
        print("Diagonal of Cube: ", self.cube_diagonal());
        print("************************************");

class Sphere:
    def __init__(self, radius):
        self.radius = radius;
        
    def sphere_tsa(self):
        return new_math. round(4* 22/7 * math.pow(self.radius,2));
        # Surface area of sphere= 4*pi* (radius)^2
    
    def sphere_volume(self):
        return 1.67 * 22/7 * math.pow(self.radius,3);
        # Volume of sphere= 4/3*pi*(radius)^3
    
    def execu(self):
        print("*************** Sphere ***************");
        print("Total Surface area of Sphere: ", self.sphere_tsa());
        print("Volume of Sphere: ", self.sphere_volume());
        print("**************************************");

class Cylinder:
    def __init__(self, radius, height):
        self.radius= radius;
        self.height= height;
    
    def cylinder_tsa(self):
        return 2* 22/7 * self.radius *(self.height + self.radius);
        # Total Surface area of Cylinder = 
        #       2*pi*radius *(height + radius)
    
    def cylinder_csa(self):
        return 2* 22/7 * self.radius* self.height;
        # Curved Surface area of Cylinder = 
        #               2*pi * radius *height
    
    def cylinder_volume(self):
        return 22/7 * math.pow(self.radius,2)* self.height;
        # Volume of Cylinder = 
        #           pi * (radius)^2 * height
    def execu(self):
        print("*************** Cylinder ***************");
        print("Total Surface area of Cuboid: ", self.cylinder_tsa());
        print("Curved Surface area of Cuboid: ", self.cylinder_csa());
        print("Volume of Cuboid: ", self.cylinder_volume());
        print("****************************************");
while True:
    choice= int(input("Choose any one: \n1. Sphere \n2. Cube \n3. Cuboid \n4. Cylinder\n5. Exit \nEnter your choice number: "))
    print("\n");
    if choice ==1:
        mySphere= Sphere(int(input("Enter radius: ")));
        mySphere.execu();
    elif choice ==2:
        myCube = Cube(int(input("Enter side: ")));
        myCube.execu();
    elif choice ==3:
        myCuboid = Cuboid(int(input("Enter length: ")), int(input("Enter breadth: ")), int(input("Enter height: ")));
        myCuboid.execu();
    elif choice ==4:
        myCylinder= Cylinder(int(input("Enter radius: ")), int(input("Enter height: ")));
        myCylinder.execu();
    elif choice ==5: break;
    else:
        print("Only these 4 3D shapes are available");
    cont = input("Do you want to continue? [Yn]: ");
    print();
    if cont.lower()== "n": break;