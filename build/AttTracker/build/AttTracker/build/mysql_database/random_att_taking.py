import MySQLdb as mdb
import datetime

import random

db = mdb.connect(charset='utf8', host="127.0.0.1", user="root", passwd="root", db="lwc_members")
cur = db.cursor()

cur.execute("SELECT * FROM event_test")
list_of_events = cur.fetchall()

cur.execute("SELECT * FROM members_list")
list_of_members = cur.fetchall()

list_of_status = ['P', 'B', 'A']


i=0
for event in list_of_events:
    for member in list_of_members:
        i+=1
        print i
        random_status = random.choice(list_of_status)
        print member[0], event[0], random_status
        cur.execute("INSERT INTO attendance_test VALUES (NULL, '%d', '%d', '%s' )" % (member[0], event[0], random_status))
    db.commit()