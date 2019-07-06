#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:00:33 2019

@author: hemant
"""

import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            
            self._connection=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="tinderb3")
            self._cursor=self._connection.cursor()
            print("Connected to database")
        
        except:
            
            print("Couldn't connect to database")
            #exit(0)
            
            
    
    def search(self,key1,value1,key2,value2,table):          #Make this table general for all searching
        
        self._cursor.execute("""
            select * from `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'
            """.format(table,key1,value1,key2,value2))
        
        data=self._cursor.fetchall()
        
        return data
    
    def searchOne(self,key1,value1,table,type):
        
        
        self._cursor.execute("""
            select * from `{}` WHERE `{}` {} '{}'
            """.format(table,key1,type,value1))
        
        data=self._cursor.fetchall()
        
        return data

    #new search
    def searchOneFromList(self,key1,value1,table,type):
        
        print("""
            select * from `{}` WHERE `{}` {} {}
            """.format(table,key1,type,value1))
        self._cursor.execute("""
            select * from `{}` WHERE `{}` {} {}
            """.format(table,key1,type,value1))
        
        data=self._cursor.fetchall()
        
        return data

    
    def insert(self,insertDict,table):    #General Table for all tables in databases
        
        
        colValue=""
        dataValue=""
        
        for i in insertDict:
            colValue=colValue + "`" + i + "`,"
            dataValue=dataValue + "'" +insertDict[i] + "',"
            
        colValue=colValue[0:-1]
        dataValue=dataValue[0:-1]
        
        
        query="INSERT INTO `{}` ({}) VALUES ({})".format(table,colValue,dataValue)
        
        
        try:
            self._cursor.execute(query)
            self._connection.commit()
            
            return 1
        except:
            
            return 0


    def update(self,insertDict,table,sessionId):

        query="""
        UPDATE `{}` SET `name` ='{}', `password` ='{}',`gender` ='{}', `age` ='{}', `city` ='{}', `Dp` ='{}' WHERE user_id={}""".format(table,insertDict['name'],insertDict['password'],insertDict['gender'],insertDict['age'],insertDict['city'],insertDict['Dp'],sessionId)
        try:
            self._cursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0

        
                                                                              
        
        