# from Tkinter import *
import Tkinter as tk
from serial import *
import serial.tools.list_ports

root = tk.Tk()
root.wm_title("Port List")

# ----------------------------------------------------------
# Widget-called functions
# ----------------------------------------------------------
def ListPorts():
    PortVal = sorted(serial.tools.list_ports.comports())
    print PortVal
    PortVal = enumerate(PortVal)
    print PortVal
    #print list(PortVal)
    for n,(p1,p2,p3) in PortVal:
        PortList.insert(tk.END,p1)

# ----------------------------------------------------------
# GUI Widgets
# ----------------------------------------------------------
FrmPort= tk.Frame(root, padx=10, pady=10, borderwidth=7, relief="raised")
BtnLstPort=tk.Button(FrmPort,text='List COM Ports',command=ListPorts)
PortList=tk.Listbox(FrmPort,height=4,width=15)
BtnLstPort.pack()
PortList.pack()
FrmPort.pack()

# ----------------------------------------------------------
# Let'er rip
# ----------------------------------------------------------
root.mainloop()