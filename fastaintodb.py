#!/usr/bin/python

#a quick script to parse a FASTA file and then insert it into a mysqlDB
#starting with the CSBs, because they seem like the easiest thing to start with
#this script assumes that the data is located in biodb_project/data (where it is on my laptop)
#######

#########HEADER

import MySQLdb

#########FUNCTIONS

####DATABASE CONNECTION

#the below is just copied from yozen code
def connect_db(dbase):
    """
    connected to the database dbase, user and password is hardcoded (for now)
    """
    #make a connection object
    connection = MySQLdb.connect (host="localhost", db=dbase, user="benpote", passwd="password") #highly secure password
    #get a cursor object from that
    cursor = connection.cursor()
    return cursor, connection

def close_db(cursor, connection):
    """
    close db connection
    """
    cursor.close()
    connection.close()

def run_query(cursor, query):
    """
    Pass it a cursor object and a text mysql query and get results!
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

####FASTA PARSING


def read_file(file):
    """
    Just reads in a file at the location it is passed
    """
    with open (file, "r") as myfile:
        data = myfile.read()
    return data

##functions for dealing with our various datafiles (parsing them into lists)

#csb functions
def format_csb(data):
    """
    Inserts our CSB files into the CSB table, expects a long string
    (normal result of calling read_file on csb.fasta)
    Returns a nicely formatted list which we can iterate through with a query function
    """
    data = data.replace('>','') #remove the > character from fasta headers
    data = data.split('\n')  #split string into list based on newline character
    data.pop()   #remove '' (last item in list)
    return data

def insert_csb(fasta,cursor):
    """
    takes a formatted fasta list (from format_csb) and a cursor, and executes querys to
    insert the data in the list into the database connection specified by the cursor
    """
    i = 0
    while i < len(fasta):
       query = """
       INSERT INTO csb(csbid,sequence) VALUES ('%s', '%s');
       """ % (fasta[i], fasta[i+1])
       cursor.execute(query)
       i += 2
    
        





########END FUNCTIONS


########ACTUALLY DOING STUFF!

file = "/home/benpote/Code/biological_databases/group_project/data/csb.fasta"

data = read_file(file)



#connect to our database
cursor, connection = connect_db('msad')

#a really boring example query
query = """
SHOW TABLES;
"""
#get the results!
results = run_query(cursor, query)
#print to see if it works
print results
#close the connection to our database 
close_db(cursor, connection)