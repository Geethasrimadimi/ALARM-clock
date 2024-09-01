# importing the required modules
from tkinter import *
import datetime as dt
import time
import winsound as ws


# defining the function for the alarm clock
def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        currentDate = actualTime.strftime("%d / %m / %Y")
        the_message = "Current Time: " + str(currentTime)
        print(the_message)
        if currentTime == setAlarmTimer:
            ws.PlaySound(r"C:\Users\91912\OneDrive\Desktop\CodeClause\Task-2 Alarm Clock Using GUI\sound.wav",
                         ws.SND_ASYNC)
            break


def getAlarmTime():
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"
    alarm(alarmSetTime)


# creating the GUI for the application
guiWindow = Tk()
guiWindow.title("The Alarm Clock")
guiWindow.geometry("464x200")
guiWindow.config(bg="skyblue")
guiWindow.resizable(width=False, height=False)

timeFormat = Label(
    guiWindow,
    text="Remember to set time in 24-hour format!",
    fg="Black",
    bg="white",
    font=("Arial", 13, "bold")
).place(
    x=0,
    y=160
)

add_time = Label(
    guiWindow,
    text="Hour     Minute     Second",
    font=60,
    fg="Black",
    bg="White"
).place(
    x=220,
    y=10
)

setAlarm = Label(
    guiWindow,
    text="Set Time for Alarm: ",
    fg="Black",
    font=("Helevetica", 13, "bold")
).place(
    x=5,
    y=50
)

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(
    guiWindow,
    textvariable=hour,
    bg="White",
    width=4,
    font=(20)
).place(
    x=220,
    y=53
)
minuteTime = Entry(
    guiWindow,
    textvariable=minute,
    bg="White",
    width=4,
    font=(20)
).place(
    x=297,
    y=53
)
secondTime = Entry(
    guiWindow,
    textvariable=second,
    bg="White",
    width=4,
    font=(20)
).place(
    x=390,
    y=53
)

submit = Button(
    guiWindow,
    text="Set The Alarm",
    fg="white",
    bg="Blue",
    width=15,
    command=getAlarmTime,
    font=(20)
).place(
    x=140,
    y=100
)

guiWindow.mainloop()