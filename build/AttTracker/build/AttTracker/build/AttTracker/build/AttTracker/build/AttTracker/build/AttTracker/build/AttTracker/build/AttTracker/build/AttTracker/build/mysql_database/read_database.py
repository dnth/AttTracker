import MySQLdb as mdb


db = mdb.connect(host="127.0.0.1", user="root", passwd="root", db="lwc_members", charset='utf8')

cur = db.cursor()

#insert data
# cur.execute("""INSERT INTO member VALUES(%s, %s, %s, %s, NULL)""",("Jeong", "Su Seon", 'F', "1986-4-6"))
# 
# db.commit()

# cur.execute("INSERT INTO member(family_name) VALUES('Alibaba')")

# cur.execute("SELECT * FROM attendance")
# for row in cur.fetchall():
#     print row[4].strftime("%A")
#     print row
#      
# db.close()

id_value = '150'
cur.execute("SELECT * FROM members_list WHERE id=%s " % id_value)
data = cur.fetchall()
 
for row in data:
    print row[0], row[1], row[2]
#     print type(str(row[0])), type(id_value)
    if id_value == str(row[0]):
        print 'match'