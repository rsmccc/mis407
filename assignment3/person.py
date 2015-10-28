# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:08:38 2015

@author: rsmccloskey
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
        

    
if __name__ == '__main__':
  main()