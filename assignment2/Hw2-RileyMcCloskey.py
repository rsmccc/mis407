# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:02:14 2015

@author: rsmccc
"""

class Person():
    __PCount = 0
    
    def __init__(self, uid, lastname):
        self.uid = uid
        self.lastname = lastname
        self.__PCount += 1
        
    def showMe(self):
        print(self.uid, self.lastname, self.__PCount)
      
class Student(Person):
    
    def __init__(self, sid, lname, status):
        self.sid = sid
        self.lname = lname
        self.status = status
        Person.__init__(self,sid, lname)
        
    def showMe(self):
        
        Person.showMe(self)
        print('My status is ', self.status)
        
class SalaryEmp(Person):
  
  def __init__(self, eid, lname, monthlyPay):
      self.eid = eid
      self.lname = lname
      self.monthlyPay = monthlyPay
      Person.__init__(self, eid, lname)
      
  def showMe(self):
      Person.showMe(self)
      print('Salary = ' + self.monthlyPay)
        
def main():
    
    Tony = SalaryEmp(103, 'Trevor', '$2,500')
    Tony.showMe()
    
if __name__ == '__main__':
    main()