# from pymysql import connect
# conn=connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="123456"
# )
# print(conn.get_server_info())
# conn.close()
from pymysql import connect
con =connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
cur=con.cursor()
con.select_db("world")
# cur.execute("create table test_1(id int)")
# cur.execute("select *from student")
# result=cur.fetchall()
# for row in result:
#     print(row)
cur.execute("insert into student values(8,'h',31,'男')")
# con.commit()
cur.close()
con.close()