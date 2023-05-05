from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIME_TRACK = 1
looper = True

# ---------------------------- TIMER RESET ------------------------------- # 
def resetter():
    global looper
    global TIME_TRACK
    TIME_TRACK = 1
    label_work_break.config(text="Resetted")
    label_checkmarks.config(text="")
    new_window.after_cancel(looper)
    canvas.itemconfig(text_id, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def counting_checkmarks(local_tracker):
    if local_tracker ==1:
        label_checkmarks.config(text="✓")
    elif local_tracker ==3:
        label_checkmarks.config(text="✓"*2)
    elif local_tracker ==5:
        label_checkmarks.config(text="✓"*3) 

def start_timer():
    global TIME_TRACK
    if TIME_TRACK <= 6:
        if TIME_TRACK % 2 != 0:
            label_work_break.config(text="Work!")
            countdown(WORK_MIN)
            counting_checkmarks(TIME_TRACK)
        elif TIME_TRACK % 2 ==0:
            label_work_break.config(text="Break")
            if TIME_TRACK == 6:
                countdown(LONG_BREAK_MIN)
            else:
                countdown(SHORT_BREAK_MIN)
        # print("time track: ", TIME_TRACK)
        TIME_TRACK +=1
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time_):
    global looper

    mins, secs = divmod(time_, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    canvas.itemconfig(text_id, text=timer)
    if time_>0:
        looper = new_window.after(100,countdown, time_ - 1)
    else:
        start_timer()
    # print("time_: ", time_)
  
    
# ✓
# ---------------------------- UI SETUP ------------------------------- #

new_window = Tk()
new_window.config(padx=50,pady=20)
new_window.title("POMODORO - be more productive!")
new_window.config(bg = YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file=".\\tomato.png")
canvas.create_image(103, 100, image = img)
canvas.grid(row=5, column=2)

text_id = canvas.create_text(103,135,text="00:00", fill="white",font=(FONT_NAME,24,"bold"))


label_work_break = Label(text="",font=(FONT_NAME,24, "bold"), bg=YELLOW, fg=GREEN)
label_work_break.grid(row = 3, column=2)

label_checkmarks = Label(text="", font=(FONT_NAME,20,"bold"), bg=YELLOW, fg=GREEN)
label_checkmarks.grid(row=8,column=2)

button_start = Button(text = "Start", command=start_timer)
button_start.grid(row=7, column=1)


button_reset = Button(text="Reset", command=resetter)
button_reset.grid(row=7, column=3)




new_window.mainloop()
