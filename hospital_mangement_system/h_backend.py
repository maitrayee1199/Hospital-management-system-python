import tkinter as tk
import datetime
class h_backend:
    def __init__(self):
        #dictionary contains username as key and password as value
        self.u_password={'admin':'admin@123','maitrayee':'hello_maitrayee','samar':'hello_samar'}
        #dictionary users username as key to staore user details
        self.user_details={'maitrayee':['maitrayee',{'house_no':'e 3198','area':'rjpm','city':'lucknow','landmark':'near mini stadium'}
                                        ,'1234567890','maitrayee'],
                           'samar':['samar puri',{'house_no':'abc building flat no.123','area':'mud island','city':'mumbai','landmark':''}
                                    ,'9987654322','samar']}
        #ambulances available with distance as key
        self.ambulance_available=dict()
        self.ambulance_available={1:{'distance':1,'available':1},2:{'distance':2,'available':3},4:{'distance':5,'available':2}}
        #ambulances available and their details with distance as key
        self.ambulance_details=dict()
        self.ambulance_details[1]=[{'ambulance_id':'dis1id1','ambulance_no':'UP 32 AS 5467','driver_contact':'7654321890','cost':'Rs 100'}]
        self.ambulance_details[2]=[{'ambulance_id':'dis2id1','ambulance_no':'UP 32 AS 5462','driver_contact':'7254321890','cost':'Rs 200'},
                           {'ambulance_id':'dis2id2','ambulance_no':'UP 32 AS 5362','driver_contact':'7253321890','cost':'Rs 200'},
                           {'ambulance_id':'dis2id3','ambulance_no':'UP 32 AS 5262','driver_contact':'7253321892','cost':'Rs 200'}]
        self.ambulance_details[4]=[{'ambulance_id':'dis4id1','ambulance_no':'UP 32 AS 5462','driver_contact':'7254321890','cost':'Rs 400'},
                           {'ambulance_id':'dis4id2','ambulance_no':'UP 32 AS 5662','driver_contact':'7256321890','cost':'Rs 400'}]
        #dictionary wth doctordetails and category as key
        self.doctor_details={'heart':{'id':'heart001','name':'Jay Kumar','education':'MBBS,MD','cabin':'floor 1 room no 302',
                                      'app':{str(datetime.date(2019,10,31)):'1'},'fees':'Rs.1500','type':'heart','time':'9:00 a.m'},
                             'dentist':{'id':'dentist001','name':'Ashok Sehgal','education':'MDes','cabin':'floor 1 room no 303',
                                        'app':{str(datetime.date(2019,10,31)):'1'},'fees':'Rs.800','type':'dentist','time':'12:00 p.m'},
                             'gen':{'id':'gen001','name':'Bhuvan Bam','education':'MD','cabin':'floor 1 room no 303',
                                    'app':{str(datetime.date(2019,10,31)):'1'},'fees':'RS.600','type':'gen','time':'3:00 p.m'}}
        #stores booking details with username as key
        self.user_bookings={'maitrayee':{'ambulance':['13-11-2019\ndis1id1']},
                            'samar':{'ambulance':['31-10-2019\ndis1id1'],'doctor':['13-11-2019\nheart001']}}
    '''UPDATE Doctor DETAILS'''
    def update_doc_details(self,det,d):#,username,user_det):
        a=self.doctor_details.items()
        #search for value's key in key value pair in 'a'
        for i in a:
            if(i[1]==det):
                try:
                    self.doctor_details[i[0]]['app'][d]=str(int(self.doctor_details[i[0]]['app'][d])+1)
                except:
                    self.doctor_details[i[0]]['app'][d]=1
    '''UPDATE USER BOOKINGS'''
    def update_user_bookings(self,username,type_,booking_details):
        try:
            a=self.user_bookings[username]#if user has previous booking
            if type_=='doctor':
                try:
                    p=a['doctor']
                    if booking_details in p:
                        self.prompt('booking already exists')
                        return 0
                    else:
                        p.append(booking_details)
                        return 1    
                except KeyError:
                    self.user_bookings[username][type_]=[booking_details]
                    return 1
            elif type_=='ambulance':
                try:
                    p=a['ambulance']
                    for i in p:
                        if booking_details[0:8] in i[0:8]:
                            self.prompt('booking already exists ')
                            return 0
                    else:
                        p.append(booking_details)
                        return 1
                except KeyError:
                    self.user_bookings[username][type_]=[booking_details]
                    return 1
        except KeyError:
            self.user_bookings[username]=dict()
            #if it's user's 1st booking
            self.user_bookings[username][type_]=list(booking_details)
    '''GET ADMIN RIGHTS'''
    def admin_rights(self):
        book_keys=self.user_bookings.keys()
        user_keys=self.u_password.keys()
        s=''
        for i in book_keys:
            s+='\n\n====='+i+'=====\n'
            for j in self.user_bookings[i]:
                s+=str(j)+'  '+str(self.user_bookings[i][j])+'\n\n'
        for i in user_keys:
            if i=='admin':
                continue
            s+='\n\n====='+i+'=====\n'
            try:
                #not to get key error when key is 'admin'
                for j in self.user_details[i]:
                    s+=str(j)+'\n'
            except:pass
        for i in self.ambulance_available.keys():
            s+='\n\n====='+str(i)+'=====\n'
            for j in self.ambulance_details[i]:
                s+=str(j)+'\n'
        for i in self.doctor_details.keys():
            s+='\n\n====='+i+'=====\n'
            for j in self.doctor_details[i]:
                s+=str(j)+' '+str(self.doctor_details[i][j])+'\n'
        return s
    '''GET DOCTOR DETAILS'''
    def getapp_details(self,doc,*date):
        doctor=self.doctor_details[doc]
        return doctor
    '''GET USER DETAILS'''
    def get_details(self,username):
        return self.user_details[username]
    '''LOAD AMBULANCE DETAILS'''
    def load_ambulance_details(self,distance):
        if distance=='':
            self.prompt('Please enter distance')
            return
        else:
            distance=int(distance)
        try:
            if distance>400 or distance<1:
                return self.prompt('please enter distance between 1 to 400 KM')
            #get no of ambulances available
            available=self.ambulance_available[distance]['available']
            if (available==0):
                return self.prompt("Sorry!! no ambulance is available")
            #get details of the ambulance at index available-1
            detail=self.ambulance_details[distance][available-1]
            return detail
        except KeyError:
            #if ambulance for entered distance is not available
            return self.prompt("Sorry!! no ambulance is available")
    '''UPDATE AMBULANCE DETAILS'''
    def update_ambulance_details(self,distance):
        #update number of ambulances availabble
        self.ambulance_available[distance]['available']=self.ambulance_available[distance]['available']-1
        return
    '''UPDATE DETAILS'''
    def update_details(self,*args):
        #setting username as key and password as value
        self.u_password[args[4]]=args[1]
        #storing user detsils with usernmae as key
        self.user_details[args[4]]=[args[0],args[2],args[3],args[4]]
    def prompt(message):
        p=tk.Tk()
        p.config(bg='black')
        p.title('Warning')
        label=tk.Label(p,text=message,font=('times',20,'bold'),fg='red',bg='#aaffaa')
        s=str(label.winfo_height()+40)
        s=str(label.winfo_width()+100)+'x'+str(label.winfo_height()+100)
        p.geometry('+%d+%d'%(400,300))
        label.pack()
        ok=tk.Button(p,text='OK',bg='black',fg='white',command=lambda:p.destroy())
        ok.pack()
    prompt=staticmethod(prompt)
    '''CHECK IF PASSWORD IS CORRECT'''
    def check_password(self,user,password,type_='none'):
        #if user tries to login as admin'''
        if user=='admin' and type_!=('ad'):
            self.prompt('username cannot be admin')
            return 0
        '''admin login'''
        if user=='admin' and type_=='ad':
            if password==self.u_password['admin']:
                self.prompt("admin verified")
                return 1
            else:   
                self.prompt('incorrect password')    
        else:#user login
            try:
                if  self.u_password[user]==password and type_=='user':
                    self.prompt("verified")
                    return 1
                else:
                    self.prompt('incorrect password')
            except:
                self.prompt('incorrect username')
    '''NEW USER SIGNIN'''
    def signin(self,name,password,address,contact,username):
        a=all(x.isalpha() or x.isspace() for x in name)
        if name=='' or a==False:
            self.prompt('invalid name')
        elif name=='' or (username in self.u_password.keys())==True:
            self.prompt('This username is not available choose another one')
        elif password=='':
            self.prompt('password field cannot be empty')
        elif address['house_no']=='' or address['area']=='' or address['city']=='':
            self.prompt('please fill complete address')
        elif contact=='' or contact.isdigit()==False or len(contact)!=10:
            self.prompt('invalid contact')
        else:
            self.update_details(name,password,address,contact,username)
            return 1
            
    
