data_warehouse_name = "db_warehouse"

#sql-server (target db, data_warehouse)
data_warehouse_db_config = {
    'Trusted Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'datawarehouse_sql_server',
    'database': '{}'.format(data_warehouse_name),
    'user': 'my_db_username',
    'password': 'my_db_password',
    'autocommit': 'True',
}

#sql-server (source db)
sqlserver_db_config = [
    {
    'Trusted Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'your_sql_server',
    'database': 'db1',
    },
    {
    'user': 'my_db_username',
    'password': 'my_db_password',
    'autocommit': 'True',
    },
]

#mysql (source db)
mysql_db_config =[
    {
    'user': 'your_user_1',
    'password': 'your_password_1',
    'host': 'db_connection_string_1',
    'database': 'db_1',
    },
    {
    'user': 'your_user_2',
    'password': 'your_password_2',
    'host': 'db_connection_string_2',
    'database': 'db_2',
    },
]

#firebird (source db)
fdb_db_config = [{
    'dsn': "/your/path/to/source.db",
    'user': "your_username",
    'password': 'your_password',
}]