import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import StringVar, messagebox, filedialog
from ttkthemes import ThemedStyle
from cryptography.fernet import Fernet
import time
import datetime as tm

app = tk.Tk()
app.geometry("300x250")
app.title("Emergencounter")
# Setting Theme
style = ThemedStyle(app)
style.set_theme("arc")
key = Fernet.generate_key()

# Global Variables
is_paused = False
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tabs
tabControl = ttk.Notebook(app)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
# tab3 = ttk.Frame(tabControl)
# tab4 = ttk.Frame(tabControl)
# tab5 = ttk.Frame(tabControl)


tabControl.add(tab1, text='ألعداد')
tabControl.add(tab2, text='ألمهام')
# tabControl.add(tab3, text='ألاعدادات')
# tabControl.add(tab4, text='السيرفرات')
# tabControl.add(tab5, text='الملفات')


tabControl.pack(expand=1, fill="both")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


day= StringVar()
hour= StringVar()
minute= StringVar()
second= StringVar()

day.set("00")
hour.set("00")
minute.set("00")
second.set("00")

DayEntry= ttk.Entry(tab1, width=3, font=("Arial",18,""), textvariable=day)
DayEntry.place(x=30,y=30)
DayLabel = ttk.Label(tab1, text=("ألايام"), font=("Arial",10,"bold"))
DayLabel.place(x=30, y=70)

hourEntry= ttk.Entry(tab1, width=3, font=("Arial",18,""), textvariable=hour)
hourEntry.place(x=85,y=30)
HourLabel = ttk.Label(tab1, text=("الساعات"), font=("Arial",10,"bold"))
HourLabel.place(x=85, y=70)
  
minuteEntry= ttk.Entry(tab1, width=3, font=("Arial",18,""), textvariable=minute)
minuteEntry.place(x=140,y=30)
MinuteLabel = ttk.Label(tab1, text=("الدقاىْق"), font=("Arial",10,"bold"))
MinuteLabel.place(x=140, y=70)

secondEntry= ttk.Entry(tab1, width=3, font=("Arial",18,""), textvariable=second)
secondEntry.place(x=195,y=30)
SecondsLabel = ttk.Label(tab1, text=("الثواني"), font=("Arial",10,"bold"))
SecondsLabel.place(x=195, y=70)

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        starttime = time.time()
        inputtedfile = int(day.get())*86400 + int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        temp = inputtedfile
    except:
        print("Please input the right value")
    pausetime = None
    while temp >= -1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
        days=0
        if hours >24:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            days, hours = divmod(hours, 24)
        # using format () method to store the value up to
        # two decimal places
        day.set("{0:2d}".format(days))
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        if not is_paused:
            if pausetime is not None:
                starttime += time.time() - pausetime
                pausetime = None
            tab1.update()
          
            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp <= 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
                
            # after every one sec the value of temp will be decremented
            # by one
            temp = int(inputtedfile - (time.time() - starttime))
        else:
            tab1.update()
            if pausetime is None:
                pausetime = time.time()




def toggle_pause():
    global is_paused
    if is_paused == False:
        is_paused = True
    else:
        is_paused = False

# button widget
btn = ttk.Button(tab1, text = 'Start',
                          command = submit)
btn.place(x = 80,y = 120)

btn = ttk.Button(tab1, text = 'Pause',
                          command = toggle_pause)
btn.place(x = 80,y = 160)

  
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
app.mainloop()


no_list = [22,68,90,78,90,88]

def average(x):
    Sum = sum(no_list)
    Items = len(no_list)
    Sum / Items

    
print(average(no_list))