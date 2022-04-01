from tkinter import *


class My_Button(Button):

    def __init__(self, root, text, command, *args, **kwargs):
        button_font = ("Helvetica", 13,)
        button_background = "#e56b6f"
        button_text_colour = "#1d3557"
        self.root = root
        self.text = text
        self.font = button_font
        self.command = command
        super().__init__()
        self["text"] = self.text
        self["command"] = self.command
        self["bg"] = button_background
        self["fg"] = button_text_colour
        self["activebackground"] = "#e9c46a"
        self["width"] = 20
        self["font"] = button_font

