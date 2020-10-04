import mysql.connector as conn

def getconn():
    db = conn.connect(host = 'localhost', user= 'root', passwd = '',
                          database = 'project')

    return db
