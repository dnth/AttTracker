import MySQLdb as mdb
import pandas as pd

data = pd.read_excel("/home/camaro-workstation/Desktop/lwc_members_list.xlsx", header=None)
db = mdb.connect(charset='utf8', host="127.0.0.1", user="root", passwd="root", db="lwc_members")
cur = db.cursor()

# iterate over pandas dataframe
for index, row in data.iterrows():
    print index, row[0], row[1]
    cur.execute("INSERT INTO members_list VALUES(Null, %s, %s)", (row[0],row[1]))

# print data[0][0]
# cur.execute("INSERT INTO members_list(chi_name) VALUES(%s)", (data[0][0]))

# cur.execute("SELECT * FROM members_list")
# for row in cur.fetchall():
#     print row
db.commit()
db.close()