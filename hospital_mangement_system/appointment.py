from tkcalendar import Calendar,DateEntry
import time
import tkinter as tk
from tkinter import ttk
import datetime
class appointment:
    def __init__(self):
        pass


    def get_calendar(self):
            print('in get_calendar app')
            window=tk.Tk()
            cal=Calendar(window)
            year=time.localtime(time.time())[0]
            month=time.localtime(time.time())[1]
            date=time.localtime(time.time())[2]
            
            if month==12:
                cal.config(mindate=datetime.date(year,month,date),maxdate=datetime.date(year,1,date))
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

            select_button=tk.Button(cal,text='Select Date',command=lambda:print(cal.selection_get()))
            select_button.pack()
            cal.mainloop()
