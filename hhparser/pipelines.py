# -*- coding: utf-8 -*-
import sys
import MySQLdb
from hhparser.items import HhparserItem 



class HhparserPipeline(object):
        def __init__(self):
            self.conn = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="133737Aa",  # your password
                     db="sys")
            self.cursor = self.conn.cursor()

        def process_item(self, item, spider):  
        
            
     
            try:
                self.cursor.execute("""INSERT INTO hhvacancy (NameVacancy,Salary,Employer) 
                        VALUES (%s, %s,%s)""", 
                       (item['NameVacancy'],item['Salary'],item['Employer']))
   
                self.conn.commit()            
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
            return item
    

    
   
 
 
            