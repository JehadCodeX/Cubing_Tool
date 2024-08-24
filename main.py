from tkinter import *
import random
import time

moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]

def update_time():
    if running:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time % 1) * 100)
        time_string = f"{minutes:02}:{seconds:02}:{milliseconds:02}"
        timer_label.config(text=time_string)
        window.after(10, update_time)

def toggle_stopwatch(event=None):
    global start_time, running
    if running:
        running = False
    else:
        start_time = time.time() - (elapsed_time if elapsed_time else 0)
        running = True
        update_time()

def reset_stopwatch(event=None):
    global running, elapsed_time
    running = False
    elapsed_time = 0
    timer_label.config(text="00:00:00")

def generate_random_moves():
    random_moves = [random.choice(moves) for _ in range(21)]
    return '  '.join(random_moves)

def update_label():
    display_move_label.config(text=generate_random_moves())

def color_light():
    window.config(bg="white")
    timer_label.config(fg="black", bg="white")
    generate_button.config(bg="lightgray", fg="black", activebackground="gray", activeforeground="black")
    display_move_label.config(fg="black", bg="white")

def color_dark():
    window.config(bg="#1e1e1e")
    timer_label.config(fg="#b0b0b0", bg="#1e1e1e")
    generate_button.config(bg="#333333", fg="#b0b0b0", activebackground="#444444", activeforeground="#b0b0b0")
    display_move_label.config(fg="#b0b0b0", bg="#1e1e1e")

def color_purple():
    window.config(bg="#3b0a45")
    timer_label.config(fg="#dcdcdc", bg="#3b0a45")
    generate_button.config(bg="#6a0d91", fg="#dcdcdc", activebackground="#7b2d9b", activeforeground="#dcdcdc")
    display_move_label.config(fg="#dcdcdc", bg="#3b0a45")

def color_green():
    window.config(bg="#004d40")
    timer_label.config(fg="#e0f2f1", bg="#004d40")
    generate_button.config(bg="#00796b", fg="#e0f2f1", activebackground="#009688", activeforeground="#e0f2f1")
    display_move_label.config(fg="#e0f2f1", bg="#004d40")

window = Tk()

start_time = 0
running = False
elapsed_time = 0

window.bind("<space>", toggle_stopwatch)
window.bind("<r>", reset_stopwatch)

menu = Menu(window)
window.config(menu=menu)

window.title("Cube Move Generator")
window.geometry("500x300")

generate_button = Button(window, text="Generate Moves", command=update_label, width=20, height=2, font=("Arial", 12))
generate_button.pack(pady=10)

display_move_label = Label(window, text="", font=("Arial", 10))
display_move_label.pack(pady=10)

timer_label = Label(text="00:00:00", font=("Arial", 20))
timer_label.pack(pady=20)

theme_menu = Menu(menu, tearoff=0)
theme_menu.add_command(label="Light", command=color_light)
theme_menu.add_command(label="Dark", command=color_dark)
theme_menu.add_command(label="Purple", command=color_purple)
theme_menu.add_command(label="Green", command=color_green)
menu.add_cascade(label="Themes", menu=theme_menu)

window.mainloop()
