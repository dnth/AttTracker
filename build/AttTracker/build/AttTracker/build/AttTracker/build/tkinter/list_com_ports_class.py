import Tkinter as tk
import ttk
import serial
import serial.tools.list_ports

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        def ListPorts():
            PortVal = sorted(serial.tools.list_ports.comports())
#             print PortVal
            PortVal = enumerate(PortVal)
            #print list(PortVal)
            for n,(p1,p2,p3) in PortVal:
                PortList.insert(tk.END,p1) 
        
        FrmPort= tk.Frame(self, padx=10, pady=10, borderwidth=7, relief="raised")
        FrmPort.grid(row=4, column=2)
        BtnLstPort=ttk.Button(FrmPort,text='List COM Ports',command=ListPorts)
        BtnLstPort.grid(row=0)
        PortList=tk.Listbox(FrmPort,height=4,width=15)
        PortList.grid(row=1)
        

app = StartPage()
app.mainloop()