import tkinter as tk
import tkinter.font as tkFont
import pyautogui
from tkinter import *

from tkinter import messagebox

class App:
    GLineEdit_73 = None
    GLineEdit_298 = None

    def __init__(self, root):
        self.GLineEdit_73 = tk.Entry(root)
        self.GLineEdit_298 = tk.Entry(root)
        #setting title
        root.title("undefined")
        #setting window size
        width=508
        height=370
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_597=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_597["font"] = ft
        GLabel_597["fg"] = "#333333"
        GLabel_597["justify"] = "center"
        GLabel_597["text"] = "Kullanıcı Girişi"
        GLabel_597.place(x=160,y=40,width=225,height=30)

        GButton_566=tk.Button(root)
        GButton_566["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_566["font"] = ft
        GButton_566["fg"] = "#000000"
        GButton_566["justify"] = "center"
        GButton_566["text"] = "Giriş"
        GButton_566.place(x=170,y=210,width=156,height=35)
        GButton_566["command"] = self.GButton_566_command



        GLabel_879=tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_879["font"] = ft
        GLabel_879["fg"] = "#333333"
        GLabel_879["justify"] = "center"
        GLabel_879["text"] = "Kullanıcı Adı"
        GLabel_879.place(x=150, y=100, width=70,
                         height=25)

        GLabel_283=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_283["font"] = ft
        GLabel_283["fg"] = "#333333"
        GLabel_283["justify"] = "center"
        GLabel_283["text"] = "Şifre"
        GLabel_283.place(x=150, y=150,
                         width=70, height=25)


        self.GLineEdit_298["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_298["font"] = ft
        self.GLineEdit_298["fg"] = "#333333"
        self.GLineEdit_298["justify"] = "center"
        self.GLineEdit_298["text"] = "Entry"
        self.GLineEdit_298.place(x=240, y=150,
                                 width=107, height=30)
        self.GLineEdit_298["show"] = "*"


        self.GLineEdit_73["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_73["font"] = ft
        self.GLineEdit_73["fg"] = "#333333"
        self.GLineEdit_73["justify"] = "center"
        self.GLineEdit_73["text"] = "Entry2"
        self.GLineEdit_73.place(x=240, y=90,
                           width=109, height=30)

    def GButton_566_command(self):
        kadi = self.GLineEdit_73.get()
        sifre = self.GLineEdit_298.get()
        print(kadi, sifre)
        if kadi == "a" and sifre == "a":
            root2 = tk.Tk()
            root.title("undefined")
            # setting window size
            width = 200
            height = 200
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root2.geometry(alignstr)
            root2.resizable(width=False, height=False)
            root.destroy()
        else:
            tk.messagebox.showerror(title="Hata",
                                         message="Yanlış hemşerim")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()









    pyautogui.moveTo(500, 500, duration=2,
                 tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(1000, 1000, duration=2,
                 tween=pyautogui.easeInCirc)
pyautogui.moveTo(50, 50, duration=2,
                 tween=pyautogui.easeInBounce)
pyautogui.moveTo(500, 500, duration=2,
                 tween=pyautogui.easeOutElastic)




                 # Ekran Çözünürlüğü
screenWidth, screenHeight = pyautogui.size()
print("Ekran Çzözünürlüğü :", screenWidth, screenHeight)

# Fare Pozisyonu
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)






pyautogui.moveTo(799, 466, duration=2,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()
for i in range(100):
    pyautogui.write('Ne yazık ki evet!', interval=0.001)
    pyautogui.press('enter')




    pyautogui.moveTo(100, 250, duration=2,
                 tween=pyautogui.easeInOutQuad)

distance = 200
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up







window = Tk()

window.title("Merhaba Python GUI")

window.mainloop()





window = Tk()

window.title("Merhaba Python GUI")
lbl = Label(window, text="Merhaba")
lbl2 = Label(window, text="Merhaba", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
lbl2.grid(column=1, row=0)
window.geometry('500x400')
window.mainloop()








window = Tk()

window.title("Merhaba Python GUI")
lbl = Label(window, text="Merhaba")
lbl2 = Label(window, text="Merhaba", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
lbl2.grid(column=1, row=0)
window.geometry('500x400')

btn = Button(window, text="Tıkla")
btn.grid(column=1, row=1)


def tiklandi():
    lbl.configure(text="Butona tıklandı")


btn2 = Button(window, text="Tıkla Renkli",
              bg="orange", fg="red",
              width=10, height=10,
              command=tiklandi
              )

btn2.grid(column=1, row=3)

window.mainloop()







window = Tk()

window.title("Merhaba Python GUI")
lbl = Label(window, text="Merhaba")
lbl2 = Label(window, text="Merhaba", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
lbl2.grid(column=1, row=0)
window.geometry('500x400')

btn = Button(window, text="Tıkla")
btn.grid(column=1, row=1)


def tiklandi():
    pyautogui.moveTo(100, 100, duration=1,
                     tween=pyautogui.easeInOutQuad)


btn2 = Button(window, text="Tıkla Renkli",
              bg="orange", fg="red",
              width=10, height=10,
              command=tiklandi
              )

btn2.grid(column=1, row=3)

window.mainloop()






window = Tk()

window.title("Merhaba Python GUI")
lbl = Label(window, text="Merhaba")
lbl2 = Label(window, text="Merhaba", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
lbl2.grid(column=1, row=0)
window.geometry('500x400')

btn = Button(window, text="Tıkla")
btn.grid(column=1, row=1)


def tiklandi():
    pyautogui.moveTo(100, 100, duration=1,
                     tween=pyautogui.easeInOutQuad)


btn2 = Button(window, text="Tıkla Renkli",
              bg="orange", fg="red",
              width=10, height=10,
              command=tiklandi
              )

btn2.grid(column=1, row=3)

txt = Entry(window, width=10)
txt.grid(column=0, row=1)

txt2 = Entry(window, width=10, font=("Courier New", 20))
txt2.grid(column=0, row=1)

window.mainloop()