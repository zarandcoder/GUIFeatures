#! /home/vadim/PycharmProjects/GUIFeatures/venv/bin/python3.7

import tkinter as tk


title_of_gui = 'GUI of Vadim'
custom_text = 'Hi beautiful world'


class Root(tk.Tk):

    def __init__(self):
        super().__init__()
        self.wm_title(title_of_gui)
        self.label = tk.Label(self, text=custom_text, padx=250, pady=250)
        self.label.pack()

"""
if __name__ == '__main__':
    win = Root()
    win.resizable = True
    win.mainloop()
"""