import matplotlib
from Tkinter import StringVar
from PIL.ImageTk import PhotoImage
from time import strftime
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import Tkinter as tk
import ttk

from PIL import Image

import MySQLdb as mdb
import datetime
import serial
import serial.tools.list_ports
from datetime import date, time

# import serial.tools.list_ports
# from serial import *
# from Tkinter import *

serialPort = '/dev/ttyACM0'
baudrate = 9600
arduino = serial.Serial(serialPort, baudrate, timeout=0, writeTimeout=0)
db = mdb.connect(charset='utf8', host="127.0.0.1", user="root", passwd="root", db="lwc_members")
cur = db.cursor()


LARGE_FONT= ("Times", 20)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
f.set_tight_layout(False)
a = f.add_subplot(221)
b = f.add_subplot(222)
c = f.add_subplot(223)
d = f.add_subplot(224)


def animate(i):
    '''
    Animate for sunday Service attendance stats
    '''
    event_type = "Sunday Service"
    month = 9
    cur.execute("SELECT * FROM att_summ_2 WHERE event_type='%s' AND month(event_date)=%d " % (event_type, month) )
    data = cur.fetchall()
    
    assert(len(data)>0)
    
    present_count = 0
    broadcast_count = 0
    
    for row in data:
#         print row[4]
        if row[4]=='B':
            broadcast_count+=1
        if row[4]=='P':
            present_count+=1
            
    cur.execute("SELECT COUNT(*) FROM event_test WHERE event_type='%s' " % event_type)
    num_events = cur.fetchall()[0]
    cur.execute("SELECT COUNT(*) FROM members_list")
    num_members = cur.fetchall()[0]
            
    # total days counted is num of members * num of events
    total_days_counted = (num_members[0]*num_events[0])
    # count total absentees by subtracting P and B from the total number of events for all members
    absent_count = total_days_counted - (present_count + broadcast_count)
    
    a.clear()
    a.pie([present_count, broadcast_count, absent_count], labels=["Present", "Broadcast", "Absent"],autopct='%1.1f%%',
            colors = ['green', 'yellow', 'red'])
    a.axis('equal')
    a.set_title("Sunday Service")
    
    event_type = "Wednesday Service"
    cur.execute("SELECT * FROM att_summ_2 WHERE event_type='%s' AND month(event_date)=%d " % (event_type, month) )
    data = cur.fetchall()
     
    assert(len(data)>0)
     
    present_count = 0
    broadcast_count = 0
     
    for row in data:
#         print row[4]
        if row[4]=='B':
            broadcast_count+=1
        if row[4]=='P':
            present_count+=1
             
    cur.execute("SELECT COUNT(*) FROM event_test WHERE event_type='%s' " % event_type)
    num_events = cur.fetchall()[0]
    cur.execute("SELECT COUNT(*) FROM members_list")
    num_members = cur.fetchall()[0]
             
    # total days counted is num of members * num of events
    total_days_counted = (num_members[0]*num_events[0])
    # count total absentees by subtracting P and B from the total number of events for all members
    absent_count = total_days_counted - (present_count + broadcast_count)
     
    b.clear()
    b.pie([present_count, broadcast_count, absent_count], labels=["Present", "Broadcast", "Absent"],autopct='%1.1f%%',
            colors = ['green', 'yellow', 'red'])
    b.axis('equal')
    b.set_title("Wednesday Service")
    
    event_type = "Friday Prayer Meeting"
    cur.execute("SELECT * FROM att_summ_2 WHERE event_type='%s' AND month(event_date)=%d " % (event_type, month) )
    data = cur.fetchall()
     
    assert(len(data)>0)
     
    present_count = 0
    broadcast_count = 0
     
    for row in data:
#         print row[4]
        if row[4]=='B':
            broadcast_count+=1
        if row[4]=='P':
            present_count+=1
             
    cur.execute("SELECT COUNT(*) FROM event_test WHERE event_type='%s' " % event_type)
    num_events = cur.fetchall()[0]
    cur.execute("SELECT COUNT(*) FROM members_list")
    num_members = cur.fetchall()[0]
             
    # total days counted is num of members * num of events
    total_days_counted = (num_members[0]*num_events[0])
    # count total absentees by subtracting P and B from the total number of events for all members
    absent_count = total_days_counted - (present_count + broadcast_count)
     
    c.clear()
    c.pie([present_count, broadcast_count, absent_count], labels=["Present", "Broadcast", "Absent"],autopct='%1.1f%%',
            colors = ['green', 'yellow', 'red'])
    c.axis('equal')
    c.set_title("Friday Prayer Meeting")
    
    event_type = "Dawn Service"
    cur.execute("SELECT * FROM att_summ_2 WHERE event_type='%s' AND month(event_date)=%d " % (event_type, month) )
    data = cur.fetchall()
     
    assert(len(data)>0)
     
    present_count = 0
    broadcast_count = 0
     
    for row in data:
#         print row[4]
        if row[4]=='B':
            broadcast_count+=1
        if row[4]=='P':
            present_count+=1
             
    cur.execute("SELECT COUNT(*) FROM event_test WHERE event_type='%s' " % event_type)
    num_events = cur.fetchall()[0]
    cur.execute("SELECT COUNT(*) FROM members_list")
    num_members = cur.fetchall()[0]
             
    # total days counted is num of members * num of events
    total_days_counted = (num_members[0]*num_events[0])
    # count total absentees by subtracting P and B from the total number of events for all members
    absent_count = total_days_counted - (present_count + broadcast_count)
     
    d.clear()
    d.pie([present_count, broadcast_count, absent_count], labels=["Present", "Broadcast", "Absent"],autopct='%1.1f%%',
            colors = ['green', 'yellow', 'red'])
    d.axis('equal')
    d.set_title("Dawn Service")
    


        
        
class LWC_attendance_GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

#         tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Lord's Word Church Attendance")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TakeAttendance, AboutSoftware, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        def ListPorts():
            PortVal = sorted(serial.tools.list_ports.comports())
            PortVal = enumerate(PortVal)
            #print list(PortVal)
            for n,(p1,p2,p3) in PortVal:
                PortList.insert(tk.END,p1) 
                 
        FrmPort= tk.Frame(self, padx=10, pady=10, borderwidth=7, relief="raised")
        FrmPort.grid(row=4, column=0)
        BtnLstPort=ttk.Button(FrmPort,text='List COM Ports',command=ListPorts)
        BtnLstPort.grid(row=0)
        PortList=tk.Listbox(FrmPort,height=4,width=15)
        PortList.grid(row=1)
        

        BtnConnect = ttk.Button(FrmPort, text="Connect", command=self.connect_to_port)
        BtnConnect.grid(row=2)
        
        
        
        label = tk.Label(self, text="Welcome!", font=('Times',15), bg='blue', fg='white')
        label.grid(row=0, column=1, sticky="nsew")
         
        button = ttk.Button(self, text="Take Attendance",
                            command=lambda: controller.show_frame(TakeAttendance))
        button.grid(row=2, column=0, sticky="nsew")
    
        button2 = ttk.Button(self, text="About Software",
                            command=lambda: controller.show_frame(AboutSoftware))
        button2.grid(row=3, column=0, sticky="nsew")
    
        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.grid(row=1, column=0, sticky="nsew")
        
        button_exit = ttk.Button(self, text="Exit", command=exit)
        button_exit.grid(row=0, column=0, sticky="nsew")
        
    def connect_to_port(self):
        serialPort = '/dev/ttyACM0'
        baudrate = 9600
        arduino = serial.Serial(PortList.get(PortList.curselection()), baudrate, timeout=0, writeTimeout=0)       
  
    
          

class TakeAttendance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                
        label = tk.Label(self, text="Attendance Taking Page", font=('Times',15), bg='blue', fg='white')
        label.grid(row=0, column=1)
        
        label = tk.Label(self, text="Please scan your ID...", font=('Times',15))
        label.grid(row=1, column=1, sticky="W")

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0, sticky="nsew")

        button2 = ttk.Button(self, text="About Software",
                            command=lambda: controller.show_frame(AboutSoftware))
        button2.grid(row=1, column=0, sticky="nsew")
        
        self.createRFIDLabels()
                
    def createRFIDLabels(self):
                # Static labels
        label_rfid = tk.Label(self, text="RFID:", font=LARGE_FONT)
        label_rfid.grid(row=2, column=1, sticky='E')
        
        label_name = tk.Label(self, text="Name:", font=LARGE_FONT)
        label_name.grid(row=3, column=1, sticky='E')
        
        label_name_chi = tk.Label(self, text="Chinese name:", font=LARGE_FONT)
        label_name_chi.grid(row=4, column=1, sticky='E')
        
        label_status = tk.Label(self, text="Status:", font=LARGE_FONT)
        label_status.grid(row=5, column=1, sticky='E')
        
        # Dynamic labels that changes
        self.rfid_number_label = StringVar()
        label_rfid_dyn = tk.Label(self, textvariable=self.rfid_number_label, font=LARGE_FONT)
        label_rfid_dyn.grid(row=2, column=2)
        
        self.name_label = StringVar()
        label_name_dyn = tk.Label(self, textvariable=self.name_label, font=LARGE_FONT)
        label_name_dyn.grid(row=3, column=2)
        
        self.name_chi_label = StringVar()
        label_name_chi_dyn = tk.Label(self, textvariable=self.name_chi_label, font=LARGE_FONT)
        label_name_chi_dyn.grid(row=4, column=2)
        
        self.status_label = StringVar()
        label_status_dyn = tk.Label(self, textvariable=self.status_label, font=LARGE_FONT, justify="left")
        label_status_dyn.grid(row=5, column=2)
        
        self.rfid_pic_label = StringVar()
        tk.Label(self, textvariable=self.rfid_pic_label).grid(row=6, column=4)
        
        
#         im_temp = Image.open("goku.png")
#         im_temp = im_temp.resize((250, 250), Image.ANTIALIAS)
#         im_temp.save("goku", "png")
#         
#         photo = PhotoImage(file="goku", width=32, height=32)
#         w = tk.Label(self, image=photo)
#         w.photo = photo
#         w.grid(row=5,column=4)
        
        #calls the scan_id function every 500 ms 
        self.id = self.after(1000, self.scan_id) 

    def search_database_for_member_id(self, rfid):
        '''
        Search databse for member identity and print
        param: id reader
        return: member_id 
        '''
        cur.execute("SELECT * FROM members_list WHERE rfid_num='%s' " % rfid)
        mysql_data = cur.fetchall()
        return mysql_data


    def scan_id(self):
#         data = arduino.readline()

        try:
            data = arduino.read(arduino.inWaiting())
        except:
            print("Error reading from %s " % serialPort )
        
#         print "Nothing"
        if len(data) > 10:
            print "ID detected"
            read_id = data[:12]
            print read_id
            self.rfid_number_label.set(read_id)
            
            member_data = self.search_database_for_member_id(read_id)
            if member_data:
                member_id = member_data[0][0] 
                self.name_label.set(member_data[0][3])
                self.name_chi_label.set(member_data[0][2])
                print "Name:",member_data[0][2]
                
                current_date = datetime.datetime.date(datetime.datetime.now())
                current_time = datetime.datetime.time(datetime.datetime.now())
                 
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                        
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                   
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                   
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                         
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                       
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                       
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                       
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                       
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                       
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
                        self.status_label.set("Recorded!\nMember:%s\nEvent:%s %s" % (member_data[0][2],event_type, event_date))
                    else:
                        print "Record exists for:"
                        print "Member:", member_data[0][2]
                        print "Event:", event_type, event_date
                        self.status_label.set("Record exists for\nMember:%s\nEvent: %s %s " % (member_data[0][2], event_type, event_date))
                else:
                    print "No event now!"
                    print current_date, current_time
                    self.status_label.set("No event now!\nCurrent date: %s \nCurrent time:%s" % (current_date, current_time))
            else:
                print "Sorry no match in database!"
                self.status_label.set("Sorry no match in database!")

        # calls itself again after 100ms                
        self.id = self.after(100, self.scan_id)


class AboutSoftware(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="About Software", font=LARGE_FONT)
        label.grid(row=0, column=1, sticky="nsew")

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0, sticky="nsew")

        button2 = ttk.Button(self, text="Take Attendnace",
                            command=lambda: controller.show_frame(TakeAttendance))
        button2.grid(row=1, column=0, sticky="nsew")
                
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        

app = LWC_attendance_GUI()
# app.geometry("1000x400")
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()