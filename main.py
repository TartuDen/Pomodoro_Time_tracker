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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

new_window = Tk()
new_window.config(padx=50,pady=20)
new_window.title("POMODORO - be more productive!")
new_window.config(bg = "lightblue")

canvas = Canvas(width=200, height=224)
img = PhotoImage(file=".\\tomato.png")
canvas.create_image(103, 112, image = img)
canvas.grid(row=5, column=2)





label_work_break = Label(text="Work",font=(FONT_NAME,24))
label_work_break.grid(row = 3, column=2)

label_counter = Label(text="counter")
label_counter.grid(row=5, column=2)

button_start = Button(text = "Start")
button_start.grid(row=7, column=1)


button_reset = Button(text="Reset")
button_reset.grid(row=7, column=3)


label_checkmarks = Label(text="Checkmarks")
label_checkmarks.grid(row=8,column=2)







new_window.mainloop()
