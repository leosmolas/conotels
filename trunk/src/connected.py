from connection.connection import Connection

conn = Connection("conotels", dbUser="root", dbPass="")
conn.open()

def closeConn():
	conn.close()
