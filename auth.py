import os
import sys
from customtkinter import *
from PIL import Image


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class AuthWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Вхід")
        self.resizable(True, False)
        self.name = ""
        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side="left", fill="both")
        img_ctk = CTkImage(light_image=Image.open(resource_path("bg.png")), size=(450, 400))
        self.img_label = CTkLabel(self.left_frame, text="Welcome", image=img_ctk, font=("Helvetica", 50, "bold"))
        self.img_label.pack()
        self.right_frame = CTkFrame(self)
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side="right", fill="both", expand="True")
        CTkLabel(self.right_frame, text="LogiTalk").pack(pady=60)
        self.name_entry = CTkEntry(self.right_frame, placeholder_text="☻ ім`я")
        self.name_entry.pack(fill="x", padx=10, pady=10)
        self.connect_button = CTkButton(self.right_frame, text="УВІЙТИ", command=self.open_messenger)
        self.connect_button.pack(fill="x", padx=10, pady=5)

    def open_messenger(self):
        self.name = self.name_entry.get()
        self.destroy()

main_win = AuthWindow()
main_win.mainloop()

