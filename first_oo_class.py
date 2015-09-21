# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:02:50 2015

@author: rsmccloskey
"""

class Person():
  
  __PCount = 0
  
  def __init__(self, uid, lastname):
    self.uid = uid
    self.lastname = lastname
    # no underscores is public attribute, __ (two underscores) is private
    # e.g. __private__ vs public
    self.__PCount += 1
    
  def showMe(self):
    return self.uid, self.lastname, self.__PCount

class Student(Person):
  
  def __init__(self, sid, lname, status):
    self.sid = sid
    self.lname = lname
    self.status = status
    Person.__init__(self, sid, lname)
  
  def showMe(self):
    return Person.showMe(self), self.status
  
  
def main():
  Joe = Person(101, 'Able')
  print (Joe.showMe())
  
  Jane = Person(102, 'Baker')
  print (Jane.showMe())
  
  Jack = Student(103, 'Ripper', 'Part-Time')
  print(Jack.showMe())
  
  
if __name__ == '__main__':
  main()

  