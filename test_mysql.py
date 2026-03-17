import pymysql
import sys

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password=''
    )
    cursor = conn.cursor()
    cursor.execute("DROP DATABASE IF EXISTS new_project")
    cursor.execute("CREATE DATABASE new_project CHARACTER SET utf8 COLLATE utf8_general_ci")
    print("Database 'new_project' dropped and recreated with utf8.")
    conn.select_db('new_project')
    print("Connected to 'new_project'.")
    conn.close()
except Exception as e:
    print(f"Error connecting to MySQL: {e}")
    sys.exit(1)

print(f"PyMySQL version: {pymysql.__version__}")
