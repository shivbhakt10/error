from tkinter import *
from os import *
import pickle
from tkinter import messagebox
from random import choice
import hashlib
import csv
mainroot = Tk()



l=['a','b','c','d','f','1','2','3','4','5','6','7','8','9','0']
inl=[0,3,9,10,11,21,5,4]

class fun:
        def ltt(text):
                    textt=''
                    for i in text:
                              textt+=i
                    return textt
          
        def codee(text):
                    text=list(hashlib.md5(text.encode()).hexdigest())
                    for i in inl:
                              text.insert(i,choice(l))
                    textt=fun.ltt(text)
                    return textt
        def decodee(text):
                    text=list(text)
                    for i in inl:
                              text.pop(i)
                    teext=fun.ltt(text)
                    return teext



class mainfunction:
        def entrypass():
                  if path.exists('log1.dat') == False:

                            def gt():
                                      user=uE.get()
                                      passw1=psE.get()
                                      passw2=psEc.get()

                                      #if user !=None and passw1 !=None and passw2 !=None:
                                      if passw1==passw2:
                                                          passw=passw2
                                                          storel=[user,passw]
                                                          print(storel)
                                                          with open('mainps.csv','w') as f1:
                                                                csv.writer(f1).writerow(storel)
                                                                #pickle.dump(storel,f1)
                                                          logsc()
                                                          filename=user+'.csv'
                                                          with open(filename,'w') as f:
                                                                   pass
                                      else:
                                                          messagebox.showerror('Password eroor☠','confirmation password doesn\'t matched ....!')
                                                          psE.delete(0,END)
                                                          psEc.delete(0,END)
                                                          gt()

                                      #else:
                                               # messagebox.showerror('error☠','Please fill the requirements..!')



                            ul1=Label(text=' User :-',font='Arial 18 bold',bg='black',fg='orange')
                            ul1.place(x=25,y=185)
                            uE=Entry(mainroot,width=15,font='Arial 15 bold')
                            uE.place(x=120,y=190)

                            pl1=Label(text=' Password :-',font='Arial 18 bold',bg='black',fg='orange')
                            pl1.place(x=25,y=235)
                            psE=Entry(mainroot,width=15,font='Arial 15 bold')
                            psE.place(x=180,y=240)

                            pl1c=Label(text=' Confirm Password :-',font='Arial 18 bold',bg='black',fg='orange')
                            pl1c.place(x=25,y=290)
                            psEc=Entry(mainroot,width=15,font='Arial 15 bold')
                            psEc.place(x=280,y=295)

                            btok=Button(mainroot,text=' OK ',font='Arial 15 bold',fg='orange',bg='black',command=lambda:[gt(),uE.delete(0,END),psE.delete(0,END),psEc.delete(0,END)])
                            btok.place(x=300,y=400)

                  elif path.exists('log1.dat') == True:
                            logsc()
                  def logsc():
                            def gtt():
                                      user=uE.get()
                                      passw1=psE.get()
                                      with open('mainps.csv','r') as f:
                                                l=dict(csv.reader(f))
                                                if user in l:
                                                          l[user]==passw1
                                                          global filee
                                                          filee=user+'.csv'
                                                else:
                                                          messagebox.showerror('User not found',f'There is no user named {user} ..!')
                            ul1=Label(text=' User :-',font='Arial 18 bold',bg='black',fg='orange')
                            ul1.place(x=25,y=250)
                            uE=Entry(mainroot,width=15,font='Arial 15 bold')
                            uE.place(x=120,y=255)

                            pl1=Label(text=' Password :-',font='Arial 18 bold',bg='black',fg='orange')
                            pl1.place(x=25,y=310)
                            psE=Entry(mainroot,width=15,font='Arial 15 bold')
                            psE.place(x=180,y=315)
                            print(filee)


class mainc:
        
        
        mainroot.geometry('977x532')
        mainroot.minsize(width=977,height=532)
        mainroot.maxsize(width=977,height=532)
        mainroot.title('Password Manager')  
        p1 = PhotoImage(file = 'logot.png')
        mainroot.iconphoto(False,p1) #seting icon in title bar

        pm1=PhotoImage(file ='2.png')
        bgimg=Label(mainroot,image=pm1) # background image
        bgimg.pack(expand=True)

        pbtn1=PhotoImage(file= 'btnm1.png')
        btnimg1=Button(mainroot,image=pbtn1,borderwidth=0,command=lambda:[mainfunction.entrypass()])
        btnimg1.place(x=610,y=200)
        

        mainroot.mainloop()