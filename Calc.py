#calculator
import time as t
import math as m 
repeat="true"
operators_list=['+','-','*','/','exp','check',"rem","fact","area",'add','sub','mul','div']
shape_list=["square","circle","rectangle"]
#defining operator functions
def add(x,y) :
    return x+y 
def sub(x,y) :
    return x-y
def mul(x,y) :
    return x*y 
def div(x,y) :
    return x/y 
def exp(x,y) :
    return x**y
def check(x,y):
     if x>y :
          return print( x ,' is greater than ', y)
     elif x<y :
          return print( x ,' is lesser than ' , y)
     else : 
          return print("Both are equal")
def rem(x,y):
    print(x%y)
def area() :
    shape=input("Input the shape : ")
    if shape in shape_list :
        if shape == "circle" :
            shape_length = int(input("Input the radius : "))
            area_= m.pi*shape_length*shape_length
        elif shape == "rectangle" :
            shape_length1=int(input("Input the length : "))    
            shape_length2=int(input("Input the breadth : "))
            area_= shape_length1*shape_length2
        elif shape == "square" :
            shape_length = int(input("Input the length : "))
            area_= shape_length*shape_length
        
        print(area_)
    else : print("No such shape exists !")
    exit
            


#main
while repeat=="true" :
    op_cat=input("Input the type of calculator you want to use - Alegbric or Geometric : ")
    if op_cat=="geometric" :
        op=str(input("input operation : "))
        if op == "area" : area()
        if op == "pi" : print(m.pi)
    elif op_cat=="algebric":
        x=float(input("input first number : "))
        op=str(input("input operation : "))
        y=float(input("input second number : "))
        
        if op in operators_list :
            if op == "+" or op =="add" : print(add(x,y))
            if op == "-" or op =="sub": print(sub(x,y))
            if op == "*" or op =="mul": print(mul(x,y))
            if op == "/" or op =="div": print(div(x,y))
            if op == "exp" : print(exp(x,y))
            if op == "check" : check(x,y)    
            if op == "rem" : rem(x,y)    
            
        else : print("Error ! No such operator exsits !")
    else : 
        print("No such type of calculator exists !")
        exit    
        
    repeat = str(input("Do you want to do another calculation ? \n"))
    if "y" in repeat : repeat="true"
    elif "n" in repeat :
        repeat=""
        print("Thank you for using the calculator !") 
        exit