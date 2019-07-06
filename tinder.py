#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:00:57 2019

@author: hemant
"""

#import mysql.connector



from guihelper import GUIhelper
from dbhelper import DBhelper

class Tinder(GUIhelper):
    
    def __init__(self):
        self.sessionId=0
        self.db=DBhelper()
        super(Tinder, self).__init__(self.login, self.loadRegWindow)

    def login(self):
        if self._emailInput.get()=="" or self._passwordInput.get()=="":
            self.label2.configure(text="Please fill both the fields",bg="yellow",fg="red")
        else:
            if '@' not in self._emailInput.get():
                self.label2.configure(text="Email input invalid",bg="yellow",fg="red")
            else:
                data=self.db.search('email',self._emailInput.get(),'password',self._passwordInput.get(),'users')
                if len(data)==1:
                    self.clean()
                    self.sessionId=data[0][0]
                    self.loadProfile()
                    #self.mainWindow(data)
                else:
                    self.label2.configure(text="Login Failed",bg="red", fg="white")




    def loadRegWindow(self):
        num=0
        self.regWindow(lambda: self.registrationHandler(num))
        #self.clean()

    def registrationHandler(self,num):
        if self._nameInput.get()=="" or self._emailInput.get()=="" or self._passwordInput.get()=="" or self._genderInput.get()=="" or self._ageInput.get()=="" or self._cityInput.get()=="" or self._dpInput.get()=="":
            self.label2.configure(text="Please fill all the fields",bg="yellow",fg="red")
        else:
            regDict={}
    
            #regDict['user_id']="NULL"
            regDict['name']=self._nameInput.get()
            regDict['email']=self._emailInput.get()
            regDict['password']=self._passwordInput.get()
            regDict['gender']=self._genderInput.get()
            regDict['age']=self._ageInput.get()
            regDict['city']=self._cityInput.get()
            regDict['Dp']=self._dpInput.get()

            if num==0:

                response=self.db.insert(regDict,'users')
            else:
                response=self.db.update(regDict,'users',self.sessionId)
            #print(response)
            if response==1:
                
                #self.clean()
                #obj=GUIhelper(self.login,self.loadRegWindow)
                self.label2.configure(text="Registration Successful. Login to proceed", bg="white", fg="green")
                self._root.destroy()
                obj=Tinder()

                
            else:
                
                self.label2.configure(text="Registration Failed", bg="yellow", fg="red")

#-----------------------------------------------------------------    #Self Added
    def logout(self):
        self._root.destroy()
      #self.label2.configure(text="Logout Successfully", bg="yellow", fg="red")
        obj=Tinder()
#-------------------------------------------------------------------------------------   
    
#-----------------------------------------------------------------------------
    def editProfile(self):
        num=1
        data=self.db.searchOne('user_id',self.sessionId,'users','LIKE')
        self.editWindow(data,lambda:self.registrationHandler(num))


    
#------------------------------------------------------------------



    def loadProfile(self):
        if self.sessionId!=0:
            
            data=self.db.searchOne('user_id',self.sessionId,'users',"LIKE")
            self.mainWindow(self,data,mode=1)
            
            
            
    def viewProfile(self,num):
        if self.sessionId!=0:
            data=self.db.searchOne('user_id',self.sessionId,'users',"NOT LIKE")
            #print(data)
            if num==0:
                new_data=[]
                new_data.append(data[0])
                self.mainWindow(self,new_data,mode=2,num=num)    #
            elif num<0:
                self.message("Error","User Khtm")
            elif num>len(data)-1:
                self.message("Error","User Khtm")
            else:
                new_data=[]
                new_data.append(data[num])
                self.mainWindow(self,new_data,mode=2,num=num)
                
                
    def propose(self,juliet_id):
        data=self.db.search('romeo_id',self.sessionId,'juliet_id',juliet_id,'proposals')
        if len(data)==0:
            propDict={}
            propDict['romeo_id']=str(self.sessionId)
            propDict['juliet_id']=juliet_id
            response=self.db.insert(propDict,'proposals')
            if response==1:
                self.message("Yayyyy","Proposal sent.Fingers Crossed")
            else:
                self.message("Nayyyyy","Nai gya manhoos")
        else:


            self.message("Invalid","Despo sale")    
        
    #functions for view_proposals    
    def viewProposal(self,num):
        if self.sessionId!=0:
            data=self.db.searchOne('romeo_id',self.sessionId,'proposals',"LIKE")
            #print(data)
            l1 =[val[2] for val in data]
            l1=tuple(l1)
            #print(l1)
            if (len(l1)>1):
                data=self.db.searchOneFromList('user_id',l1,'users',"IN")
                print(data)
            
                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=3,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=3,num=num)
            elif(len(l1)==1):
                data=self.db.searchOne('user_id',l1[0],'users',"LIKE")
                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=3,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=3,num=num)
            else:
                self.message("","No proposal Found")
                
    #functions for view Requests
    def viewRequest(self,num):
        if self.sessionId!=0:
            data=self.db.searchOne('juliet_id',self.sessionId,'proposals',"LIKE")
            print(data)
            l1 =[val[1] for val in data]
            l1=tuple(l1)
            print(l1)
            if(len(l1)>1):
                data=self.db.searchOneFromList('user_id',l1,'users',"IN")
                #print(data)

                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=4,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=4,num=num)
            elif(len(l1)==1):
                data=self.db.searchOne('user_id',l1[0],'users',"LIKE")
                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=4,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=4,num=num)
            else:
                self.message("So Sad!!","No Requests Found")
    
    #function to see the matchings
    def viewMatching(self,num):
        if (self.sessionId!=0):
            proposal_data=self.db.searchOne('romeo_id',self.sessionId,'proposals',"LIKE")
            #print(proposal_data)
            proposal_list=[val[2] for val in proposal_data]
            #print(proposal_list)
            request_data=self.db.searchOne('juliet_id',self.sessionId,'proposals',"LIKE")
            request_list=[val[1] for val in request_data]
            #print(request_list)
            l1=tuple(set(proposal_list)&set(request_list))
            #print(l1)
            if(len(l1)>1):
                data=self.db.searchOneFromList('user_id',l1,'users',"IN")
                #print(data)

                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=5,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=5,num=num)
            elif(len(l1)==1):
                data=self.db.searchOne('user_id',l1[0],'users',"LIKE")
                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=5,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=4,num=num)
            else:
                self.message("So Sad!!","No Matchings Found")





        
            


obj=Tinder()
        
        
        
        
        
                
                
                
                
                
        
        
        







#dbhelper

