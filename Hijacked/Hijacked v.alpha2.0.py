from tkinter import *
from tkinter import font
from tkinter import messagebox
import Dico_msg_Paco
import Dico_msg_Carla
import Dico_msg_Carla2
import Dico_msg_Lola
import variablesc

class AppP1():


        def __init__(self):
                
                self.MM = Tk()

                self.MM.title("Hijacked")
                self.MM.geometry ("515x700")

                self.MM.resizable(False, False)

                self.photol= PhotoImage(file="BEGINS9SCREEN3.png")
                self.photollab=Label(image=self.photol).grid(row=0, column=0, sticky='nsew')

                self.bouton3=Button(self.MM, text = "START", command = self.valider)
                self.bouton3.place(x=110,y=450)

                self.bouton2 = Button(self.MM, text = "CLOSE", command = self.MM.destroy) 
                self.bouton2.place(x=285,y=450)

                self.MM.mainloop()

        def valider(self):
                askyn=messagebox.askyesno('Assistance Technique','Utiliser la fonction modérateur? Si vous voulez jouer au jeu, cliquez Non')
                if askyn==True:
                        variablesc.askyn=1
                        AppP2seul.modérateur(self)
                elif askyn==False: 
                        AppP2seul(self.MM,0)
              
                

"""
---------------------------------------------------------------------------------------------------------------------
"""


class AppP2seul():

    def __init__(self,fenetre, nb):

        self.MM=fenetre
        self.MM.destroy()
        
        self.MM=Tk()
        self.MM.title("P234")
        self.MM.geometry("515x700")
        self.MM.resizable(False, False)


        if nb==0:
            self.canvas()
            self.case_reponse()
            self.buttons()
            self.msg_window()
            self.create_msg('08/02/2019','center','white')
            self.create_msg('Wesh babe','w','gray95')
            self.menu()
            self.presentation()


            
        elif nb==1:
            self.canvas()
            self.case_reponse()
            self.buttons()
            self.msg_window()
            self.create_msg('16/02/2019','center','white')
            self.create_msg('???????????','e','khaki')
            self.menu()

            self.retour.configure(state='normal')
            self.b.configure(state='disabled')
            self.SB.configure(state='disabled')

        elif nb==2:
            if variablesc.askyn==0:
                Dico_msg_Paco.x=14
                Dico_msg_Carla.y=16

            self.canvas()
            self.case_reponse()
            self.buttons()
            self.msg_window()
            self.create_msg('22/02/2019','center','white')
            self.create_msg("Salut bb désolé de ne pas t'avoir répondu. Je t'ai manqué?",'w','gray95')
            self.menu()


        self.MM.mainloop()

    
    def modérateur(self):

        print(Dico_msg_Carla.msg,'\n')
        print(Dico_msg_Paco.msg,'\n')
        
        print("\nJusqu'où avancer dans le scénario?")
        ask=int(input('\nx de Paco='))
        Dico_msg_Paco.x=ask
        Dico_msg_Carla.y=ask
        Dico_msg_Paco.x=int(Dico_msg_Paco.x-1)
        ask1=int(input('variablesc.c='))
        variablesc.c=ask1
                
        
        if ask<13:
            Dico_msg_Carla.y=int(Dico_msg_Carla.y-1)
            AppP2seul(self.MM,0)
        else:
            Dico_msg_Carla.y=int(Dico_msg_Carla.y+1)
            AppP2seul(self.MM,2)


        
        



    def presentation(self):
        self.text=open('presentation.txt','r')
        self.p=messagebox.showinfo('Hijacked alpha 1.5',self.text.read())
        self.text.close()
        
    def canvas(self):
            
        self.S9=PhotoImage(file="S9Interfacemsg.png")
        self.FEN=Canvas(self.MM, height=700 ,width=515)
        self.FEN.pack()
        self.FEN.create_image(0, 0,
                              image=self.S9,
                              anchor=NW)
        self.font=font.Font(self.MM,size=12,weight='bold',family='Helvetica')
        self.num=Label(self.FEN,text='+3376912****',
                       bg='white',font=self.font)
        self.num.place(x=110,y=70)







### PARTIE SELECTION ET ENVOI DE MESSAGE ###

        
        
        
    def case_reponse(self):
        self.reponse=LabelFrame(self.FEN, text="reponse a envoyer",
                             bg="white",
                             relief="groove",
                             padx=5, pady=1)
        self.reponse.pack()
        self.prereponse=Label(self.reponse,text="" ,bg="white")
        self.prereponse.pack(anchor="w")
        self.FEN.create_window(220,540,
                               height=40,
                               width=300,
                               window=self.reponse)
        
        
    def menu(self):
        self.b=Menubutton(self.FEN,
                          relief="flat",
                          bg='white',
                          text="selectioner un sms...",
                          direction='above',
                          wraplength=250)
        self.bListe =Menu(self.b, tearoff=0)
        self.b['menu'] = self.bListe
        self.bListe.add_command(label=Dico_msg_Carla.msg.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                command=self.var)
        self.bListe.add_command(label=Dico_msg_Carla.msg1.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                command=self.var1) 
        self.b.pack()
        self.FEN.create_window(190, 580,
                               width=225,
                               window=self.b)


        
        

    def var(self):
        self.x=self.bListe.entrycget(0,"label")
        self.prereponse.config(text=self.x)
        self.variable=0
        
    def var1(self):
        self.x=self.bListe.entrycget(1,"label")
        self.prereponse.config(text=self.x)
        self.variable=1

    def var2(self):
        self.x=self.bListe.entrycget(0,"label")
        self.prereponse.config(text=self.x)
        self.variable=2
        
    def update_menu(self):
        Dico_msg_Carla.y=int(Dico_msg_Carla.y+1)
        self.bListe.delete(0,1)
        self.bListe.add_command(label=Dico_msg_Carla.msg.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                command=self.var)
        self.bListe.add_command(label=Dico_msg_Carla.msg1.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                command=self.var1)
        


        



### PARTIE AFFICHAGE DES MESSAGES ###





       
        
    def msg_window(self):
        self.MW=Canvas(self.FEN,bg='white',
                       width=300,
                       height=420)
        
        self.scrol=Scrollbar(self.MW,
                             orient=VERTICAL)
        self.scrol.pack(side=RIGHT,fill=Y)
        self.scrol.config(command=self.MW.yview)
        self.MW.config(yscrollcommand=self.scrol.set)
        
        self.MW.pack()
        self.FEN.create_window(220,312,
                               height=420,
                               width=300,
                               window=self.MW)
        
        self.frame=Frame(self.MW,bg='white')
        self.MW_frame=self.MW.create_window((0,0),
                                            window=self.frame)
        self.frame.bind('<Configure>',self.on_frame_config)
        self.MW.bind('<Configure>',self.frame_width)
        self.MW.bind_all("<MouseWheel>", self._on_mousewheel)
       
    def _on_mousewheel(self, event):
        self.MW.yview_scroll(int(-1*(event.delta/120)),"units")
        
    def frame_width(self, event):
        MW_width = int(event.width-20)
        self.MW.itemconfig(self.MW_frame, width = MW_width)

    def on_frame_config(self, event):
        self.MW.config(scrollregion=self.MW.bbox("all"))






### PARTIE MESSAGES ###


        
        
    def create_msg(self,text,anchor,bg):
        self.msg=Label(self.frame,
                       text=text,
                       anchor=anchor,
                       bg=bg,
                       wraplength=250,
                       justify='left',
                       height=3)
        self.msg.pack(fill=X)
        self.frame.update()

    def msg_paco(self,sms):
        self.create_msg(sms,
                            'w',
                            'grey95')
        
    def throw_my_msg_in_MW(self):
        if self.prereponse['text']!='':
            self.create_msg('','e','khaki')
            self.msg['text']=self.prereponse['text']
            self.prereponse['text']=''
            self.scenario()
            
            
        else:
            messagebox.showerror('','Veuillez selectioner un SMS')

        self.MW.config(scrollregion=self.MW.bbox(ALL))
        self.MW.yview_moveto(1)
        

    
###### PARTIE SCENARIO ######


    def scenario(self):
        self.CHECKPOINT=0
        self.update_menu()
        #print("y=",Dico_msg_Carla.y)
        #print("x=",Dico_msg_Paco.x)
        #print("variable=",self.variable)
        
        if Dico_msg_Paco.x<=12:
            variablesc.passe=1
        if Dico_msg_Paco.x>12 and Dico_msg_Paco.x<14:
            variablesc.passe=0


            
        


        if Dico_msg_Paco.x==4 and self.variable==0:
            
            self.carlapic1()
            if self.askpic==False:
                self.variable=2
            elif self.askpic==True:
                self.bListe.delete(1)
                self.Carlaface=PhotoImage(file="Carla.png")
                self.mmsCarla=Label(self.frame,
                       image=self.Carlaface,
                                    anchor='ne',
                                    bg="white")
                self.mmsCarla.pack(fill=X)
                variablesc.c=0
            
                self.frame.update()
                

        elif Dico_msg_Paco.x==4 and self.variable==1:
            self.bListe.delete(0,1)
            self.bListe.add_command(label=Dico_msg_Carla.msg2.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                command=self.var2)
            self.bListe.add_command(label=Dico_msg_Carla.msg1.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                command=self.var1)








            

        if Dico_msg_Paco.x==5 and self.variable==2:
            variablesc.dejafait=0
        elif Dico_msg_Paco.x==5 and self.variable==1:
            variablesc.dejafait=1
            self.Carlaface=PhotoImage(file="Carla.png")
            self.mmsCarla=Label(self.frame,
                   image=self.Carlaface,
                                anchor="ne",
                                bg="white")
            self.mmsCarla.pack(fill=X)
            variablesc.c=0
            self.frame.update()
            
        elif Dico_msg_Paco.x==5 and self.variable==0:
            variablesc.dejafait=1





            
        if Dico_msg_Paco.x==6 and self.variable==1:
            if variablesc.dejafait==0:
                Dico_msg_Paco.x=int(Dico_msg_Paco.x-1)
                Dico_msg_Carla.y=int(Dico_msg_Carla.y-1)
                self.bListe.delete(0,1)
                self.bListe.add_command(label=Dico_msg_Carla.msg.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                    command=self.var)
                self.bListe.add_command(label=Dico_msg_Carla.msg1.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                    command=self.var1)
                self.Carlaface=PhotoImage(file="Carla.png")
                self.mmsCarla=Label(self.frame,
                   image=self.Carlaface,
                                anchor="ne",
                                bg="white")
                self.mmsCarla.pack(fill=X)
                variablesc.c=0
                self.frame.update()
                
                
                variablesc.dejafait=1
            else:
                self.carlapic2()
                self.Carlanude=PhotoImage(file="flou.png")
                self.mmsCarla1=Label(self.frame,
                       image=self.Carlanude,
                                     anchor="ne",
                                     bg="white")
                self.mmsCarla1.pack(fill=X)
                variablesc.c=1
                self.frame.update()
                
        if Dico_msg_Paco.x==6 and self.variable==1:
            self.bListe.delete(0)

        elif Dico_msg_Paco.x==6 and self.variable==0:
            self.bListe.delete(1)

        elif Dico_msg_Paco.x==6 and self.variable==2:
            self.bListe.delete(0)




#LE JOUR SUIVANT 

        if Dico_msg_Paco.x==7:
            self.create_msg('09/02/2019','center','white')
        if Dico_msg_Paco.x>=7:
            self.num['text']='Paco'
            self.pfPaco=PhotoImage(file="pfPaco.png")
            self.FEN.create_image(315,78, image=self.pfPaco)
        if Dico_msg_Paco.x>=7 and Dico_msg_Paco.x<=9:
            self.bListe.delete(1)








        if Dico_msg_Paco.x==10:
            self.text1=open('cinematique1.txt','r')
            self.p1=messagebox.showinfo('Cinématique',self.text1.read())
            self.text1.close()
            







        if Dico_msg_Paco.x==12 and self.variable==1:
            self.text2=open('cinematique2.txt','r')
            self.p2=messagebox.showinfo('Cinématique',self.text2.read())
            self.text2.close()
            variablesc.dejafait=0
            variablesc.c=2

        elif Dico_msg_Paco.x==12 and self.variable==0:
            self.text2bis=open('cinematique2bis.txt','r')
            self.p2bis=messagebox.showinfo('Cinématique',self.text2bis.read())
            self.text2bis.close()
            variablesc.dejafait=0
            






        
        if Dico_msg_Paco.x==13:
            if variablesc.dejafait==1:
                self.create_msg('15/02/2019','center','white')
                variablesc.dejafait=2
            elif variablesc.dejafait==2:
                self.create_msg('16/02/2019','center','white')
                variablesc.dejafait=3

        
            





        if Dico_msg_Carla.y==16:
            variablesc.CHECKPOINT=1 


        if variablesc.CHECKPOINT==1:
            messagebox.showinfo('CHECKPOINT',"Vous etes arrivés au CHECKPOINT. Vous avez débloqué le bouton Retour en haut à gauche!")
            messagebox.showinfo('CHECKPOINT',"Lola, la meilleure amie de Carla, vous a envoyé un message, allez voir!")
            self.retour.configure(state='normal')
            self.b.configure(state='disabled')
            self.SB.configure(state='disabled')

        
#DEBUT DE LA SECONDE PARTIE

        if Dico_msg_Paco.x==15:
                if variablesc.c==1:
                        self.variable=0
                elif variablesc.c==2:
                        self.variable=1



        if Dico_msg_Paco.x==16:
            if variablesc.c==2:
                if self.variable==0:
                        self.DMP=Dico_msg_Paco.msg1
                elif self.variable==1:
                        self.DMP=Dico_msg_Paco.msg
                self.L=Dico_msg_Paco.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Paco.x])
                self.msg_paco(self.DMPactual)
                Dico_msg_Paco.x=int(Dico_msg_Paco.x+1)
                self.variable=1
            elif variablesc.c==1:
                if self.variable==0:
                        self.DMP=Dico_msg_Paco.msg1
                elif self.variable==1:
                        self.DMP=Dico_msg_Paco.msg
                self.L=Dico_msg_Paco.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Paco.x])
                self.msg_paco(self.DMPactual)
                Dico_msg_Paco.x=int(Dico_msg_Paco.x+1)
                self.variable=0




                
            


        if variablesc.passe==1:
            if self.variable==0:
                self.DMP=Dico_msg_Paco.msg
                self.L=Dico_msg_Paco.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Paco.x])
                self.msg_paco(self.DMPactual)
                Dico_msg_Paco.x=int(Dico_msg_Paco.x+1)

            elif self.variable==1:
                self.DMP=Dico_msg_Paco.msg1
                self.L=Dico_msg_Paco.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Paco.x])
                self.msg_paco(self.DMPactual)
                Dico_msg_Paco.x=int(Dico_msg_Paco.x+1)

                
            elif self.variable==2:
                self.DMP=Dico_msg_Paco.msg2
                self.L=Dico_msg_Paco.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Paco.x])
                self.msg_paco(self.DMPactual)


                self.bListe.delete(0,1)
                self.bListe.add_command(label=Dico_msg_Carla.msg2.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                    command=self.var2)
                self.bListe.add_command(label=Dico_msg_Carla.msg1.get(Dico_msg_Carla.L[Dico_msg_Carla.y]),
                                    command=self.var1)
                Dico_msg_Paco.x=int(Dico_msg_Paco.x+1)




        
        if Dico_msg_Paco.x==20 and self.variable==0:
            self.text3=open('defaite2.txt','r')
            self.p3=messagebox.showinfo('DEFAITE',self.text3.read())
            self.text3.close()
        elif Dico_msg_Paco.x==20 and self.variable==1:
            self.text4=open('defaite1.txt','r')
            self.p4=messagebox.showinfo('DEFAITE',self.text4.read())
            self.text4.close()




        if Dico_msg_Paco.x==4:
            self.Pacoface=PhotoImage(file="Paco.png")
            self.mmsPaco=Label(self.frame,
                       image=self.Pacoface,
                               anchor='nw',
                               bg="white")
            self.mmsPaco.pack(fill=X)
            
            self.frame.update()
            






        if Dico_msg_Paco.x==13 and variablesc.dejafait==0:
            self.create_msg('14/02/2019','center','white')
            variablesc.dejafait=1




### PARTIE BOUTONS ###


            
    def carlapic1(self):
        self.askpic=messagebox.askyesno('QUESTION','Voulez-vous envoyer une photo de votre visage à Paco?',parent=self.FEN)

    def carlapic2(self):
        self.warnpic=messagebox.showwarning('ATTENTION',"Vous venez d'envoyer une photo de votre corps, cette action est irreversible",parent=self.FEN)


            
    def buttons(self):
        self.retourprincipal=Button(self.FEN,
                                    text="Quitter le jeu",
                                     command=self.retourprincp,
                                     relief='groove')
        self.FEN.create_window(220, 618,
                               width=250,
                               window=self.retourprincipal)




        
    
        self.SB=Button(self.FEN,
                       text="Envoi",
                       relief='flat',
                       command=self.throw_my_msg_in_MW,
                       bg='orange')
        self.SB.place() 
        self.FEN.create_window(330,580,
                               window=self.SB)



        self.imageretour=PhotoImage(file='S9retour.png')
        self.retour=Button(self.FEN,
                           image=self.imageretour,
                           state='disabled',
                           relief='flat',
                           borderwidth=0,
                           command=self.retourcontact)
        self.FEN.create_window(89, 79,
                               window=self.retour)

    def retourcontact(self):
        AppContact(self.MM)

        
    def retourprincp(self):
        self.quitter=messagebox.askokcancel('Quitter le jeu?','Voulez-vous quitter le jeu? La progression ne sera pas sauvegardé')
        if self.quitter==True:
            self.MM.destroy()




'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class AppContact():

    def __init__(self, fenetre):
        self.MM=fenetre
        self.MM.destroy()
        
        self.MM=Tk()
        self.MM.title("ContactMenu")
        self.MM.geometry("515x700")
        self.MM.resizable(False, False)

        self.canvas()
        self.buttons()


        self.MM.mainloop()


    def canvas(self):
        
        self.S9=PhotoImage(file="interface_contact.png")
        self.FEN=Canvas(self.MM, height=700 ,width=515)
        self.FEN.pack()
        self.FEN.create_image(0, 0,
                              image=self.S9,
                              anchor=NW)
        self.font=font.Font(self.MM,size=12,weight='bold',family='Helvetica')
        self.num=Label(self.FEN,text='   CONTACTS   ',
                       bg='white',font=self.font)
        self.num.place(x=100,y=70)
        
        self.FEN.bind("<Button-1>", self.selection)

        

    def selection(self,event):
        if event.x>75 and event.x<370:
            if event.y>104 and event.y<143: #Paco
                if variablesc.CHECKPOINT==1:
                    AppP2seul(self.MM,1)
                elif variablesc.CHECKPOINT==2:
                    AppP2seul(self.MM,2)
            elif event.y>143 and event.y<181: #Lola
                if variablesc.CHECKPOINT==1:
                    AppP3seul(self.MM,0)
                elif variablesc.CHECKPOINT==2:
                    AppP3seul(self.MM,1)
                
        

        

    def buttons(self):
        self.retourprincipal=Button(self.FEN,
                                    text="Quitter le jeu",
                                     command=self.retourprincp,
                                     relief='groove')
        self.FEN.create_window(220, 618,
                               width=250,
                               window=self.retourprincipal)




        self.imageretour=PhotoImage(file='S9retour.png')
        self.retour=Button(self.FEN,
                           image=self.imageretour,
                           state='disabled',
                           relief='flat',
                           borderwidth=0)
        self.FEN.create_window(89, 79,
                               window=self.retour)

        
    def retourprincp(self):
        self.quitter=messagebox.askokcancel('Quitter le jeu?','Voulez-vous quitter le jeu? La progression ne sera pas sauvegardé')
        if self.quitter==True:
            self.MM.destroy()



        

'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''



class AppP3seul():

    def __init__(self,fenetre,nb):

        self.MM=fenetre
        self.MM.destroy()
        
        self.MM=Tk()
        self.MM.title("MainMenu")
        self.MM.geometry("515x700")
        self.MM.resizable(False, False)

        if nb==0:
            self.canvas()
            self.case_reponse()
            self.menu()
            self.buttons()
            self.msg_window()
            self.create_msg('19/02/2019','center','white')
            self.create_msg("Carla tu aurais du me prevenir que tu sortais avec paco!!!","w","gray95")
        elif nb==1:
            self.canvas()
            self.case_reponse()
            self.buttons()
            self.msg_window()
            self.create_msg("Viens pas te plaindre s'il t'arrive qqchose",'w','grey95')
            self.menu()

            self.retour.configure(state='normal')
            self.b.configure(state='disabled')
            self.SB.configure(state='disabled')


        self.MM.mainloop()
        
        
    def canvas(self):
        self.S9=PhotoImage(file="S9Interfacemsg.png")
        self.FEN=Canvas(self.MM, height=700 ,width=515)
        self.FEN.pack()
        self.FEN.create_image(0, 0,
                              image=self.S9,
                              anchor=NW)


        self.font=font.Font(self.MM,size=12,weight='bold',family='Helvetica')
        self.num=Label(self.FEN,text='Lola ma bestie',
                       bg='white',font=self.font)
        self.num.place(x=110,y=70)

        self.pfLola=PhotoImage(file="pfLola.png")
        self.FEN.create_image(315,78, image=self.pfLola)      
        
    def case_reponse(self):
        self.reponse=LabelFrame(self.FEN, text="reponse a envoyer",
                             bg="white",
                             relief="groove",
                             padx=5, pady=1)
        self.reponse.pack()
        self.prereponse=Label(self.reponse,text="" ,bg="white")
        self.prereponse.pack(anchor="w")
        self.FEN.create_window(220,540,
                               height=40,
                               width=300,
                               window=self.reponse)
        
        
    def menu(self):
        self.b=Menubutton(self.FEN,
                          relief="flat",
                          bg='white',
                          text="selectioner un sms...",
                          direction='above',
                          wraplength=250)
        self.bListe =Menu(self.b, tearoff=0)
        self.b['menu'] = self.bListe
        self.bListe.add_command(label=Dico_msg_Carla2.msg.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),
                                command=self.var)
        self.bListe.add_command(label=Dico_msg_Carla2.msg1.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),
                                command=self.var1) 
        self.b.pack()
        self.FEN.create_window(190, 580,
                               width=225,
                               window=self.b)
        

    def var(self):
        self.x=self.bListe.entrycget(0,"label")
        self.prereponse.config(text=self.x)
        self.variable=0
        
    def var1(self):
        self.x=self.bListe.entrycget(1,"label")
        self.prereponse.config(text=self.x)
        self.variable=1

    def var2(self):
        self.x=self.bListe.entrycget(0,"label")
        self.prereponse.config(text=self.x)
        self.variable=2










        
    def msg_window(self):
        self.MW=Canvas(self.FEN,bg='white',
                       width=300,
                       height=420)
        
        self.scrol=Scrollbar(self.MW,
                             orient=VERTICAL)
        self.scrol.pack(side=RIGHT,fill=Y)
        self.scrol.config(command=self.MW.yview)
        self.MW.config(yscrollcommand=self.scrol.set)
        
        self.MW.pack()
        self.FEN.create_window(220,312,
                               height=420,
                               width=300,
                               window=self.MW)
        
        self.frame=Frame(self.MW,bg='white')
        self.MW_frame=self.MW.create_window((0,0),
                                            window=self.frame)
        self.frame.bind('<Configure>',self.on_frame_config)
        self.MW.bind('<Configure>',self.frame_width)
        self.MW.bind_all("<MouseWheel>", self._on_mousewheel)


        
    def _on_mousewheel(self, event):
        self.MW.yview_scroll(int(-1*(event.delta/120)),"units")
        
    def frame_width(self, event):
        MW_width = int(event.width-20)
        self.MW.itemconfig(self.MW_frame, width = MW_width)

    def on_frame_config(self, event):
        self.MW.config(scrollregion=self.MW.bbox("all"))
        
        
    def create_msg(self,text,anchor,bg):
        self.msg=Label(self.frame,
                       text=text,
                       anchor=anchor,
                       bg=bg,
                       wraplength=200,
                       justify='left',
                       height=3)
        self.msg.pack(fill=X)
        self.frame.update()
        
        self.MW.config(scrollregion=self.MW.bbox(ALL))
        
    def throw_my_msg_in_MW(self):
        if self.prereponse['text']!='':
            self.create_msg('','e','khaki')
            self.msg['text']=self.prereponse['text']
            self.prereponse['text']=''
            
            self.msg_lola()
            self.update_menu()

            
            
        else:
            messagebox.showerror('','Veuillez selectioner un SMS')

        self.MW.config(scrollregion=self.MW.bbox(ALL))
        self.MW.yview_moveto(1)
        
            
    def buttons(self):
        self.retourprincipal=Button(self.FEN,
                                    text="Quitter le jeu",
                                     command=self.retourprincp,
                                     relief='groove')
        self.FEN.create_window(220, 618,
                               width=250,
                               window=self.retourprincipal)




        
    
        self.SB=Button(self.FEN,
                       text="Envoi",
                       relief='flat',
                       command=self.throw_my_msg_in_MW,
                       bg='orange')
        self.SB.place() 
        self.FEN.create_window(330,580,
                               window=self.SB)



        self.imageretour=PhotoImage(file='S9retour.png')
        self.retour=Button(self.FEN,
                           image=self.imageretour,
                           state='disabled',
                           relief='flat',
                           borderwidth=0,
                           command=self.retourcontact)
        self.FEN.create_window(89, 79,
                               window=self.retour)

    def retourcontact(self):
        AppContact(self.MM)

        
    def retourprincp(self):
        self.quitter=messagebox.askokcancel('Quitter le jeu?','Voulez-vous quitter le jeu? La progression ne sera pas sauvegardé')
        if self.quitter==True:
            self.MM.destroy()





        

    
    def msg_mechant(self,sms):
        self.create_msg(sms,"w","grey95")

    
    def msg_lola(self):

        if variablesc.c==0:
            self.DMP=Dico_msg_Lola.msgrien2
            self.L=Dico_msg_Lola.L
            self.DMPactual=self.DMP.get(self.L[Dico_msg_Lola.x])
            self.create_msg(self.DMPactual,'w','gray95')
            Dico_msg_Lola.x=int(Dico_msg_Lola.x+1)
            

        if variablesc.c==1 and Dico_msg_Carla2.x!=5:
            if Dico_msg_Carla2.x==7 and self.variable==0:
                self.DMP=Dico_msg_Lola.msgphoto
                self.L=Dico_msg_Lola.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Lola.x])
                self.create_msg(self.DMPactual,'w','gray95')
                Dico_msg_Lola.x=int(Dico_msg_Lola.x+1)
            else:
                self.DMP=Dico_msg_Lola.msgphoto
                self.L=Dico_msg_Lola.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Lola.x])
                self.create_msg(self.DMPactual,'w','gray95')
                Dico_msg_Lola.x=int(Dico_msg_Lola.x+1)


            if Dico_msg_Carla2.x==5 and self.variable==0:
                Dico_msg_Carla2.x=int(Dico_msg_Carla2.x+1)
                self.bListe.delete(0,1)
                self.bListe.add_command(label=Dico_msg_Carla2.msgphoto1.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),command=self.var)
                self.bListe.add_command(label=Dico_msg_Carla2.msgphoto2.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),command=self.var)
            elif Dico_msg_Carla2.x==6 and self.variable==1:
                print("jnvnje")
                

        
        if variablesc.c!=0 and variablesc.c!=1 and Dico_msg_Carla2.x!=5:
            self.DMP=Dico_msg_Lola.msgreste
            self.L=Dico_msg_Lola.L
            self.DMPactual=self.DMP.get(self.L[Dico_msg_Lola.x])
            self.create_msg(self.DMPactual,'w','gray95')
            Dico_msg_Lola.x=int(Dico_msg_Lola.x+1)
        




    def update_menu(self):
        variablesc.passe=1
       

        if variablesc.c == 0:
            Dico_msg_Carla2.x=int(Dico_msg_Carla2.x+1)
            self.bListe.delete(0,1)
            self.bListe.add_command(label=Dico_msg_Carla2.msgrien2.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),command=self.var)

            if Dico_msg_Carla2.x==6:
                text1=open('victoire1.txt','r')
                p1=messagebox.showinfo('Victoire!',text1.read())
                text1.close()
                self.MM.destroy()

        
        if variablesc.c == 1:

            
            Dico_msg_Carla2.x=int(Dico_msg_Carla2.x+1)
            self.bListe.delete(0,1)
            self.bListe.add_command(label=Dico_msg_Carla2.msgphoto1.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),command=self.var)
            'self.bListe.add_command(label=Dico_msg_Carla2.msgphoto2.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),command=self.var1)'

            if Dico_msg_Carla2.x==5 or Dico_msg_Carla2.x==6 or Dico_msg_Carla2.x==7:
                self.bListe.add_command(label=Dico_msg_Carla2.msgphoto2.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),command=self.var1)

            
            
            if Dico_msg_Carla2.x==6 and self.variable==1: 

                self.DMP=Dico_msg_Lola.msgphoto2
                self.L=Dico_msg_Lola.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Lola.x])
                self.create_msg(self.DMPactual,'w','gray95')
                Dico_msg_Lola.x=int(Dico_msg_Lola.x+1)
                

            

            elif Dico_msg_Carla2.x==6 and self.variable==0:
                self.DMP=Dico_msg_Lola.msgphoto
                self.L=Dico_msg_Lola.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Lola.x])
                self.create_msg(self.DMPactual,'w','gray95')
                Dico_msg_Lola.x=int(Dico_msg_Lola.x)
                variablesc.CHECKPOINT=2

            if Dico_msg_Carla2.x==7 and self.variable == 1:
                text1=open('victoire2.txt','r')
                p1=messagebox.showinfo('Victoire!',text1.read())
                text1.close()
                self.MM.destroy()

            elif Dico_msg_Carla2.x==7 and self.variable == 0:
                variablesc.CHECKPOINT=2

                    
            
                

        if variablesc.c == 2:
            Dico_msg_Carla2.x=int(Dico_msg_Carla2.x+1)
            self.bListe.delete(0,1)
            self.bListe.add_command(label=Dico_msg_Carla2.msgvideo1.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),command=self.var) 

            if Dico_msg_Carla2.x==5 or Dico_msg_Carla2.x==6:
                self.bListe.add_command(label=Dico_msg_Carla2.msgvideo2.get(Dico_msg_Carla2.L[Dico_msg_Carla2.x]),command=self.var1)
            

            if Dico_msg_Carla2.x==6 and self.variable==0: 

                self.DMP=Dico_msg_Lola.msgreste2
                self.L=Dico_msg_Lola.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Lola.x])
                self.create_msg(self.DMPactual,'w','gray95')
                Dico_msg_Lola.x=int(Dico_msg_Lola.x)


            elif Dico_msg_Carla2.x==6 and self.variable==1:
                self.DMP=Dico_msg_Lola.msgreste
                self.L=Dico_msg_Lola.L
                self.DMPactual=self.DMP.get(self.L[Dico_msg_Lola.x])
                self.create_msg(self.DMPactual,'w','gray95')
                Dico_msg_Lola.x=int(Dico_msg_Lola.x)
                
                variablesc.CHECKPOINT=2

            if Dico_msg_Carla2.x==7 and self.variable == 1:
                text1=open('victoire2.txt','r')
                p1=messagebox.showinfo('Victoire!',text1.read())
                text1.close()
                self.MM.destroy()


            if Dico_msg_Carla2.x==7 and self.variable == 0:
                variablesc.CHECKPOINT=2


        if variablesc.CHECKPOINT==2:
            messagebox.showinfo('CHECKPOINT',"Vous etes arrivés au CHECKPOINT. Vous avez redébloqué le bouton Retour en haut à gauche!")
            messagebox.showwarning('ATTENTION',"Paco vous à envoyé un message. De quoi peut-il s'agir?")
            self.retour.configure(state='normal')
            self.b.configure(state='disabled')
            self.SB.configure(state='disabled')


        
        
        



'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''



AppP1()


