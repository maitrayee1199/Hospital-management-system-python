import tkinter as tk
from PIL import ImageTk,Image
import h_backend
from tkcalendar import Calendar,DateEntry
import datetime
import time
import admin
class hospital:
    login_status=0
    def __init__(self):
        self.backend=h_backend.h_backend()
        self.ambulance_call_count=0
        self.appointment_call_count=0
    '''CREATE WINDOW'''
    def create_window(self):
        self.window=tk.Tk()
        self.screen_width=self.window.winfo_screenwidth()
        self.screen_height=self.window.winfo_screenheight()
        res=str(self.screen_width)+'x'+str(self.screen_height)
        self.window.geometry(res+'0'+'0')
        self.window.configure(bg='#ddddff')
        self.window.title('City Hospital')
        self.window.update()
    '''homepage'''
    def homepage(self,*args):
        try:
            for i in args:
                i.destroy()
        except:pass
        finally:
            self.window.configure(bg='#ddddff')
            '''PARENT FRAME'''
            self.frame=tk.Frame(self.window,width=self.screen_width,height=self.screen_height,bg='red')
            self.frame.pack(fill='both',expand='yes')
            '''WELCOME'''
            text=tk.Label(self.frame,text="Welcome To City Hospital",font=('times',30,'italic'),fg='#aaaaff',bg='#000000')
            text.pack(side=tk.TOP,fill='both',expand='no')
            '''BRANCHES AND CONTACT'''
            contact_parent=tk.Label(self.frame,bg='black')
            contact_parent.pack(side=tk.BOTTOM,fill='x')
            branch1=tk.Label(contact_parent,text='gulmarg road , outer Noida , Delhi NCR \n9876501234',font=('times',20,'bold'),relief='raised')
            branch1.pack(side=tk.LEFT)
            branch2=tk.Label(contact_parent,text='Shastri Nagar , south Delhi \n9376501234',font=('times',20,'bold'),relief='raised')
            branch2.pack(side=tk.LEFT)
            branch3=tk.Label(contact_parent,text='Patrakarpuram , Gomtinagar , Lucknow \n9876501234',font=('times',20,'bold'),relief='raised')
            branch3.pack(side=tk.LEFT)
            '''SERVICES FRAME'''
            frame1=tk.Frame(self.frame)
            frame1.pack(side=tk.LEFT,fill='y')
            services=tk.Label(frame1)
            services.config(text="We are at your service 24/7 \nBook your appointments with our specialists \nGet Ambulance service fast and efficient")
            services.config(font=('times',22,'italic'),justify=tk.LEFT,relief='flat')
            services.pack()
            '''IMAGE'''
            image_frame=tk.Frame(self.frame)
            image_frame.pack(side=tk.LEFT,fill='both',expand='yes')
            path=Image.open('hospital.jpg')
            img=ImageTk.PhotoImage(path,10)
            image=tk.Label(image_frame,image=img)
            image.photo=img#anchors image to object else will load blank image
            image.pack(side=tk.TOP,fill='y',expand='no')
            '''LOGIN BUTTONS'''
            buttons_frame=tk.Frame(self.frame,bg='#aabbff')
            buttons_frame.pack(side=tk.LEFT,fill='both')
            user_login=tk.Button(buttons_frame,bg='black',fg='white',text='LOGIN',font=('calibri'))
            user_login.config(command=lambda:obj.login('user'))
            user_login.grid(row=1)
            button=tk.Button(buttons_frame,bg='#aabbff',state='disabled',bd=0)
            button.grid(row=2)
            user_signup=tk.Button(buttons_frame,bg='black',fg='white',text='SIGN UP',font=('calibri'),width=10)
            user_signup.config(command=lambda:obj.login('new user'))
            user_signup.grid(row=3)
            button=tk.Button(buttons_frame,bg='#aabbff',state='disabled',bd=0)
            button.grid(row=4)
            admin_login=tk.Button(buttons_frame,bg='black',fg='white',text='LOGIN AS ADMIN',font=('calibri'),width=20)
            admin_login.config(command=lambda:obj.login('admin'))
            admin_login.grid(row=5)
            button=tk.Button(buttons_frame,bg='#aabbff',state='disabled',bd=0)
            button.grid(row=6)
            path=Image.open('word_cloud2.jpg')
            img=ImageTk.PhotoImage(path,10)
            image=tk.Label(buttons_frame,image=img)
            image.photo=img#anchors image to object else will load blank image
            image.grid(row=7,columnspan=1)
    '''ACCOUNT VERIFICATION'''
    def verify(self,type_,*value):
        if type_=='signin':
            status=self.backend.signin(value[0],value[1],value[2],value[3],value[4])
            if status==1:
                obj.booking_page1(value[4])
        elif type_=='login':
            status=self.backend.check_password(value[0],value[1],value[2])
            if status==1 and value[2]=='ad':
                obj.admin_page(value)
                return
            if status==1:
                obj.booking_page1(value[0])
    def admin_page(self,*value):
        try:
            self.blank_frame.destroy()
            self.details.destroy()
        except:pass
        finally:
            back=tk.Button(self.window,text='BACK',command=lambda:obj.homepage(object_.sbarV,object_.sbarH,object_,back))
            back.pack()
            object_=admin.MyCanvas()
            object_.define(parent=self.window,data=self.backend.admin_rights())
    '''AMBULANCE BOOKING FRAME '''
    def load_ambulance_booking(self,parent_frame,count):
        self.ambulance_call_count=count
        try:
            self.app_frame.destroy()
            self.ambulance_call_count=1
        except:pass
        self.submit_count=0
        #if button is pressed more than once
        if self.ambulance_call_count>1:
            return
        self.ambulance_frame=tk.Frame(parent_frame)
        self.ambulance_frame.config(width=parent_frame.winfo_width(),height=parent_frame.winfo_height(),bg='pink')
        self.ambulance_frame.pack_propagate(0)
        self.ambulance_frame.pack()
        distance_frame=tk.Frame(self.ambulance_frame)
        distance_frame.config(width=parent_frame.winfo_width(),bg='white')
        distance_frame.pack(fill='x')
        distance=tk.Label(distance_frame,text='enter distance in KM')
        distance.pack(side=tk.LEFT)
        enter_d=tk.Entry(distance_frame,text='0',fg='black')
        enter_d.pack(side=tk.LEFT)
        blank_button=tk.Button(distance_frame,relief='flat',state='disabled')
        blank_button.pack(side=tk.LEFT)
        submit_button=tk.Button(distance_frame,text='Submit',bg='blue',fg='white')
        book=tk.Button(self.ambulance_frame,text='Book\nAmbulance',bg='blue',fg='black',font=('bold'),state='active')
        book.config(command=lambda:obj.print_booked('ambulance',self.ambulance_frame,book,int(enter_d.get())))
        book.pack(side=tk.BOTTOM)
        self.dp=['']
        submit_button.config(command=lambda:obj.booking_load('ambulance',self.ambulance_frame,enter_d.get(),self.submit_count+1,self.dp,book))
        submit_button.pack(side=tk.LEFT)
    '''GENERATE BILL'''
    def generate_bill(self,type_,*details):
        try:
            self.booking1_frame.destroy()
        except:
            pass
        finally:
            self.window.config(bg='#111144',bd=4,highlightcolor='#ffffff')
            self.window.update()
            #parent frame
            self.parent_frame=tk.Label(self.window)
            self.parent_frame.update()          
            self.parent_frame.config(bg='#111144',fg='#000000')
            self.parent_frame.pack()
            self.window.update_idletasks()
            back=tk.Label(self.parent_frame,width=self.window.winfo_screenwidth())
            back.pack_propagate(0)
            button=tk.Button(back,text='BACK',bg='black',fg='white',command=lambda:obj.booking_page1(details[0][3]))
            button.pack(side=tk.LEFT)
            back.pack()
            booked=tk.Label(self.parent_frame,text='BOOKING SUCCESSFUL'+'\n\n',font=('times',20,'italic','bold'),fg='dark green',bg='pink')
            booked.pack(fill=tk.BOTH)
            bill_form=tk.Label(self.parent_frame,width=self.parent_frame.winfo_width(),height=self.parent_frame.winfo_height())
            bill_form.config(bg='blue')
            bill_form.pack(fill='y')
            name=tk.Label(bill_form,width=100,height=2)
            name.pack_propagate(0)
            set_=tk.Label(name,text='Name: '+details[0][0],font=('times',12))
            set_.pack(side=tk.LEFT)
            name.pack()
            address=tk.Label(bill_form,width=100,height=5)
            address.pack_propagate(0)
            set_=tk.Label(address,text='Address: '+details[0][1]['house_no']+'\n'+
                             ''*len('address')+details[0][1]['area']+'\n'+''*len('address')
                             +details[0][1]['city']+'\n'+''*len('address')+details[0][1]['landmark'],font=('times',12))
            set_.pack(side=tk.LEFT)
            address.pack()
            contact=tk.Label(bill_form,width=100,height=2)
            contact.pack_propagate(0)
            set_=tk.Label(contact,text='Contact Number: '+details[0][2],font=('times',12))
            set_.pack(side=tk.LEFT)
            contact.pack()
            if type_=='ambulance':
                ambulance=tk.Label(bill_form,width=100,height=6)
                ambulance.pack_propagate(0)
                y=time.localtime(time.time())[0]
                m=time.localtime(time.time())[1]
                d=time.localtime(time.time())[2]
                set_=tk.Label(ambulance,text='Ambulance ID '+details[1]['ambulance_id']+'\n'+'Ambulance number '+details[1]
                              ['ambulance_no']+'\n'+"Driver's contact number "+details[1]['driver_contact']+'\nCost '+details[1]['cost']+'\nBooked on:'+str(
                                  datetime.date(y,m,d)),font=('times',12)
                              ,justify=tk.LEFT)
                set_.pack(side=tk.LEFT)
                ambulance.pack()
            else:
                appointment=tk.Label(bill_form,width=100,height=8)
                appointment.pack_propagate(0)
                set_=tk.Label(appointment,text=details[1]+'\nDate: '+str(details[2]),font=('times',12),justify=tk.LEFT)
                set_.pack(side=tk.LEFT)
                appointment.pack()
    '''PRINT BOOKED'''
    def print_booked(self,value,parent_frame,button,d,*details):
        if value=='ambulance':
            status=self.backend.update_user_bookings(self.u_details[3],'ambulance',time.strftime("%d-%m-%Y",time.localtime(time.time()))+'\n'+self.a['ambulance_id'])
            if status==1:
                booked=tk.Label(parent_frame,text='AMBULANCE BOOKED'+'\n\n',font=('times',20,'italic','bold'),fg='dark green',bg='pink')
                booked.pack()
                get_bill=tk.Button(booked,command=lambda:obj.generate_bill('ambulance',self.u_details,self.a),text='Get Bill')
                get_bill.pack()
                self.b=booked
                self.backend.update_ambulance_details(d)
        else:
            #protect nested tupling
            a=details[1]
            doctor_det=a
            status=self.backend.update_user_bookings(self.u_details[3],'doctor',str(d)+'\n'+a['id'])
            if status==1:
                booked=tk.Label(parent_frame,text='APPOINTMENT BOOKED'+'\n\n',font=('times',20,'italic','bold'),fg='dark green',bg='white')
                booked.pack()
                get_bill=tk.Button(parent_frame,command=lambda:obj.generate_bill('appointment',self.u_details,details[0],d),text='Get Bill')
                get_bill.pack()
                self.backend.update_doc_details(doctor_det,d)
    '''LOAD BOOKING DETAILS'''
    def booking_load(self,value,parent_frame,d,count,dp,button):
        self.submit_count=count
        #if blank distance if given
        if d=='':
            self.backend.load_ambulance_details(d)
            self.submit_count-=1
            return
        #if same distance is enterd twice
        if count>1 and d==self.dp[count-1]:
            self.dp.append(d)
            return
        if value=='ambulance':
            self.dp.append(d)
            self.a=self.backend.load_ambulance_details(d)
            if self.a==None:
                return
            #if distance entered is not same as previous one
            if count>1 and d!=self.dp[count-1]:
                self.submit_count=1
                button.config(state='active')
                try:
                    self.label0.destroy()
                except:
                    pass
                try:
                    self.b.destroy()   
                except:pass
            v='Ambulance ID '+self.a['ambulance_id']+'\n'+'Ambulance number '+self.a['ambulance_no']+'\n'+"Driver's contact number "+self.a['driver_contact']+'\nCost '+self.a['cost']
            self.label0=tk.Label(parent_frame,height=parent_frame.winfo_height())
            self.label0.pack(side=tk.LEFT,fill='y')
            label=tk.Label(self.label0,text=v,justify=tk.LEFT,font=15)
            label.pack()
    '''LOAD DOCTOR DETAILS'''
    def load_doc(self,value):
            try:
                self.display.destroy()
            except:pass
            date=list()
            def store_date(val):
                date.append(val)
            def get_date():
                try:
                    x=date[-1]
                    book_button.config(command=lambda:obj.print_booked('appointment',self.display,book_button,date[-1],det,doc_details))
                except:
                    self.backend.prompt('choose date please')
            doc_details=self.backend.getapp_details(value)
            det="Doctor's Name : "+doc_details['name']+'\nEducation : '+doc_details['education']+'\nCabin : '+doc_details['cabin']+'\nFees : '+doc_details['fees']+'\ntime :'+doc_details['time']
            self.display=tk.Label(self.app_frame,text=det,font=('times',12,'bold'),justify=tk.LEFT,width=self.app_frame.winfo_width()//5,bg='white')
            self.display.pack_propagate(0)
            self.display.pack(side=tk.LEFT,fill='y')
            choose_date=tk.Button(self.display,text='Choose Date')
            choose_date.config(command=lambda:get_calendar())
            choose_date.pack()
            book_button=tk.Button(self.display,text='Book Appointment')
            book_button.config(command=lambda:get_date())
            book_button.pack(side=tk.BOTTOM)
            def get_calendar():
                win=tk.Tk()
                cal=Calendar(win)
                year=time.localtime(time.time())[0]
                month=time.localtime(time.time())[1]
                date=time.localtime(time.time())[2]
                if month==12:
                    cal.config(mindate=datetime.date(year,month,date),maxdate=datetime.date(year+1,1,date))
                elif month==1 and date>28:
                    cal.config(mindate=datetime.date(year,month,date),maxdate=datetime.date(year,month+1,28))
                else:
                    try:
                        cal.config(mindate=datetime.date(year,month,date),maxdate=datetime.date(year,month+1,date))
                    except ValueError:
                        cal.config(mindate=datetime.date(year,month,date),maxdate=datetime.date(year,month+1,date-1))
                cal.config(showweeknumbers=False,disabledbackground='red',disabledforeground='blue',
                           disabledselectbackground='pink',disabledselectforeground='purple'
                           ,disableddaybackground='red')
                cal.pack()
                select_button=tk.Button(cal,text='Select Date',command=lambda:store_date(cal.selection_get()))
                select_button.pack(side=tk.LEFT)
                ok_button=tk.Button(cal,text='OK',command=lambda:win.destroy())
                ok_button.pack(side=tk.LEFT)
                cal.mainloop()        
    '''APPOINTMENT BOOKING FRAME'''
    def load_appointment_booking(self,parent_frame,count):
        self.appointment_call_count=count
        try:
            self.ambulance_frame.destroy()
            self.appointment_call_count=1
        except:
            pass
        #if button is pressed more than once
        if self.appointment_call_count>1:
            return
        #parent frame
        self.app_frame=tk.Label(parent_frame,width=parent_frame.winfo_width(),height=parent_frame.winfo_height(),bg='pink')
        self.app_frame.pack_propagate(0)
        self.app_frame.pack()
        choose_doc=tk.Label(self.app_frame,bg='white')
        choose_doc.pack(side=tk.LEFT,fill='y')
        doc=tk.Label(choose_doc,text='Choose doctor',font=('times',20,'italic','bold'),fg='black',bg='white')
        doc.pack(fill='y')
        heart=tk.Button(choose_doc,text='Heart\nspecialist',font=('times',10),bg='pink',fg='blue',width=10)
        heart.config(command=lambda:obj.load_doc('heart'))
        heart.pack()
        fake_button=tk.Button(choose_doc,state='disabled',relief='flat',bg='white')
        fake_button.pack()
        dentist=tk.Button(choose_doc,text='Dentist',font=('times',10),bg='pink',fg='blue',width=10)
        dentist.config(command=lambda:obj.load_doc('dentist'))
        dentist.pack()
        fake_button=tk.Button(choose_doc,state='disabled',relief='flat',bg='white')
        fake_button.pack()
        gen=tk.Button(choose_doc,text='General\nPhysician',font=('times',10),bg='pink',fg='blue',width=10)
        gen.config(command=lambda:obj.load_doc('gen'))
        gen.pack()
    '''BOOKING PAGE 1'''
    def booking_page1(self,username):
        try:
            self.parent_frame.destroy()
        except:pass
        try:
            self.details.destroy()
            self.blank_frame.destroy()
        except:pass
        finally:
            self.u_details=self.backend.get_details(username)#####return user details using username as key
            self.ambulance_call_count=0
            self.appointment_call_count=0
            self.window.configure(bg='#aaaaff')
            self.booking1_frame=tk.Frame(self.window,bg='white',height=self.window.winfo_screenheight(),width=self.window.winfo_screenwidth())
            self.booking1_frame.pack_propagate(False)
            self.booking1_frame.pack()
            back=tk.Frame(self.booking1_frame,bg='white',height=self.window.winfo_screenheight()//3,width=self.window.winfo_screenwidth())
            back.pack(fill='x')
            back_button=tk.Button(back,text='BACK',bg='black',fg='white')
            back_button.config(command=lambda:obj.homepage(self.booking1_frame))
            back_button.pack(side=tk.LEFT)
            book_ambulance_frame=tk.Frame(self.booking1_frame)
            book_ambulance_frame.config(height=self.window.winfo_screenheight()//4,bg='white',width=self.window.winfo_screenwidth()-100)
            book_ambulance_frame.pack_propagate(False)
            book_ambulance_frame.pack(side=tk.TOP,fill='x')
            a_button=tk.Button(book_ambulance_frame,text='Book Ambulance',fg='#ff1111',font=15,bd=0,bg='white',relief='flat')
            a_button.config(command=lambda:obj.load_ambulance_booking
                            (book_appointment_frame,self.ambulance_call_count+1))
            a_button.pack(side=tk.LEFT)
            d_button=tk.Button(book_ambulance_frame,text='Book Appointment',fg='#ff1111',font=15,bd=0,bg='white',relief='flat')
            d_button.config(command=lambda:obj.load_appointment_booking(book_appointment_frame,self.appointment_call_count+1))
            d_button.pack(side=tk.RIGHT)
            path=Image.open('ambulance.jpg')
            img=ImageTk.PhotoImage(path)
            image=tk.Label(book_ambulance_frame,image=img)
            image.photo=img
            image.pack()
            book_appointment_frame=tk.Frame(self.booking1_frame,bg='pink',height=self.window.winfo_screenheight(),width=self.window.winfo_screenwidth())
            book_appointment_frame.pack(side=tk.RIGHT)
            book_appointment_frame.pack_propagate(False)
            user_details=tk.Frame(book_appointment_frame,bg='light blue',width=self.window.winfo_screenwidth()//4)
            user_details.pack(side=tk.LEFT,fill='y')
            user_details.pack_propagate(False)
            details=tk.Label(user_details,text='YOUR DETAILS')
            details.pack()
            address=self.u_details[1]['house_no']+'\n'+''*len('address')+self.u_details[1]['area']+'\n'+''*len('address')+self.u_details[1]['city']+'\n'+''*len('address')+self.u_details[1]['landmark']
            name=tk.Label(user_details,text='Name : %s\nAddress : %s\nContact  : %s\nUser Name : %s'%(self.u_details[0],
                                                                                                      address,self.u_details[2],
                                                                                                      self.u_details[3]),justify=tk.LEFT)
            name.pack()
    '''LOGIN '''
    def login(self,user):
        try:
            self.frame.destroy()
        except:pass
        finally:
            self.window.config(bg='#ffcccc')
            self.blank_frame=tk.Frame(self.window,bg='#ffcccc',width=self.screen_width//2,height=(self.screen_height//4))
            self.blank_frame.pack()
            self.details=tk.Frame(self.window,bg='#ffffff',width=self.screen_width//4,height=self.screen_height//2,bd=0,
                                  highlightcolor='#cccccc',highlightbackground='#aaaaff',highlightthickness=4,relief='groove')
            self.details.pack()
            label1=tk.Label(self.details,text='Enter Your Details',font=('caliblri',20,'italic'))
            label1.pack()
            blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
            blank_button.pack()
            if(user=='user' or user=='admin'):
                frame1=tk.Frame(self.details)
                frame1.pack()
                username=tk.Label(frame1,text='User Name',font=('times',16))
                username.pack(side=tk.LEFT)
                u_name=tk.Entry(frame1,width=50,font=('times',10))
                u_name.pack(side=tk.LEFT)
                blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
                blank_button.pack()
                frame2=tk.Frame(self.details)
                frame2.pack()
                password=tk.Label(frame2,text='Password',font=('times',16))
                password.pack(side=tk.LEFT)
                u_password=tk.Entry(frame2,width=50,font=('times',10),show='*')
                u_password.pack(side=tk.LEFT)
                self.c=0
                show=tk.Button(frame2,text='Show Password',command=lambda:password_visibility(),relief='flat')
                show.pack()
                blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
                blank_button.pack()
                '''to hide or show password'''
                def password_visibility():
                    if self.c%2==0:
                        u_password.config(show='')
                        show.config(text='Hide Password')
                        self.c+=1
                    else:
                        u_password.config(show='*')
                        show.config(text='Show Password')
                        self.c+=1
                frame3=tk.Frame(self.details,width=self.details.winfo_width(),height=self.details.winfo_height())
                frame3.pack(side=tk.BOTTOM)
                _login=tk.Button(frame3,text='Log in',bg='#ffcccc',fg='black',width=20,height=2)
                if(user=='user'):
                    _login.config(command=lambda:obj.verify('login',u_name.get(),u_password.get(),'user'))
                else:
                    _login.config(command=lambda:obj.verify('login','admin',u_password.get(),'ad'))
                _login.pack(side=tk.LEFT)
                quit_=tk.Button(frame3,text='Quit',bg='#ffcccc',fg='black',width=20,height=2,
                                command=lambda:obj.homepage(self.details,self.blank_frame))
                quit_.pack(side=tk.RIGHT)
            else:
                frame1=tk.Frame(self.details)
                frame1.pack()
                username=tk.Label(frame1,text='User Name',font=('times',16))
                username.pack(side=tk.LEFT)
                u_name=tk.Entry(frame1,width=50,font=('times',10))
                u_name.pack(side=tk.LEFT)
                blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
                blank_button.pack()
                frame6=tk.Frame(self.details)
                frame6.pack()
                name=tk.Label(frame6,text='Name',font=('times',16))
                name.pack(side=tk.LEFT)
                _name=tk.Entry(frame6,width=50,font=('times',10))
                _name.pack(side=tk.LEFT)
                blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
                blank_button.pack()
                frame2=tk.Frame(self.details)
                frame2.pack()
                password=tk.Label(frame2,text='Password',font=('times',16))
                password.pack(side=tk.LEFT)
                u_password=tk.Entry(frame2,width=50,font=('times',10))
                u_password.pack(side=tk.LEFT) 
                self.c=0#counter to decise show or hide password
                show=tk.Button(frame2,text='Show Password',command=lambda:password_visibility(),relief='flat')
                show.pack()
                blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
                blank_button.pack()
                '''to hide or show password'''
                def password_visibility():
                    if self.c%2==0:
                        u_password.config(show='')
                        show.config(text='Hide Password')
                        self.c+=1
                    else:
                        u_password.config(show='*')
                        show.config(text='Show Password')
                        self.c+=1
                blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
                blank_button.pack()
                frame4=tk.Frame(self.details)
                frame4.pack()
                address=tk.Label(frame4,text='House no',font=('times',16))
                address.pack(side=tk.LEFT)
                house_no=tk.Entry(frame4,width=50,font=('times',10))
                house_no.pack(side=tk.LEFT)
                frame7=tk.Frame(self.details)
                frame7.pack()
                address=tk.Label(frame7,text='Area',font=('times',16))
                address.pack(side=tk.LEFT)
                area=tk.Entry(frame7,width=50,font=('times',10))
                area.pack(side=tk.LEFT)
                frame8=tk.Frame(self.details)
                frame8.pack()
                address=tk.Label(frame8,text='City',font=('times',16))
                address.pack(side=tk.LEFT)
                city=tk.Entry(frame8,width=50,font=('times',10))
                city.pack(side=tk.LEFT)
                frame9=tk.Frame(self.details)
                frame9.pack()
                address=tk.Label(frame9,text='*Landmark',font=('times',16))
                address.pack(side=tk.LEFT)
                landmark=tk.Entry(frame9,width=50,font=('times',10))
                landmark.pack(side=tk.LEFT)
                blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
                blank_button.pack()
                frame5=tk.Frame(self.details)
                frame5.pack()
                contact=tk.Label(frame5,text='Contact number',font=('times',16))
                contact.pack(side=tk.LEFT)
                u_contact=tk.Entry(frame5,width=50,font=('times',10))
                u_contact.pack(side=tk.LEFT)
                blank_button=tk.Button(self.details,bg='#ffffff',height=1,state='disabled',bd=0)
                blank_button.pack()
                frame3=tk.Frame(self.details,width=self.details.winfo_width(),height=self.details.winfo_height())
                frame3.pack(side=tk.BOTTOM)
                _signin=tk.Button(frame3,text='Sign in',bg='#ffcccc',fg='black',width=20,height=2)
                _signin.config(command=lambda:obj.verify('signin',_name.get(),u_password.get(),
                                                         obj.get_address(house_no.get(),area.get(),city.get(),landmark.get())
                                                         ,u_contact.get(),u_name.get()))
                _signin.pack(side=tk.LEFT)
                
                quit_=tk.Button(frame3,text='Quit',bg='#ffcccc',fg='black',width=20,height=2,
                                command=lambda:obj.homepage(self.blank_frame,self.details))
                quit_.pack(side=tk.RIGHT)
    '''TO RETURN ADDRESS AS DICTIONARY'''
    def get_address(self,h,a,c,l):
        u_address=dict()
        u_address['house_no']=h
        u_address['area']=a
        u_address['city']=c
        u_address['landmark']=l
        return u_address
    def run(self):
        obj.create_window()
        obj.homepage()
        self.window.mainloop()
obj=hospital()
obj.run()

        
