from cmath import inf
from mailbox import NotEmptyError
from graphics import *
class mystack:
    def __init__(self):
        self.list=[]
    def top(self):
        if self.notempty():
            return self.list[-1]
        else:
            return False
    def push(self,item):
        self.list.append(item)
    def pop(self):
        if self.notempty():
            item=self.list[-1]
            self.list.remove(item)
            return item
        else:
            return False
    def notempty(self):
        if len(self.list)==0:
            return False
        else:
            return True

def print_instructions():
    print("Welcome to the one stop graphing calculator!")
    print("you will be asked to provide an equation you would liked graphed")
    print()
    print("here is a key of supported operands you can do->")
    print()
    print("times -> *")
    print("divide -> /")
    print("subtract -> -")
    print("add -> +")
    print("parenthesis-> ( )")
    print("power of -> ^")
    print()
    print ("examples of equations")
    print()
    print("x^2")
    print("x * x / (x - 2)")
    print("x*2*x/3+2")
    print("x * x * x * x *")
    print()
    print("spaces are allowed but not required")




def InfixToPostfix(infix):
    op_stack=mystack()
    list=[]
    i=0
    while i<len(infix):
        if infix[i]=="(":
            op_stack.push(infix[i])
            i+=1
        elif infix[i]==")":
            while op_stack.top()!="(":
                operand=op_stack.pop()
                list.append(operand)
            op_stack.pop()
            i+=1
        elif infix[i] in "0123456789":
            num=""
            while  infix[i]!="(" and infix[i]!=")" and infix[i]!="*" and infix[i]!="/" and infix[i]!="+" and infix[i]!="-" and infix[i]!="x":
                if i==len(infix)-1:
                    num+=infix[i]
                    i+=1
                    break
                num+=infix[i]
                i+=1
            list.append(int(num))
        elif infix[i]=="^":
            list.append(infix[i])
            i+=1
        elif infix[i]=="*" or infix[i]=="/":
            if op_stack.top=="/" or op_stack.top()=="*":
                item=op_stack.pop()
                list.append(item)
                op_stack.push(infix[i])
                i+=1
            else:
                op_stack.push(infix[i])
                i+=1

        elif infix[i]=="+" or infix[i]=="-" :
            if op_stack.top=="*" or op_stack.top=="/" :
                item=op_stack.pop()
                list.append(item)

            if op_stack.top()=="+" or op_stack.top()=="-":
                item=op_stack.pop()
                list.append(item)

            op_stack.push(infix[i])
            i+=1
        elif infix[i]=="x":
            list.append(infix[i])
            i+=1
        else:
            i+=1
    while op_stack.notempty():
        list.append(op_stack.pop())
    
    return list
            
                
def EvaluatePostfix(postfix,x):
    stack=mystack()
    i=0
    while i <len(postfix):
        
        if postfix[i]=="x" or postfix[i]=="X":
            stack.push(x)
            i+=1
        elif postfix[i]=="^":
            lhs=stack.pop()
            rhs=postfix[i+1]
            result=lhs**int(rhs)
            stack.push(result)
            i+=2
        elif postfix[i]=="*":
            #pop pop multiply push result
            rhs=stack.pop()
            lhs=stack.pop()
            result=lhs*rhs
            stack.push(result)
            i+=1
        elif postfix[i]=="/":
            #pop pop multiply push resu alt
            rhs=stack.pop()
            lhs=stack.pop()
            result=lhs/rhs
            stack.push(result)
            i+=1
        elif postfix[i]=="+":
            #pop pop multiply push result
            rhs=stack.pop()
            lhs=stack.pop()
            result=lhs+rhs
            stack.push(result)
            i+=1
        elif postfix[i]=="-":
            #pop pop multiply push result
            rhs=stack.pop()
            lhs=stack.pop()
            result=lhs-rhs
            stack.push(result)
            i+=1
        elif type(postfix[i])==int:
            stack.push(postfix[i])
            i+=1
    return stack.pop()
def main():
    print()
    print_instructions()
    infix=input("Enter your equation here -> ")
    postfix=InfixToPostfix(infix)
    points=[]
    xlow= -10
    xhigh= 10
    ylow= -10
    yhigh= 10

    win = GraphWin("My Circle", 500, 500)
    win.setCoords(xlow,ylow,xhigh,yhigh)
    win.setBackground(color_rgb(25,25,25))
    line=Line(Point(-10,0),Point(10,0))
    line.setFill(color_rgb(255,255,255))
    line.draw(win)
    
    line=Line(Point(0,-10),Point(0,10))
    line.setFill(color_rgb(255,255,255))
    line.draw(win)
    x=xlow
    while x<xhigh:
        y=EvaluatePostfix(postfix,x)
        points.append((x,y))
        x+=.1
    for i in range (len(points)-1):
        p=points[i]
        p2=points[i+1]
        x1=p[0]
        y1=p[1]
        x2=p2[0]
        y2=p2[1]
        line=Line(Point(x1,y1),Point(x2,y2))
        line.setFill(color_rgb(0,0,255))
        line.draw(win),(0,255,0)
    # x_axis=yhigh/2
    # line=Line(Point(xlow,x_axis),Point(xhigh,x_axis))  
    # line.draw(win)  
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()