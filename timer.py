import time
import winsound
import tkinter as tk
from tkinter import messagebox

def countdown(t, alert_intervals=None, custom_message=None):
    root = tk.Tk()
    root.title("Countdown Timer")

    label = tk.Label(root, font=('Helvetica', 48), text="")
    label.pack(pady=60)

    def update_label():
        nonlocal t
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        root.update()

        if alert_intervals and t in alert_intervals:
            winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 milliseconds

        time.sleep(1)
        t -= 1

        if t >= 0:
            root.after(1000, update_label)
        else:
            label.config(text=custom_message)
            root.update()
           # if custom_message:
           #     messagebox.showinfo("Custom Message", custom_message)

    update_label()

    root.mainloop()

# Input time in seconds
t = int(input("Enter the time in seconds: "))

# Input alert intervals (comma-separated) and custom message
alert_intervals_str = input("Enter alert intervals (comma-separated, e.g., 30,10): ")
alert_intervals = list(map(int, alert_intervals_str.split(',')))

custom_message = input("Enter a custom message (press Enter for none): ")

# Function call with add-ons
countdown(t, alert_intervals, custom_message)
