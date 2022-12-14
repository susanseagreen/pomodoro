from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_TIMER = 5
# SHORT_BREAK_TIMER = 5
# LONG_BREAK_TIMER = 5
WORK_TIMER = 25 * 60
SHORT_BREAK_TIMER = 5 * 60
LONG_BREAK_TIMER = 20 * 60
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    show_start_hide_reset()
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def show_reset_hide_start():
    start_btn.grid_forget()
    reset_btn.config(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
    reset_btn.grid(column=1, row=2)


def show_start_hide_reset():
    reset_btn.grid_forget()
    start_btn.config(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
    start_btn.grid(column=1, row=2)


def start_timer():
    global reps
    if reps == 0:
        show_reset_hide_start()
    reps += 1
    window.lift()
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)
    if reps <= 8:
        if reps % 8 == 0:
            count_down(LONG_BREAK_TIMER)
            title_label.config(text="BREAK", fg=RED)
        elif reps % 2 == 0:
            count_down(SHORT_BREAK_TIMER)
            title_label.config(text="BREAK", fg=PINK)
        else:
            count_down(WORK_TIMER)
            title_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = count // 60
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            mark += "???"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=10, bg=YELLOW)

title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=240, height=260, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(120, 120, image=tomato_img)
timer_text = canvas.create_text(113, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=1, row=2)

reset_btn = Button(text="")
reset_btn.grid_forget()

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))

check_marks.grid(column=1, row=3,)

window.mainloop()
