class Student:
    def __init__(self,first,last,ssn,email,age):
        self.first=first
        self.last=last
        self.ssn=ssn
        self.email=email
        self.age=age
    def __eq__(self,rhs):
            return self.ssn==rhs.ssn
    def __ne__(self,rhs):
        return self.ssn!=rhs.ssn
    def __lt__(self,rhs):
            return self.ssn<rhs.ssn
    def __gt__(self,rhs):
            return self.ssn>rhs.ssn
    def __le__(self,rhs):
            return self.ssn<=rhs.ssn
    def __ge__(self,rhs):
            return self.ssn>=rhs.ssn
            
class Count:
    def __init__ (self):
        self.total_age=0
