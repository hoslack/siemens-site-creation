from Tkinter import *
import step1           #IMPORT STEP1 PROGRAM TO BRING FIRST WINDOW
import sys
import os
class Application(Frame):
        def __init__(self, master):
             Frame.__init__(self, master)
             self.grid()
             if step1.app.ob_btstype.btstype_group.get()=="micro" or step1.app.ob_btstype.btstype_group.get()=="ibs":
                     self.create_widget_micro()    #<------- APPLYING CONDITION TO CALL DIFFERENT WINDOW FOR MICRO/IBS AND MACRO
             else:
                     self.create_widget_macro()
                     
        
        def create_widget_micro(self):            #<-------- CREATE WINDOW FOR MICRO AND IBS

#HEADER

             row_id=1             
             Label(self,text="Site creation: STEP-2",
                   font=("VERDANA",10,"bold")).grid(row = row_id,column=2)
             row_id+=1
             Label(self,text="*****COMMON CONFIGURATIONS*****",
                   font=("VERDANA",10,"bold")).grid(row = row_id,column=2)
             

#BSS_ID
             
             row_id+=1
             Label(self,text = "BSS_ID:").grid(row = row_id, column = 0, sticky = W)
             self.bss_id = Entry(self)
             self.bss_id.grid(row = row_id, column = 1,sticky = W)      

#PCMB
             
             Label(self,text = "PCMB:").grid(row = row_id, column = 3, sticky = W)
             self.pcmb = Entry(self)
             self.pcmb.grid(row = row_id, column = 4,sticky = W)


#PCML

             row_id+=1
             if step1.app.ob_all.ob_bsctype.bsctype_group.get()=="ebsc":
                     Label(self,text = "PCMM:").grid(row = row_id, column = 0, sticky = W)
                     self.port_pcmm = Entry(self)
                     self.port_pcmm.grid(row = row_id, column = 1,sticky = W)
		     self.port_pcmm.insert(0,"4-5-TRUNKA")
             else:
                     Label(self,text = "PCML:").grid(row = row_id, column = 0, sticky = W)
                     self.port_pcml = Entry(self)
                     self.port_pcml.grid(row = row_id, column = 1,sticky = W)

#SIPLEX A/B                     
                     Label(self,text = "SIPLEX A/B:").grid(row = row_id, column = 3, sticky = W)
                     self.simplex_a_b = Entry(self)
                     self.simplex_a_b.grid(row = row_id, column = 4,sticky = W)
             	     self.simplex_a_b.insert(0,"SIMPLEXA")



             
             nc=step1.app.ob_nc.cell_array_maker()
             buf=step1.app.ob_nc.cell_no
                
             
             self.site_id=["s0","s1","s2","s3","s4","s5","s6"]
             self.btsm_id=["s0","s1","s2","s3","s4","s5","s6"]
             self.pcmb_tsl_start=["s0","s1","s2","s3","s4","s5","s6"]
             self.pcmb_tsl_stop=["s0","s1","s2","s3","s4","s5","s6"]
             self.abis_tsl=["s0","s1","s2","s3","s4","s5","s6"]
             self.sub_tsl=["s0","s1","s2","s3","s4","s5","s6"]
             self.lac=["s0","s1","s2","s3","s4","s5","s6"]
             self.racode=["s0","s1","s2","s3","s4","s5","s6"]
             self.apn=["s0","s1","s2","s3","s4","s5","s6"]
             self.lapdpool=["s0","s1","s2","s3","s4","s5","s6"]
             self.cell_st=["s0","s1","s2","s3","s4","s5","s6"]
             self.bsicz=["s0","s1","s2","s3","s4","s5","s6"]
             self.bcch=["s0","s1","s2","s3","s4","s5","s6"]
             self.tch=["s0","s1","s2","s3","s4","s5","s6"]
             self.symname_btsm=["s0","s1","s2","s3","s4","s5","s6"]
             self.symname_btsep=["s0","s1","s2","s3","s4","s5","s6"]
	     dum_bcch=["27","29","31","749","751","753"]
	     dum_tch=["33","35","37","755","757","759"]
#TITLE: VARIABLE CONFIGURATIONS



             
             for n in range(0,nc,1):
#SITE_ID
                     row_id+=1
                     Label(self,text="INPUT FOR SITE: "+str(buf[n]),
                     font=("VERDANA",10,"bold")).grid(row = row_id,column=2)
             
                     row_id+=1
                     Label(self,text = "Site_ID"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                     self.site_id[buf[n]] = Entry(self)
                     self.site_id[buf[n]].grid(row = row_id, column = 1,sticky = W)
                     
                             
#BTSM

                     Label(self,text = "Btsm_ID"+str(buf[n])+":").grid(row = row_id, column = 3, sticky = W)
                     self.btsm_id[buf[n]] = Entry(self)
                     self.btsm_id[buf[n]].grid(row = row_id, column = 4,sticky = W)



#PCMB_TSL_START

                     row_id+=1
                     Label(self,text = "PCMB_TSL_START"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                     self.pcmb_tsl_start[buf[n]]= Entry(self)
                     self.pcmb_tsl_start[buf[n]].grid(row = row_id, column = 1,sticky = W)

#PCMB_TSL_STOP

                     Label(self,text = "PCMB_TSL_STOP"+str(buf[n])+":").grid(row = row_id, column = 3, sticky = W)
                     self.pcmb_tsl_stop[buf[n]] = Entry(self)
                     self.pcmb_tsl_stop[buf[n]].grid(row = row_id, column = 4,sticky = W)

             
#ABIS_TSL
                     row_id+=1
                     Label(self,text = "ABIS_TSL"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                     self.abis_tsl[buf[n]] = Entry(self)
                     self.abis_tsl[buf[n]].grid(row = row_id, column = 1,sticky = W)

             
#SUB_TSL
                     Label(self,text = "SUB_TSL"+str(buf[n])+":").grid(row = row_id, column = 3, sticky = W)
                     self.sub_tsl[buf[n]] = Entry(self)
                     self.sub_tsl[buf[n]].grid(row = row_id, column = 4,sticky = W)

     
#LAC
                     row_id+=1

                     Label(self,text = "LAC"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                     self.lac[buf[n]] = Entry(self)
                     self.lac[buf[n]].grid(row = row_id, column = 1,sticky = W)


#RACODE
                     Label(self,text = "RACODE"+str(buf[n])+":").grid(row = row_id, column = 3, sticky = W)
                     self.racode[buf[n]] = Entry(self)
                     self.racode[buf[n]].grid(row = row_id, column = 4,sticky = W)



#LAPDPOOL

                     row_id+=1
                     if step1.app.ob_all.ob_bsctype.bsctype_group.get()=="ebsc":
                             Label(self,text = "APN"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                             self.apn[buf[n]] = Entry(self)
                             self.apn[buf[n]].grid(row = row_id, column = 1,sticky = W)
                     else:
                             Label(self,text = "LAPDPOOL"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                             self.lapdpool[buf[n]] = Entry(self)
                             self.lapdpool[buf[n]].grid(row = row_id, column = 1,sticky = W)



#CELL_ID

                     Label(self,text = "Cell_ID"+str(buf[n])+":").grid(row = row_id, column = 3, sticky = W)
                     self.cell_st[buf[n]] = Entry(self)
                     self.cell_st[buf[n]].grid(row = row_id, column = 4,sticky = W)

                     row_id+=1
                     Label(self,text = "BCCH"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                     self.bcch[buf[n]] = Entry(self)
                     self.bcch[buf[n]].grid(row = row_id, column = 1,sticky = W)
		     self.bcch[buf[n]].insert(0,dum_bcch[n])
                     Label(self,text = "TCH"+str(buf[n])+":").grid(row = row_id, column = 3, sticky = W)
                             
                     self.tch[buf[n]] = Entry(self)
                     self.tch[buf[n]].grid(row = row_id, column = 4,sticky = W)
		     self.tch[buf[n]].insert(0,dum_tch[n])
#BSIC

                     row_id+=1
                     Label(self,text = "BSIC"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                     self.bsicz[buf[n]] = Entry(self)
                     self.bsicz[buf[n]].grid(row = row_id, column = 1,sticky = W)

                    
                     row_id+=1
                     Label(self,text = "END OF INPUT FOR SECTOR"+str(buf[n])+":",
                           font=("VERDANA",10,"bold")).grid(row = row_id, column = 2, sticky = E)

                     
             row_id+=1
             Button(self,
             text="Execute",
             command=self.getValue_micro).grid(row = row_id, column = 1, sticky = W)


        def getValue_micro(self):
                buf=step1.app.ob_nc.cell_no
                nc=step1.app.ob_nc.cell_array_maker()
                        #si=self.site_id[3].get()
                bsctype=step1.app.ob_all.ob_bsctype.bsctype_group.get()
                pdtype=step1.app.ob_all.ob_packetdatatype.packetdatatype_group.get()
                btstype=step1.app.ob_btstype.btstype_group.get()
                filename=step1.app.infile
                path=os.getcwd()+"/unix/"+filename
                if step1.app.ob_all.ob_bsctype.bsctype_group.get()=="ebsc":
                        port="pcmm="+self.port_pcmm.get()
                else:
                        port="pcml="+self.port_pcml.get()
                                        


                print "\nReading characters from the file."


                        #text_file = open(string1, "r")
                text_file_o = open(self.site_id[buf[0]].get(),"w+")
                text_file_o.write("\t\t#*****COMMON PARAMETERS******#\n")
                text_file_o.write("bss_id="+self.bss_id.get()+"\n"
                                  +"pcmb_no="+self.pcmb.get()+"\n"
                                  +port+"\n"
                                  +"simplex_a_b="+self.simplex_a_b.get()+"\n"
                                  +"\t\t#*****DISTINCT PARAMETERS*****#\n")
                                                
                for n in range(0,nc,1):
                        #mi=n+4
                        self.symname_btsep[buf[n]]=self.site_id[buf[n]].get().replace('#','_')
                        self.symname_btsm[buf[n]]="Setsymbolicname btsm:BSS:$bss_id/BTSM:$btsm_id"+str(buf[n])+",symname=\""+self.site_id[buf[n]].get()+"\";"                  
                        self.symname_btsep[buf[n]]="Setsymbolicname btsep:BSS:$bss_id/BTSEP:$btsm_id"+str(buf[n])+",symname=\""+self.symname_btsep[buf[n]]+"\";"


                        if step1.app.ob_all.ob_bsctype.bsctype_group.get()=="ebsc":
                                sig_card="apn"+str(buf[n])+"="+self.apn[buf[n]].get()
                        else:
                                sig_card="lpdpool"+str(buf[n])+"="+self.lapdpool[buf[n]].get()
                        text_file_o.write("site_id"+str(buf[n])+"="+self.site_id[buf[n]].get()+"\n"
                                          "btsm_id"+str(buf[n])+"="+self.btsm_id[buf[n]].get()+"\n\n"
                                          "pcmb_tsl_start"+str(buf[n])+"="+self.pcmb_tsl_start[buf[n]].get()+"\n"
                                          "pcmb_tsl_stop"+str(buf[n])+"="+self.pcmb_tsl_stop[buf[n]].get()+"\n"
                                          "abis_tsl"+str(buf[n])+"="+self.abis_tsl[buf[n]].get()+"\n"
                                          "subtsl"+str(buf[n])+"="+self.sub_tsl[buf[n]].get()+"\n"
                                          "cell_id"+str(buf[n])+"="+self.cell_st[buf[n]].get()+"\n"
                                          +sig_card+"\n"
                                          "lac"+str(buf[n])+"="+self.lac[buf[n]].get()+"\n"
                                          "racod"+str(buf[n])+"="+self.racode[buf[n]].get()+"\n"
                                          "bsic"+str(buf[n])+"="+self.bsicz[buf[n]].get()+"\n"
                                          "bcchfreq_"+str(buf[n])+"="+self.bcch[buf[n]].get()+"\n"
                                          "tch_"+str(buf[n])+"="+self.tch[buf[n]].get()+"\n"
                                          +self.symname_btsm[buf[n]]+"\n"
                                          +self.symname_btsep[buf[n]]+"\n")
                        

                text_file = open(path, "r")
                whole_file=text_file.read()
                text_file.close()    
                text_file_o.write(whole_file)
                text_file_o.close()


                

        def create_widget_macro(self):
             row_id=1             
             Label(self,text="Site creation: STEP-2",
                   font=("VERDANA",10,"bold")).grid(row = row_id,column=2)
             
#BSS_ID
             
             row_id+=1
             Label(self,text = "BSS_ID:").grid(row = row_id, column = 0, sticky = W)
             self.bss_id = Entry(self)
             self.bss_id.grid(row = row_id, column = 1,sticky = W)      


#BTSM

             Label(self,text = "BTSM_ID").grid(row = row_id, column = 3, sticky = E)
             self.btsm_id = Entry(self)
             self.btsm_id.grid(row = row_id, column = 4,sticky = W)

#PCMB
             row_id+=1
             Label(self,text = "PCMB:").grid(row = row_id, column = 0, sticky = W)
             self.pcmb = Entry(self)
             self.pcmb.grid(row = row_id, column = 1,sticky = W)


#PCML




             
             if step1.app.ob_all.ob_bsctype.bsctype_group.get()=="ebsc":
                     Label(self,text = "PCMM:").grid(row = row_id, column = 3, sticky = E)
                     self.port_pcmm = Entry(self)
                     self.port_pcmm.grid(row = row_id, column = 4,sticky = W)
		     self.port_pcmm.insert(0,"4-5-TRUNKA")
             else:
                     Label(self,text = "PCML:").grid(row = row_id, column = 3, sticky = E)
                     self.port_pcml = Entry(self)
                     self.port_pcml.grid(row = row_id, column = 4,sticky = W)



#SITE_ID
                     
             row_id+=1
             Label(self,text = "Site_ID").grid(row = row_id, column = 0, sticky = W)
             self.site_id = Entry(self)
             self.site_id.grid(row = row_id, column = 1,sticky = W)

#SIPLEX A/B
             if step1.app.ob_all.ob_bsctype.bsctype_group.get()!="ebsc":

                     Label(self,text = "SIPLEX A/B:").grid(row = row_id, column = 3, sticky = E)
                     self.simplex_a_b = Entry(self)
                     self.simplex_a_b.grid(row = row_id, column = 4,sticky = W)
		     self.simplex_a_b.insert(0,"SIMPLEXA")


#PCMB_TSL_START

             row_id+=1
             Label(self,text = "PCMB_TSL_START:").grid(row = row_id, column = 0, sticky = W)
             self.pcmb_tsl_start= Entry(self)
             self.pcmb_tsl_start.grid(row = row_id, column = 1,sticky = W)
	     self.pcmb_tsl_start.insert(0,"1")
#PCMB_TSL_STOP

             Label(self,text = "PCMB_TSL_STOP").grid(row = row_id, column = 3, sticky = E)
             self.pcmb_tsl_stop = Entry(self)
             self.pcmb_tsl_stop.grid(row = row_id, column = 4,sticky = W)
	     self.pcmb_tsl_stop.insert(0,"30")

     
#ABIS_TSL
             row_id+=1
             Label(self,text = "ABIS_TSL").grid(row = row_id, column = 0, sticky = W)
             self.abis_tsl = Entry(self)
             self.abis_tsl.grid(row = row_id, column = 1,sticky = W)
	     self.abis_tsl.insert(0,"31")


#LAPDPOOL

             
             if step1.app.ob_all.ob_bsctype.bsctype_group.get()=="ebsc":
                     Label(self,text = "APN").grid(row = row_id, column = 3, sticky = E)
                     self.apn = Entry(self)
                     self.apn.grid(row = row_id, column = 4,sticky = W)
             else:
                     Label(self,text = "LAPDPOOL").grid(row = row_id, column = 3, sticky = E)
                     self.lapdpool = Entry(self)
                     self.lapdpool.grid(row = row_id, column = 4,sticky = W)



#LAC
             
             row_id+=1
             Label(self,text = "LAC").grid(row = row_id, column = 0, sticky = W)
             self.lac = Entry(self)
             self.lac.grid(row = row_id, column = 1,sticky = W)


             

#RACODE
             Label(self,text = "RACODE").grid(row = row_id, column = 3, sticky = E)
             self.racode = Entry(self)
             self.racode.grid(row = row_id, column = 4,sticky = W)


             nc=step1.app.ob_nc.cell_array_maker()
             buf=step1.app.ob_nc.cell_no
                
             self.cell_st=["s0","s1","s2","s3","s4","s5","s6"]
             self.bsicz=["s0","s1","s2","s3","s4","s5","s6"]
             self.bcch=["s0","s1","s2","s3","s4","s5","s6"]
             self.tch=["s0","s1","s2","s3","s4","s5","s6"]
	     dum_bcch=["27","29","31","749","751","753"]
	     dum_tch=["33","35","37","755","757","759"]


#BSIC

             row_id+=1

             Label(self,text = "BSIC").grid(row = row_id, column = 0, sticky = W)
             self.bsicz = Entry(self)
             self.bsicz.grid(row = row_id, column = 1,sticky = W)

#CELL_STRAT


             Label(self,text = "CELL_START").grid(row = row_id, column = 3, sticky = E)
             self.cell_st = Entry(self)
             self.cell_st.grid(row = row_id, column = 4,sticky = W)



             for n in range(0,nc,1):
                     #macro_index=n+1

                     row_id+=1
                     Label(self,text = "BCCH"+str(buf[n])+":").grid(row = row_id, column = 0, sticky = W)
                     self.bcch[buf[n]] = Entry(self)
                     self.bcch[buf[n]].grid(row = row_id, column = 1,sticky = W)
		     self.bcch[buf[n]].insert(0,dum_bcch[n])
                     Label(self,text = "TCH"+str(buf[n])+":").grid(row = row_id, column = 3, sticky = E)
                             
                     self.tch[buf[n]] = Entry(self)
                     self.tch[buf[n]].grid(row = row_id, column = 4,sticky = W)
                     self.tch[buf[n]].insert(0,dum_tch[n])
             row_id+=1
             Button(self,
             text="Execute",
             command=self.getValue_macro).grid(row = row_id, column = 1, sticky = W)




        def getValue_macro(self):
                buf=step1.app.ob_nc.cell_no
                print buf
                nc=step1.app.ob_nc.cell_array_maker()
                bsctype=step1.app.ob_all.ob_bsctype.bsctype_group.get()
                pdtype=step1.app.ob_all.ob_packetdatatype.packetdatatype_group.get()
                btstype=step1.app.ob_btstype.btstype_group.get()
                filename2=step1.app.infile
                path=os.getcwd()+"/unix/"+filename2
                print filename2
                print path
                if step1.app.ob_all.ob_bsctype.bsctype_group.get()=="ebsc":
                        port="pcmm="+self.port_pcmm.get()
                        sig_card="apn="+self.apn.get()
                else:
                        port="pcml="+self.port_pcml.get()
                        sig_card="lpdpool="+self.lapdpool.get()
                        
                        
                print "\nReading characters from the file."
                
                text_file_o = open(self.site_id.get(),"w+")
                text_file_o.write("site_id="+self.site_id.get()+"\n"
                                  +"bss_id="+self.bss_id.get()+"\n"
                                  +"btsm_id="+self.btsm_id.get()+"\n"
                                  +"pcmb_no="+self.pcmb.get()+"\n"
                                  +port+"\n"
                                  +sig_card+"\n")
                if step1.app.ob_all.ob_bsctype.bsctype_group.get()!="ebsc":
                        text_file_o.write("simplex_a_b="+self.simplex_a_b.get()+"\n")

                text_file_o.write("pcmb_tsl_start="+self.pcmb_tsl_start.get()+"\n"
                                  +"pcmb_tsl_stop="+self.pcmb_tsl_stop.get()+"\n"
                                  +"abis_tsl="+self.abis_tsl.get()+"\n"
                                  +"lac="+self.lac.get()+"\n"
                                  +"racod="+self.racode.get()+"\n\n")

                cell=int(self.cell_st.get())-1
                for n in range(0,nc,1):
                     cell+=1
                    # macro_index=n+1
                     text_file_o.write("cell_id"+str(buf[n])+"="+str(cell)+"\n"
                                       "bcchfreq_"+str(buf[n])+"="+self.bcch[buf[n]].get()+"\n"
                                       "tch_"+str(buf[n])+"="+self.tch[buf[n]].get()+"\n"
				       "bsic"+str(buf[n])+"="+self.bsicz.get()+"\n\n")


		symname_btsep=self.site_id.get().replace('#','_')
                symname_btsm="Setsymbolicname btsm:BSS:$bss_id/BTSM:$btsm_id,symname=\""+self.site_id.get()+"\";"                  
                symname_btsep="Setsymbolicname btsep:BSS:$bss_id/BTSEP:$btsm_id,symname=\""+symname_btsep+"\";"
                text_file_o.write(symname_btsm+"\n"+symname_btsep+"\n")

		

                text_file = open(path, "r")     
                whole_file=text_file.read()
                      
                text_file_o.write(whole_file)
                     
                text_file_o.close()
                text_file.close()

root1 = Tk()
root1.title("Site creation")
root1.config(bd=10,relief=GROOVE)
        
if step1.app.flag==1:
        print step1.app.flag
        app = Application(root1)
        root1.mainloop()

else:
        sys.exit()
        


                
                
                


             
             



    

