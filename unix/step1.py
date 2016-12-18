from Tkinter import *
import os
class AttachAll(Label):
    def __init__(self, parent=None,**config):         # add callback method
        Label.__init__(self, parent,config)
        self.pack()
        
        self.config(bd=10,relief=GROOVE)
        self.create_widget()

    def create_widget(self):
        self.flag=1
        self.ob_all=AttachBscPd(self)
        self.ob_all.pack(side=TOP,fill=X)
        self.ob_all.config(bd=5,relief=RIDGE)
        
        self.ob_nc=NC(self)
        self.ob_nc.config(bd=5,relief=RIDGE)
        self.ob_nc.pack(side=TOP,fill=X)
            
        self.ob_btstype=BtsType(self)
        self.ob_btstype.pack(side=TOP,fill=X)
        self.ob_btstype.config(bd=5,relief=RIDGE)
        
        self.msg=Entry(self)
        self.msg.pack(side=LEFT,expand=YES,fill=X)
        self.bttn_auth=Button(self,text="AUTHENTICATE",command=self.call_me,bd=2,relief=RAISED)
        self.bttn_auth.pack(side=LEFT)
        
        

        self.bttn_next=Button(self,text="NEXT",state=DISABLED,bd=2,relief=RAISED)
        self.bttn_next.pack(side=RIGHT)
    def call_me(self):

        self.infile=self.ob_all.ob_bsctype.bsctype_group.get()+"_"+str(self.ob_nc.cell_array_maker())+"cell_"+self.ob_all.ob_packetdatatype.packetdatatype_group.get()+"_"+self.ob_btstype.btstype_group.get()+self.ob_nc.vv
        path=os.getcwd()
        
        self.des=path+"/unix/"+self.infile
        print self.des
        try:
            filename=open(self.des,"r")
                
        except(IOError):
            self.flag=0
            self.msg.config(bg="red",fg="white")
            self.msg.insert(0,"FILE NOT FOUND!!")
            
            self.bttn_next.config(self,text="NEXT",state=NORMAL,command=self.next_call,bd=2,relief=RAISED)
            self.bttn_next.pack(side=RIGHT)
            self.bttn_auth.config(self,text="AUTHENTICATE",state=DISABLED,bd=2,relief=RAISED)
            self.bttn_auth.pack(side=LEFT)
            
        else:
            self.msg.config(bg="green",fg="white")
            self.msg.insert(0,"SELCECTION OK!!")
            self.bttn_next.config(self,text="NEXT",state=NORMAL,command=self.next_call,bd=2,relief=RAISED)
            self.bttn_next.pack(side=RIGHT)
            self.bttn_auth.config(self,text="AUTHENTICATE",state=DISABLED,bd=2,relief=RAISED)
            self.bttn_auth.pack(side=LEFT)
            filename.close()

    def next_call(self):
        root.destroy()
        
        
    


class AttachBscPd(Frame):
    def __init__(self, parent=None):         # add callback method
        Frame.__init__(self, parent)          # and pack myself
        self.pack( )
        self.create_widget()

    def create_widget(self):                                # default press action
        self.ob_bsctype=BscType(self)
        self.ob_bsctype.pack(side=LEFT)

        self.ob_packetdatatype=PacketDataType(self)
        self.ob_packetdatatype.pack(side=RIGHT)


        
class BscType(Frame):
    def __init__(self, parent=None):         # add callback method
        Frame.__init__(self, parent)          # and pack myself
        self.pack( )
        self.create_widget() 

    def create_widget(self):                                # default press action
        Label(self,text="BSCTYPE",
              font=("courier",10,'bold')).pack()
        self.bsctype_group=StringVar()
        self.bsctype_group.set("cbsc")
        Radiobutton(self,
                    text="C_BSC",
                    variable=self.bsctype_group,
                    value="cbsc").pack()
             
        Radiobutton(self,
                    text="E_BSC",
                    variable=self.bsctype_group,
                    value="ebsc").pack()

        
class PacketDataType(Frame):
    def __init__(self, parent=None):         # add callback method
        Frame.__init__(self, parent)          # and pack myself
        self.pack( )
        self.create_widget()
    def create_widget(self):                                # default press action
        Label(self,text="PACKET DATA TYPE",
              font=("courier",10,'bold')).pack()
        self.packetdatatype_group=StringVar()
        self.packetdatatype_group.set("gprs")
        Radiobutton(self,
                    text="GPRS",
                    variable=self.packetdatatype_group,
                    value="gprs").pack()
             
        Radiobutton(self,
                    text="EDGE",
                    variable=self.packetdatatype_group,
                    value="edge").pack()



class BtsType(Frame):
    def __init__(self, parent=None):         # add callback method
        Frame.__init__(self, parent)          # and pack myself
        self.pack( )
        self.create_widget()
        
    def create_widget(self):                                # default press action
        Label(self,text = "BTS TYPE",
              font=("courier",10,'bold')).pack()
        self.btstype_group=StringVar()
        self.btstype_group.set("macro")
         
        Radiobutton(self,
                    text="MACRO",
                    font=("courier",8),
                    variable=self.btstype_group,
                    value="macro").pack(side=LEFT,padx=5,pady=5)
        Radiobutton(self,
                    text="MICRO",
                    font=("courier",8),
                    variable=self.btstype_group,
                    value="micro").pack(side=LEFT,padx=30)

        Radiobutton(self,
                    text="I_B_S",
                    font=("courier",8),
                    variable=self.btstype_group,                        
                    value="ibs").pack(side=RIGHT,padx=5,pady=5)



class NC(Label):
    def __init__(self, parent=None):         # add callback method
        Label.__init__(self, parent)          # and pack myself
        self.pack( )
        self.create_widget()
    def create_widget(self):                                # default press action
        Label(self,text="CHOOSE SECTORS",
              font=("courier",10,'bold')).pack()
        self.cell_array=[]
        
    
        for n in range(1,7,1):
            var=IntVar()
            Checkbutton(self,
                        text=str(n),
                        variable=var).pack(side=LEFT,padx=5,pady=5)
            self.cell_array.append(var)


        frm = Frame(self)
        frm.pack()
   
    def cell_array_maker(self):
        n=0
        nos=0
        self.cell_no=[]
	self.vv=""
        for var in self.cell_array:
            n+=1
            if var.get():
                nos+=1
                self.vv+="_"+str(n)
                self.cell_no.append(n)
        print self.vv
	print self.cell_no
        return nos       

root=Tk()
app=AttachAll(root)
root.mainloop()
