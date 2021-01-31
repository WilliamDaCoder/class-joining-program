import os
import webbrowser
import datetime
import time
import json
import tkinter as tk
import subprocess
homedir = os.path.dirname(os.path.realpath(__file__))
OFL_File = homedir+"\\OpenLocation.bat"
root = tk.Tk()
root.title("meeting.py")
frame = tk.Frame(root)
frame.pack()


def open_ofl():
    subprocess.call(OFL_File)


def settings():
    def cfu():
        webbrowser.open("https://github.com/WilliamDaCoder/semi-auto-class-joining-program")
    root = tk.Tk()
    root.title("Settings")
    frame = tk.Frame(root)
    frame.pack()
    exit_settings = tk.Button(frame,
                        text="🚪",
                        fg="red",
                        command=root.destroy)
    exit_settings.pack(side=tk.LEFT)

    ofl = tk.Button(frame,
                    text="📂",
                    fg="blue",
                    command=open_ofl)
    ofl.pack(side=tk.LEFT)

    update = tk.Button(frame,
                       text="check for updates",
                       fg="blue",
                       command=cfu)
    update.pack(side=tk.LEFT)


def run():
    root.destroy()


weekend = tk.Button(frame,
                    text="weekend",
                    fg="red",
                    command=quit)


weekday = tk.Button(frame,
                    text="weekday",
                    fg="green",
                    command=run)


settings_button = tk.Button(frame,
                text="⚙",
                fg="blue",
                command=settings)

exit_button = tk.Button(frame,
                        text="🚪",
                        fg="red",
                        command=quit)
exit_button.pack(side=tk.LEFT)
weekend.pack(side=tk.LEFT)
settings_button.pack(side=tk.RIGHT)
weekday.pack(side=tk.RIGHT)
exit_button.pack(side=tk.RIGHT)
root.mainloop()

file = homedir+"\\Meeting.json"
url="put url here"
while True:
    time.sleep(1)
    with open(file) as f:
        MeetingsFile = json.load(f)
        Meetings = MeetingsFile["Meetings"]
    now = datetime.datetime.now()
    current_day = now.strftime("%A")
    current_time = now.strftime("%I:%M %p")
    for meeting in Meetings:
        if current_time == meeting:
            def join_class():
                webbrowser.open(url)
                root.destroy()
            root = tk.Tk()
            root.title("class found")
            frame = tk.Frame(root)
            frame.pack()

            join_call = tk.Button(frame,
                                  text="join "+current_time+" call",
                                  fg="green",
                                  command=join_class)

            no_class_now = tk.Button(frame,
                                     text="There is no "+current_time+" call")
            Quit = tk.Button(frame,
                             text="🚪",
                             fg="red",
                             command=quit)
            Quit.pack(side=tk.RIGHT)
            join_call.pack(side=tk.LEFT)
            root.mainloop()
            time.sleep(65)
