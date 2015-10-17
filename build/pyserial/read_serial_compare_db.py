import serial, time
arduino = serial.Serial('/dev/ttyACM0', 9600)

import MySQLdb as mdb
db = mdb.connect(charset='utf8', host="127.0.0.1", user="root", passwd="root", db="lwc_members")
cur = db.cursor()


def search_database(id):
    cur.execute("SELECT * FROM members_list WHERE rfid_num='%s' " % read_id)
    mysql_data = cur.fetchall()
    for row in mysql_data:
            print "Identity:",row[2], row[3] 
    return mysql_data

id=39
while True:
    data = arduino.readline()
    print "Nothing"
    if len(data) > 10:
        print "ID detected"
        read_id = data[:12]
        print read_id
        mysql_data = search_database(read_id) 
        
        # this portion is to write the rfid to the database
        if mysql_data == ():
            id+=1
            print id
            cur.execute("UPDATE members_list SET rfid_num = '%s' WHERE id='%d' " % (read_id, id))
            print "Written!"
            db.commit()
            
            
            
    
    