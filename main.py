import math
import copy

"""
Personal Python Module
"""
def __init__():
    return "This is a Python file used as a personal python module "
def new():
    return "Prefix and Postfix notation are not complete and can only used for 2 integers"


class new_math:
    def round(num):
        f= math.floor(num)
        r1= num-f
        if r1> 0.78:
            return math.ceil(num)
        elif r1< 0.23:
            return math.floor(num)
        else:
            return (num)
    def cbrt(num):
        return round(num**(1/3))
    def logadd(a,b):
        lga=math.log(a)/math.log(10)
        lgb=math.log(b)/math.log(10)
        return lgb+lga
    def logsub(a,b):
        div=round(a/b)
        lgsb=math.log(div)/math.log(10)
        return lgsb
    def __init__():
        return "This class is for attribute which you want in math module but don't have "

class matrix:
    def matrix(mtx_list):
        for row in mtx_list:
            for elem in row:
                print (elem,end="  ")
            print ()
    def mat_trans(mt_list):
        mtx_list= copy.copy(mt_list)
        for n in range(len(mtx_list)):
            i=0
            mtx_list[n][i], mtx_list[i][n]=mtx_list[i][n], mtx_list[n][i]
            if n!=0:
                i+=1
                mtx_list[n][i], mtx_list[i][n]=mtx_list[i][n], mtx_list[n][i]
        for row in mtx_list:
            for elem in row:
                print (elem,end="  ")
            print ()
    def determin(mtx_list):
        co11= mtx_list[1][1]*mtx_list[2][2]- mtx_list[1][2]*mtx_list[2][1]
        co12= mtx_list[1][0]*mtx_list[2][2]- mtx_list[1][2]*mtx_list[2][0]
        co13= mtx_list[1][0]*mtx_list[2][1]- mtx_list[1][1]*mtx_list[2][0]
        if len(mtx_list) ==2:
            print (co11- co12)
        else:
            print (co11*mtx_list[0][0]- co12*mtx_list[0][1]+ co13*mtx_list[0][2])
    def __init__():
        return "This class is for making matrix in python "

numlist=list("1234567890")
sym=list("+-*/")
class notation:
    def postfix(nota1):
        notalist=list(nota1)
        if notalist[2] == sym[0]:
            sum=int(notalist[0])+ int(notalist[1])
            print (sum)
        elif notalist[2]==sym[1]:
            sub=int (notalist[0])- int(notalist[1])
            print(sub)
        elif notalist [2]==sym[2]:
            mul= int(notalist[0])* int(notalist[1])
            print (mul)
        else:
            div =int(notalist[0])/ int(notalist [1])
            print (div)
    def prefix(nota1):
        notalist =list(nota1)
        if notalist [0]==sym [0]:
            sum=int(notalist[1]) + int(notalist[2])
            print (sum)
        elif notalist [0]==sym[1]:
            sub= int(notalist[1])- int(notalist[2])
            print(sub)
        elif notalist [0]==sym[2]:
            mul= int(notalist[1]) * int(notalist[2])
            print(mul)
        else:
            div= int(notalist[1])/ int(notalist[2])
            print(div)
