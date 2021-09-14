from tkinter import * 
from tkinter import messagebox, DISABLED
from PIL import ImageTk as ptk, Image as pim
# import PIL

from dir import __defs as defs

# global attack_image, buttons


class App(object):
    def __init__(self):
        img = pim.open("assets/tinderfire.png")
        img.thumbnail((100,100), pim.ANTIALIAS)
        self.i = ptk.PhotoImage(img)
        self.l = Label(main_ui, image=self.i).pack()
        self.b = Button(main_ui, text="run",command=self.pre_attack_command)
        self.b.pack(padx=80)

    def pre_attack_command(self):
        self.b['state'] = DISABLED
        defs.pre_attack()
        self.login_time()

    def login_time(self):
        self.loginpopup = tk.Toplevel()
        label = tk.Label(self.loginpopup, image=self.i, text="Log in to Tinder. When you are succesfully logged in, click 'Done'")
        label.pack(fill='x', padx=50, pady=5)
        button_close = tk.Button(self.loginpopup, text="Done", command=self.login_successful)
        button_close.pack(fill='x')
    
    def login_successful(self):
        self.loginpopup.destroy()



main_ui = Tk()
main_ui.title("Tinder attack")
a = App()
main_ui.mainloop()