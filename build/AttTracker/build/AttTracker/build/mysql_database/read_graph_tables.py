from __future__ import division
import MySQLdb as mdb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import collections
from _sqlite3 import Row


# data = pd.read_excel("/home/camaro-workstation/Desktop/lwc_members_list.xlsx", header=None)
db = mdb.connect(charset='utf8', host="127.0.0.1", user="root", passwd="root", db="lwc_members")
cur = db.cursor()



def calc_num_all_dept(verbose=False):
    '''
    Calculates the number of members in each dept 
    '''
    cur.execute("SELECT * FROM members_list")
    
    
    CL_count = 0
    BF_count = 0
    JS_count = 0
    YM_count = 0
    YF_count = 0
    CM_count = 0
    CF_count = 0
    SSM_count = 0
    SSF_count = 0
    MWM_count = 0
    MWF_count = 0
    GL_count = 0
    OS_count = 0
    
    data = cur.fetchall()
    for row in data:
#         print row
    #     print row[0], row[1].encode('utf8'), row[2]
        if row[4]=='CL':
            CL_count+=1
        if row[4]=='BF':
            BF_count+=1
        if row[4]=='JS':
            JS_count+=1
        if row[4]=='YM':
            YM_count+=1
        if row[4]=='YF':
            YF_count+=1
        if row[4]=='CM':
            CM_count+=1
        if row[4]=='CF':
            CF_count+=1
        if row[4]=='SSM':
            SSM_count+=1
        if row[4]=="SSF":
            SSF_count+=1
        if row[4]=='MWM':
            MWM_count+=1
        if row[4]=='MWF':
            MWF_count+=1    
        if row[4]=='GL':
            GL_count+=1
        if row[4]=='OS':
            OS_count+=1   
    if verbose:        
        print "CL:", CL_count
        print "BF:", BF_count
        print "JS:", JS_count
        print "YM:", YM_count
        print "YF:", YF_count
        print "CM:", CM_count
        print "CF:", CF_count
        print "SSM:", SSM_count
        print "SSF:", SSF_count
        print "MWM:", MWM_count
        print "MWF:", MWF_count
        print "GL:", GL_count
        print "OS:", OS_count
        print "Total members:", CL_count+BF_count+JS_count+YM_count+YF_count+CM_count+CF_count+SSM_count+SSF_count+MWM_count+MWF_count+GL_count+OS_count
    
    d = collections.OrderedDict()
    d['CL'] = CL_count
    d['BF'] = BF_count
    d['JS'] = JS_count
    d['YM'] = YM_count
    d['YF'] = YF_count
    d['CM'] = CM_count
    d['CF'] = CF_count
    d['SSM'] = SSM_count
    d['SSF'] = SSF_count
    d['MWM'] = MWM_count
    d['MWF'] = MWF_count
    d['GL'] = GL_count
    d['OS'] = OS_count    
    return d

def plot_dept_stats():
    '''
    Plots a bar chart of the number of members in each dept
    '''
    members_count = calc_num_all_dept()
#     plt.figure(figsize=(15,10))
    plt.grid(True)
    plt.title("LWC Members Distribution")
    plt.xlabel("Department")
    plt.ylabel("Number of members")
    plt.bar(range(len(members_count)), members_count.values(), align='center')
    plt.xticks(range(len(members_count)), members_count.keys())
    plt.show()

def search_database_for_id(search_for):
    cur.execute("SELECT * FROM member")
    data = cur.fetchall()
    status = "No Match"
    for id, name, dept in data:
        if id == search_for:
            status = "Match"
    return status

def plot_dept_att(month): 
    '''
    Plots the entire church department attendance on a specified month
    '''
    dept_list = ['CL','BF','JS','YM','YF','CM','CF','SSM','SSF','MWM','MWF', 'GL','OS']
    total_att = []
    for dept in dept_list:
        present_count = 0
#         print dept
        
        cur.execute("SELECT * FROM att_summ WHERE dept='%s' AND month(event_date)=%d " % (dept, month) )
        data = cur.fetchall()
        for row in data:
            if row[5]=='P' or row[4]=='B':
                present_count+=1
        # just to check for zero attendance to prevent zero division
        if len(data)== 0 :
            total_att.append(0)
#             print "Total number of days:", len(data)
#             print "Total numbers absence:", abs_count
            print "Total attendance for all events for %s department is %f"% (dept, total_att[-1]), "%"

        else:
#             print "Total number of days:", len(data)
#             print "Total numbers absence:", abs_count
            total_att.append( present_count/len(data)*100.00)
            print "Total attendance for %s department is %f"% (dept, total_att[-1]),"%"
    
    print "Overall church attendance for Month: %d is %f " % (month, np.mean(total_att)),"%"
       
#     plt.figure(figsize=(15,10))
    plt.grid(True)
    plt.title("Department Attendance for month: %d"% month)
    plt.xlabel("Department")
    plt.ylabel("Percentage")
    plt.bar(range(len(dept_list)), total_att, align='center')
    plt.xticks(range(len(dept_list)), dept_list)
#     plt.show()

def plot_att_by_category(month, year, event_type):
    '''
    Plots the attendance statistics for entire church given event and month
    '''
    cur.execute("SELECT * FROM att_summ_2 WHERE event_type='%s' AND month(event_date)=%d " % (event_type, month) )
    data = cur.fetchall()
    
    assert(len(data)>0)
    
    present_count = 0
    broadcast_count = 0
    
    for row in data:
#         print row[4]
        if row[4]=='B':
            present_count+=1
        if row[4]=='P':
            broadcast_count+=1
    
    cur.execute("SELECT COUNT(*) FROM event_test WHERE event_type='%s' " % event_type)
    num_events = cur.fetchall()[0]
    cur.execute("SELECT COUNT(*) FROM members_list")
    num_members = cur.fetchall()[0]
    
    # total days counted is num of members * num of events
    total_days_counted = (num_members[0]*num_events[0])
    # count total absentees by subtracting P and B from the total number of events for all members
    absent_count = total_days_counted - (present_count + broadcast_count)
    
    print "Total days counted for all members events in month %d is %d" % (month, len(data))
    print "Present:", present_count
    print "Broadcast:", broadcast_count
    print "Absent:", absent_count
     
    plt.pie([present_count, broadcast_count, absent_count], labels=["Present", "Broadcast", "Absent"],autopct='%1.1f%%',
            colors = ['green', 'yellow', 'red'])
    plt.title("Attendance Statistics for %s for month %d, %d"  % (event_type, month, year))
    plt.tight_layout(pad=5)
    plt.axis('equal')
#     plt.show()
    
    
    
plt.figure(figsize=(15,15))
plt.subplot(221)
plot_att_by_category(9, 2015, 'Sunday Service')
plt.subplot(222)
plot_att_by_category(9, 2015, 'Wednesday Service')
plt.subplot(223)
plot_att_by_category(9, 2015, 'Friday Prayer Meeting')
plt.subplot(224)
plot_att_by_category(9, 2015, 'Dawn Service')
plt.show()


    
# plt.figure(figsize=(15,15))
# plt.subplot(211)
# plot_dept_att(9)
# plt.subplot(212)
# plot_dept_stats()
# plt.show()






