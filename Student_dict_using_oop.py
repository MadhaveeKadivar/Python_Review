
from abc import ABC, abstractmethod
import random

class Myinterface(ABC):
    @abstractmethod
    def add(self,name,attendence):
        """ 
        Description: 
            This function is abstract method
        Parameter:
            It takes self,name and attendence as argument
        Return:
            None
        """
        pass

student_dict ={}  

class College(Myinterface):
    count = 0
    global student_dict
    def add(self,name,attendence):
        """ 
        Description: 
            This function is implementing add abstract method and adding value to dictionary
        Parameter:
            It takes self,name and attendence as argument
        Return:
            True or false
        """
        student_dict[self.count] = {}
        student_dict[self.count]["name"] = name
        student_dict[self.count]["attendence"] = attendence

def switch_case(check):
        """ 
        Description: 
            This function is getting attendence based on random value
        Parameter:
            It takes random int as argument
        Return:
            True or false
        """
        switch={
            1 : True,
            0 : False,
            }
        return switch.get(check,"")
    
obj = College() 
College.count = 1
student_list = ["s1","s2","s3"]
for i in student_list:
    check = random.randint(0,1)
    result = switch_case(check)
    obj.add(i,result)
    College.count += 1
    
print(student_dict)