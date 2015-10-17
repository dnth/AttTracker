import MySQLdb as mdb
import datetime
import serial
from datetime import date, time

arduino = serial.Serial('/dev/ttyACM0', 9600)
db = mdb.connect(charset='utf8', host="127.0.0.1", user="root", passwd="root", db="lwc_members")
cur = db.cursor()

def search_database_for_member_id(rfid):
    '''
    Search databse for member identity and print
    param: id reader
    return: member_id 
    '''
    cur.execute("SELECT * FROM members_list WHERE rfid_num='%s' " % rfid)
    mysql_data = cur.fetchall()
#     for row in mysql_data:
#             print "Identity:", row[0], row[1], row[2], row[3] 
#             return str(row[0])
    return mysql_data

while True:
    data = arduino.readline()
    print "Nothing"
    if len(data) > 10:
        print "ID detected"
        read_id = data[:12]
#         print read_id
        member_data = search_database_for_member_id(read_id) 
        print member_data[0][0]
        cur.execute("UPDATE members_list SET checker='1' WHERE id='%d' " % member_data[0][0])
        db.commit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            