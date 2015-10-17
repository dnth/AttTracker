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
        
    

# current_date = date(2015,9,7)
# current_time = time(1,0,0)
# print "Current day",current_date.strftime("%A")
# print "Current time",current_time
 
# print "NOW:", datetime.datetime.time(datetime.datetime.now()) # get current time
# print "NOW:", datetime.datetime.date(datetime.datetime.now()) # get current date
# print "NOW:", datetime.datetime.date(datetime.datetime.now()).strftime("%A") # get current day
 
 
 
# while True:
#     data = arduino.readline()
#     print "Nothing"
#     if len(data) > 10:
#         print "ID detected"
#         read_id = data[:12]
# #         print read_id
#         member_data = search_database_for_member_id(read_id) 
#         member_id = member_data[0][0] 
#          
#         # usual service & meeting
#         if current_date.strftime("%A") == "Sunday" and current_time >= time(7,0,0) and current_time <= time(10,30,0):
#             event_type = "Sunday Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#  
#               
#                
#         elif current_date.strftime("%A") == "Wednesday" and current_time >= time(18,0,0) and current_time <= time(21,0,0):
#             event_type = "Wednesday Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#            
#         elif current_date.strftime("%A") == "Friday" and current_time >= time(18,0,0) and current_time <= time(21,0,0):
#             event_type = "Friday Prayer Meeting"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#            
#         # dawn service
#         elif current_date.strftime("%A") == "Sunday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
#             event_type = "Dawn Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#                  
#         elif current_date.strftime("%A") == "Monday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
#             event_type = "Dawn Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#                
#         elif current_date.strftime("%A") == "Tuesday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
#             event_type = "Dawn Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#                
#         elif current_date.strftime("%A") == "Wednesday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
#             event_type = "Dawn Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#                
#         elif current_date.strftime("%A") == "Thursday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
#             event_type = "Dawn Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#                
#         elif current_date.strftime("%A") == "Friday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
#             event_type = "Dawn Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#                
#         elif current_date.strftime("%A") == "Saturday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
#             event_type = "Dawn Service"
#             event_date = current_date
#             cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
#             event_id = str(cur.fetchall()[0][0])
#             # search for existing record before inserting
#             cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
#             if cur.fetchall() == ():
#                 cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
#                 db.commit()
#                 print "Recorded!"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date 
#             else:
#                 print "Record exists for:"
#                 print "Member:", member_data[0][2]
#                 print "Event:", event_type, event_date
#            
#         else:
#             print "No event!"


###########################
# realtime implementation #
###########################
while True:
    data = arduino.readline()
    print "Nothing"
    if len(data) > 10:
        print "ID detected"
        read_id = data[:12]
        print read_id
        member_data = search_database_for_member_id(read_id) 
        
        # check if the ID is available in database
        if member_data:
            print member_data
            member_id = member_data[0][0] 
            
            print "Name:",member_data[0][2]
             
            current_date = datetime.datetime.date(datetime.datetime.now())
            current_time = datetime.datetime.time(datetime.datetime.now())
            # usual service & meeting
            if current_date.strftime("%A") == "Sunday" and current_time >= time(7,0,0) and current_time <= time(10,30,0):
                event_type = "Sunday Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
     
                  
                   
            elif current_date.strftime("%A") == "Wednesday" and current_time >= time(18,0,0) and current_time <= time(21,0,0):
                event_type = "Wednesday Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
               
            elif current_date.strftime("%A") == "Friday" and current_time >= time(18,0,0) and current_time <= time(21,0,0):
                event_type = "Friday Prayer Meeting"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
               
            # dawn service
            elif current_date.strftime("%A") == "Sunday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
                event_type = "Dawn Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
                     
            elif current_date.strftime("%A") == "Monday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
                event_type = "Dawn Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
                   
            elif current_date.strftime("%A") == "Tuesday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
                event_type = "Dawn Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
                   
            elif current_date.strftime("%A") == "Wednesday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
                event_type = "Dawn Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
                   
            elif current_date.strftime("%A") == "Thursday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
                event_type = "Dawn Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
                   
            elif current_date.strftime("%A") == "Friday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
                event_type = "Dawn Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
                   
            elif current_date.strftime("%A") == "Saturday" and current_time >= time(0,0,0) and current_time <= time(5,0,0):
                event_type = "Dawn Service"
                event_date = current_date
                cur.execute("SELECT * FROM event_test WHERE event_type='%s' AND event_date='%s' " % (event_type, event_date) )
                event_id = str(cur.fetchall()[0][0])
                # search for existing record before inserting
                cur.execute("SELECT * FROM attendance_test_2 WHERE member_id='%d' AND event_id='%d' " % ( int(member_id), int(event_id) ) )
                if cur.fetchall() == ():
                    cur.execute("INSERT INTO attendance_test_2 VALUES (NULL, '%d', '%d', 'P' )" % ( int(member_id), int(event_id) ))
                    db.commit()
                    print "Recorded!"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date 
                else:
                    print "Record exists for:"
                    print "Member:", member_data[0][2]
                    print "Event:", event_type, event_date
            else:
                print "No event!"
                print current_date, current_time
        else:
            print "Sorry no match in database!"
