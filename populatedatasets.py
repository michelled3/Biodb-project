#!/usr/bin/python

###This is a quick script to insert data into the dataset table
###necessary to have data in this table to insert minicircle data
###(datasetid foreign key is not_null in minicircle table)

###add datasets

datasets = {1:'genbank dataset',2:'pacbio dataset'}

def add_datasets(cursor,connection):
    for i in datasets:
        query = """
        INSERT INTO dataset(did,description) VALUES ('%d', '%s');
        """ % (i,datasets[i])
        cursor.execute(query)
    connection.commit()

###run it!

cursor, connection = connect_db('msad')
add_datasets(cursor,connection)
close_db(cursor, connection)
