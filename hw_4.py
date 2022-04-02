from json.tool import main
from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
import time
class Student:
    def __init__(self,first,last,ssn,email,age):
        self.first=first
        self.last=last
        self.ssn=ssn
        self.email=email
        self.age=age

def traverse():
    print()
    # print("traverse-")
    # t1=time.time()
    
    roll_call=[]
    fin=open("InsertNames.txt", "r")
    for line in fin:
        values=line.split()
        person=Student(values[0],values[1],values[2],values[3],values[4])
        duplicate=False
        for student in roll_call:
            if student.ssn==person.ssn:
                # print("sorry,",person.first,person.last," has the same ssn as",student.first,student.last,person.ssn)
                duplicate=True
        if duplicate!=True:
            roll_call.append(person) 
    # t2=time.time()
    # print("time spent=",(round(t2-t1,2)),"seconds")
    print()
    fin.close()
    return roll_call

def average_age():
    t1=time.time()
    roll_call=traverse()
    print("average-")
    total_age=0
    for person in roll_call:
        total_age+=int((person.age))

    average=total_age/len(roll_call)
    print("age=",average)
    
    t2=time.time()
    print("time spent=",(round(t2-t1,2)),"seconds")

def delete():
    t1=time.time()
    roll_call=traverse()
    print("delete-")
    
    fin=open("DeleteNames.txt", "r")
    for line in fin:
        found=False
        for student in roll_call:
            if student.ssn==line:
                roll_call.remove(student)
                found=True
                break
        if not found:
            print(line," not found")
    t2=time.time()
    print("time spent=",(round(t2-t1,2)),"seconds")

    fin.close()

def retrieve():
    t1=time.time()
    roll_call=traverse()
    print("retrieve-")
    fin=open("RetrieveNames.txt", "r")
    num_of_students=0
    age=0
    for line in fin:
        found=False
        for student in roll_call:
            if student.ssn==line.strip():
                age+=int(student.age)
                num_of_students+=1
                found=True
                break
        if not found:
            print(line," not found")
    t2=time.time()
    print("age=",age/num_of_students)
    print("time spent=",(round(t2-t1,2)),"seconds")
    print()




def main():
    average_age()
    delete()
    retrieve()

main()
