import time
import student
import bst
import container 
class Count:
    def __init__ (self):
        self.total_age=0
def traverse(roll_call):
    t1=time.time()
    print()
    print("-Traverse-")
    fin=open("InsertNames.txt", "r")
    for line in fin:
        values=line.split()
        person=student.Student(values[0],values[1],values[2],values[3],values[4])
        valid=roll_call.Insert(person)
        if valid==False:
            print(person.first,person.last,"already exist") 
    t2=time.time()
    print("time spent=",(round(t2-t1,2)),"seconds")
    print(roll_call.size())
    fin.close()

def ages(item,kount):
    kount.total_age+=int(item.age)

def average_age(container):
    t1=time.time()
    print()
    print("-average-")
    
    count=Count()
    container.Traverse(ages,count)

    average=count.total_age/container.size()
    print("age=",average)
    
    t2=time.time()
    print("time spent=",(round(t2-t1,2)),"seconds")

def delete(container):
    t1=time.time()
    print()
    print("-delete-")
    
    fin=open("DeleteNames.txt", "r")
    for line in fin:
        ssn=line.strip()
        person=student.Student("","",ssn,"","0")
        found= container.Delete(person)
        if found==False:
           print( ssn," not found!")
             
    t2=time.time()
    print("time spent=",(round(t2-t1,2)),"seconds")

    fin.close()

def retrieve(container):
    t1=time.time()
    print()
    print("-retrieve-")
    fin=open("RetrieveNames.txt", "r")
    num_of_students=0
    age=0
    for line in fin:
        ssn=line.strip()
        fake_person=student.Student(" "," ",ssn," ","0")
        real_person=container.Retrieve(fake_person)
        if real_person is None:
            print(ssn," not found")
        else:
            num_of_students+=1
            age+=int(real_person.age)
    t2=time.time()
    print("age=",age/num_of_students)
    print("time spent=",(round(t2-t1,2)),"seconds")
    print()

def main():
    roll_call=bst.Container()
    traverse(roll_call)
    average_age(roll_call)
    delete(roll_call)
    retrieve(roll_call)
    
main()