import tkinter as tk;
from tkinter import ttk;

NORM_FONT = ("Verdana", 10);

class PopUp(object):

    def alert(self, msg):
        popup = tk.Tk();
        popup.wm_title("!");
        label = ttk.Label(popup, text=msg, font=NORM_FONT);
        label.pack(side="top", fill="x", pady=10);
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy);
        B1.pack();
        popup.mainloop();
