import math
import copy

"""
Personal Python Module
"""
def __init__():
    return "This is a Python file used as a personal python module "
def new():
    return "Prefix and Postfix notation are now complete"

"""
Use of New_Math class

Use of round() function
It round off value to its nearest integer in a limited range
>>> from Lib.main import *
>>> new_math.round(8.9)
9
>>> new_math.round(1.2)
1
>>> new_math.round(5.6)
5.6

Use of cbrt() functions
Use to get cube root
>>> new_math.cbrt(1728)
12

Use of logadd() function
Use for log addition
>>> new_math.logadd(2,3)
0.7781

Use of logsub(10,5) function
Use for log subtraction
>>> 0.3010
"""

class new_math:
    def round(num):
        f= math.floor(num)
        r1= num-f
        if r1> 0.8:
            return math.ceil(num)      # round off to greater integer
        elif r1< 0.25:
            return math.floor(num)     # round off to lower integer
        else:
            return (num)               # present in middle range thus it will not be changed
    cbrt = lambda num: round(num**(1/3))
    """ because math module uses log base e also called natural log or ln,
    to convert it to log base 10, we divide it with math.log(10) or ln(10)"""
    def logadd(a,b):
        lga=math.log(a)/math.log(10)   # gets log base 10 value of a
        lgb=math.log(b)/math.log(10)   # gets log base 10 value of b
        return lgb+lga
    def logsub(a,b):
        div=round(a/b)                # as log(a) - log(b)= log(a/b), div= a/b
        lgsb=math.log(div)/math.log(10)  # lgsb is log(div) where div=a/b
        return lgsb
    def __init__():
        return "This class is for attribute which you want in math module but don't have "

"""
Use of matrix class

Use of matrix() function
Used to print a matrix form list into matrix
>>> mat=[[2,5,7],[3,2,6],[4,7,2]]
>>> from Lib.main import *
>>> matrix.matrix(mat)
2 5 7
3 2 6
4 7 2
 
Use of mat_trans() function
Used of print a matrix formed list into transpose of its matrix
>>> matrix.mat_trans(mat)
2 3 4
5 2 7
7 6 2

Use of determin() function
>>> matrix.determin(mat)
105
"""

class matrix:
    def matrix(mtx_list):
        for row in mtx_list:
            for elem in row:
                print (elem,end="  ")        # print elements of matrix list
            print ()
    def mat_trans(mt_list):
        mtx_list= copy.copy(mt_list)
        for n in range(len(mtx_list)):
            i=0
            mtx_list[n][i], mtx_list[i][n]=mtx_list[i][n], mtx_list[n][i]     # swapping elements position aij=aji, where i, j= (3,1),(1,3),(2,3),(3,2)
            if n!=0:
                i+=1
                mtx_list[n][i], mtx_list[i][n]=mtx_list[i][n], mtx_list[n][i]   # swapping elements position aij=aji, where i, j= (1,2),(2,1)
        for row in mtx_list:
            for elem in row:
                print (elem,end="  ")
            print ()
    def determin(mtx_list):
        co11= mtx_list[1][1]*mtx_list[2][2]- mtx_list[1][2]*mtx_list[2][1]     # cofactor of a11
        co12= mtx_list[1][0]*mtx_list[2][2]- mtx_list[1][2]*mtx_list[2][0]     # cofactor of a12
        co13= mtx_list[1][0]*mtx_list[2][1]- mtx_list[1][1]*mtx_list[2][0]     # cofactor of a13
        if len(mtx_list) ==2:
            print (co11- co12)
        else:
            print (co11*mtx_list[0][0]- co12*mtx_list[0][1]+ co13*mtx_list[0][2])
    def __init__():
        return "This class is for making matrix in python "

"""
Use of notation class

Use of prefix() function
Used to calculate a prefix equation for 2 integers
>>> from Lib.main import *
>>> notation.prefix("*23")
6
>>> notation.prefix("/+235")
1
>>> notation.prefix("/9*52")
0.9
>>> notation.prefix("/*26*34")
1

Use of postfix() function
Used to calculate postfix equation
>>> notation.postfix("94%")
1
>>> notation.postfix("23*5%")
1
>>> notation.postfix("952*/")
0.9
>>> notation.postfix("26*34*/")
1
"""

class notation:
    def postfix(nota1):
        notalist=list(nota1)
        if len(notalist) == 3:
            if notalist[2] == "+":
                sum= int(notalist[0])+ int(notalist[1])       # ab+ = a+b
                print (sum)
            elif notalist[2] == "-":
                sub= int(notalist[0])- int(notalist[1])       # ab- = a-b
                print(sub)
            elif notalist [2] == "*":
                mul= int(notalist[0])* int(notalist[1])       # ab* = a*b
                print (mul)
            elif notalist [2] == "%":
                Mod= int(notalist[0])% int(notalist[1])       # ab% = a%b
                print(Mod)
            else:
                div= int(notalist[0])/ int(notalist[1])       # ab/ = a/b
                print (div)
        
        if len(notalist) == 5:
            if notalist[2] in list("+-*%/"):
                """
                equation for this is ab*c/ = (a*b)/c, you can use +-*/% operators 
                """
                # solving 1st postfix
                if notalist[2] == "+":
                    solv= int(notalist[0]) + int(notalist[1])
                elif notalist[2] == "-":
                    solv= int(notalist[0]) - int(notalist[1])
                elif notalist[2] == "*":
                    solv= int(notalist[0]) * int(notalist[1])
                elif notalist[2] == "%":
                    solv= int(notalist[0]) % int(notalist[1])
                else:
                    solv= int(notalist[0]) / int(notalist[1])
                # solving main postfix
                if notalist[4] == "+":
                    solution= solv + int(notalist[3])
                elif notalist[4] == "-":
                    solution= solv - int(notalist[3])
                elif notalist[4] == "*":
                    solution= solv * int(notalist[3])
                elif notalist[4] == "/":
                    solution= solv / int(notalist[3])
                else:
                    solution= solv % int(notalist[3])
                print(solution)
            elif notalist[3] in list("+-*%/"):
                """
                equation for this is abc*/ = a/(b*c), you can use +-*/% operators 
                """
                if notalist[3] == "+":
                    solv= int(notalist[1]) + int(notalist[2])
                elif notalist[3] == "-":
                    solv= int(notalist[1]) - int(notalist[2])
                elif notalist[3] == "*":
                    solv= int(notalist[1]) * int(notalist[2])
                elif notalist[3] == "/":
                    solv= int(notalist[1]) / int(notalist[2])
                else:
                    solv= int(notalist[1]) % int(notalist[2])
                # solving main postfix
                if notalist[4] == "+":
                    solution = int(notalist[0]) + solv
                elif notalist[4] == "-":
                    solution = int(notalist[0]) - solv 
                elif notalist[4] == "*":
                    solution = int(notalist[0]) * solv 
                elif notalist[4] == "/":
                    solution = int(notalist[0]) / solv 
                else:
                    solution = int(notalist[0]) % solv 
                print(solution)
            else:
                return "Please enter correct equation in abc*/ format or ab*c/, you can use */+-%"

        if len(notalist) == 7:
            """
            equation for this is ab*cd*/ = (a*b)/(c*d), you can use +-*/% operators
            """
            # for 1st postfix
            if notalist[2]=="+":
                calc1= int(notalist[0]) + int(notalist[1])
            elif notalist[2]=="-":
                calc1= int(notalist[0]) - int(notalist[1])
            elif notalist[2]=="*":
                calc1= int(notalist[0]) * int(notalist[1])
            elif notalist[2]=="/":
                calc1= int(notalist[0]) / int(notalist[1])
            else:
                calc1= int(notalist[0]) % int(notalist[1])
            # 1st postfix is done
            # now, for second postfix
            if notalist[5]== "+":
                calc2= int(notalist[3]) + int(notalist[4])
            elif notalist[5]== "-":
                calc2= int(notalist[3]) - int(notalist[4])
            elif notalist[5]== "*":
                calc2= int(notalist[3]) * int(notalist[4])
            elif notalist[5]=="/":
                calc2= int(notalist[3]) / int(notalist[4])
            else:
                calc2= int(notalist[3]) % int(notalist[4])
            # 2nd postfix is also done
            # now for main prefix
            if notalist[6]=="+":
                result= calc1 + calc2
            elif notalist[6]=="-":
                result= calc1 - calc2
            elif notalist[6]=="*":
                result= calc1 * calc2
            elif notalist[6]=="/":
                result= calc1 / calc2
            else:
                result= calc1 % calc2
            print(result)
    
    def prefix(nota1):
        notalist =list(nota1)
        if len(notalist) == 3:
            if notalist[0] == "+":
                sum=int(notalist[1]) + int(notalist[2])      # +ab = a+b
                print (sum)
            elif notalist[0] == "-":
                sub= int(notalist[1])- int(notalist[2])      # -ab = a-b
                print(sub)
            elif notalist[0] == "*":
                mul= int(notalist[1])* int(notalist[2])      # *ab = a*b
                print(mul)
            elif notalist[0] == "%":
                Mod= int(notalist[1])% int(notalist[2])      # %ab = a%b
                print(Mod)
            else:
                div= int(notalist[1])/ int(notalist[2])      # /ab = a/b
                print(div)

        if len(notalist) == 5:
            if notalist[1] in list("+-*%/"):
                """
                equation for this is /*abc = (a*b)/c, you can use +-*/% operators
                """
                # solving 1st postfix
                if notalist[1] == "+":
                    solv= int(notalist[2]) + int(notalist[3])
                elif notalist[1] == "-":
                    solv= int(notalist[2]) - int(notalist[3])
                elif notalist[1] == "*":
                    solv= int(notalist[2]) * int(notalist[3])
                elif notalist[1] == "%":
                    solv= int(notalist[2]) % int(notalist[3])
                else:
                    solv= int(notalist[2]) / int(notalist[3])
                # solving main postfix
                if notalist[0] == "+":
                    solution= solv + int(notalist[4])
                elif notalist[0] == "-":
                    solution= solv - int(notalist[4])
                elif notalist[0] == "*":
                    solution= solv * int(notalist[4])
                elif notalist[0] == "/":
                    solution= solv / int(notalist[4])
                else:
                    solution= solv % int(notalist[4])
                print(solution)
            elif notalist[2] in list("+-*%/"):
                """
                equation for this is /a*bc = a/(b*c), you can use +-*/% operators
                """
                if notalist[2] == "+":
                    solv= int(notalist[3]) + int(notalist[4])
                elif notalist[2] == "-":
                    solv= int(notalist[3]) - int(notalist[4])
                elif notalist[2] == "*":
                    solv= int(notalist[3]) * int(notalist[4])
                elif notalist[2] == "/":
                    solv= int(notalist[3]) / int(notalist[4])
                else:
                    solv= int(notalist[3]) % int(notalist[4])
                # solving main prefix
                if notalist[0] == "+":
                    solution = int(notalist[1]) + solv
                elif notalist[0] == "-":
                    solution = int(notalist[1]) - solv
                elif notalist[0] == "*":
                    solution = int(notalist[1]) * solv
                elif notalist[0] == "/":
                    solution = int(notalist[1]) / solv
                else:
                    solution = int(notalist[1]) % solv
                print(solution)
            else:
                return "Please enter correct equation in abc*/ format or ab*c/, you can use */+-%"

        if len(notalist)==7:
            """
            equation for this is /*ab*cd = (a*b)/(c*d), you can use +-*/% operators
            """
            # for 1st prefix
            if notalist[1]=="+":
                calc1= int(notalist[2]) + int(notalist[3])
            elif notalist[1]=="-":
                calc1= int(notalist[2]) - int(notalist[3])
            elif notalist[1]=="*":
                calc1= int(notalist[2]) * int(notalist[3])
            elif notalist[1]=="/":
                calc1= int(notalist[2]) / int(notalist[3])
            else:
                calc1= int(notalist[2]) % int(notalist[3])
            # 1st prefix is done
            # now, for second prefix
            if notalist[4]== "+":
                calc2= int(notalist[5]) + int(notalist[6])
            elif notalist[4]== "-":
                calc2= int(notalist[5]) - int(notalist[6])
            elif notalist[4]== "*":
                calc2= int(notalist[5]) * int(notalist[6])
            elif notalist[4]=="/":
                calc2= int(notalist[5]) / int(notalist[6])
            else:
                calc2= int(notalist[5]) % int(notalist[6])
            # 2nd prefix is also done
            # now for main prefix
            if notalist[0]=="+":
                result= calc1 + calc2
            elif notalist[0]=="-":
                result= calc1 - calc2
            elif notalist[0]=="*":
                result= calc1 * calc2
            elif notalist[0]=="/":
                result= calc1 / calc2
            else:
                result= calc1 % calc2
            print(result)
