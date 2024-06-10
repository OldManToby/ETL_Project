from db_credentials import data_warehouse_name
import mysql.connector
import pyodbc
import fdb

def etl(query, source_cnx, target_cnx):
    #the following extracts data from source db
    source_cursor = source_cnx.cursor()
    source_cursor.execute(query.extract_query)
    data = source_cursor.fetchall()
    source_cursor.close()

    #the following loads data from source db
    if data:
        target_cursor = target_cnx.cursor()
        target_cursor.execute("USE{}".format(data_warehouse_name))
        target_cursor.executemany(query.load_query, data)
        print('data loaded to warehouse db')
        target_cursor.close()
    else:
        print('data is empty')

def etl_process(queries, target_cnx, source_db_config, db_platform):
    #establish db connection
    if db_platform == 'mysql':
        source_cnx = mysql.connector.connect(**source_db_config)
    elif db_platform == 'sqlserver':
        source_cnx = pyodbc.connect(**source_db_config)
    elif db_platform == 'firebird':
        source_cnx = fdb.connect(**source_db_config)
    else:
        return 'Error with Db platform!'
    
    #Loop through sql queries
    for query in queries:
        etl(query, source_cnx, target_cnx)
    #close the source db connection
    source_cnx.close()