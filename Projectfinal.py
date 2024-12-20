from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# Clear Entry
def ClearEntry():
    EntryBase.delete(0, END)
    EntryFromBase.delete(0, END)
    EntryToBase.delete(0, END)


def set_text(text):
    defult.set(text)


def Calculate():
    en = EntryBaseG.get()
    box1 = EntryFromBase.get()
    box2 = EntryToBase.get()
    Alist = []

    if (box1 == "10" and box2 == "2"):
        Alist = []
        for i in range(0, 10):
            y = en % 2
            en = en/2
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "3"):
        Alist = []
        for i in range(0, 10):
            y = en % 3
            en = en/3
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "4"):
        Alist = []
        for i in range(0, 10):
            y = en % 4
            en = en/4
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "5"):
        Alist = []
        for i in range(0, 10):
            y = en % 5
            en = en/5
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "6"):
        Alist = []
        for i in range(0, 10):
            y = en % 6
            en = en/6
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "7"):
        Alist = []
        for i in range(0, 10):
            y = en % 7
            en = en/7
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "8"):
        Alist = []
        for i in range(0, 8):
            y = en % 8
            en = en/8
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "9"):
        Alist = []
        for i in range(0, 10):
            y = en % 9
            en = en/9
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "11"):
        Alist = []
        for i in range(0, 10):
            y = en % int(box2)
            en = en//int(box2)
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "12"):
        Alist = []
        for i in range(0, 10):
            y = en % int(box2)
            en = en//int(box2)
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "13"):
        Alist = []
        for i in range(0, 10):
            y = en % int(box2)
            en = en//int(box2)
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "14"):
        Alist = []
        for i in range(0, 10):
            y = en % int(box2)
            en = en//int(box2)
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "15"):
        Alist = []
        for i in range(0, 10):
            y = en % int(box2)
            en = en//int(box2)
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "10" and box2 == "16"):
        Alist = []
        for i in range(0, 10):
            y = en % int(box2)
            en = en//int(box2)
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "3"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        tri = decimal
        for i in range(0, 10):
            y = tri % 3
            tri = tri/3
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "4"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        fou = decimal
        for i in range(0, 10):
            y = fou % 4
            fou = fou/4
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "5"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        fif = decimal
        for i in range(0, 10):
            y = fif % 5
            fif = fif/5
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "6"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        sixy = decimal
        for i in range(0, 10):
            y = sixy % 6
            sixy = sixy/6
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "7"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        sev = decimal
        for i in range(0, 10):
            y = sev % 7
            sev = sev/7
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "8"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        octa = decimal
        for i in range(0, 10):
            y = octa % 8
            octa = octa/8
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "9"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        nin = decimal
        for i in range(0, 10):
            y = nin % 9
            nin = nin/9
            Alist.append(int(y))
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "10"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
                set_text(decimal)

    if (box1 == "2" and box2 == "11"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        elev = decimal
        for i in range(0, 10):
            y = elev % 11
            elev = elev//11
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "12"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        tw = decimal
        for i in range(0, 10):
            y = tw % 12
            tw = tw//12
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "13"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        thi = decimal
        for i in range(0, 10):
            y = thi % 13
            thi = thi//13
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "14"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        fot = decimal
        for i in range(0, 10):
            y = fot % 14
            fot = fot//14
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "15"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        fift = decimal
        for i in range(0, 10):
            y = fift % 15
            fift = fift//15
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break

    if (box1 == "2" and box2 == "16"):
        num = str(en)
        decimal = 0
        pos = len(num)
        for i in num:
            pos = pos - 1
            if int(i) != 0:
                decimal = decimal + 2**pos
        Alist = []
        hexter = decimal
        for i in range(0, 10):
            y = hexter % 16
            hexter = hexter//16
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            Alist.append(y)
        Alist.reverse()
        for i in range(len(Alist)):
            if Alist[i] != 0:
                set_text(Alist)
                break


# Build Window
mainframe = Tk()
mainframe.option_add("*Font", "impact 15")
mainframe.title("Base Number ")
mainframe.geometry("850x400")
"""--------------------------------------------------------------------"""

# Position an object on a window page.
BaseTitle = ttk.Label(mainframe, text="Number Base System")
BaseTitle.grid(row=0, column=1, padx=55)
BaseTitle2 = ttk.Label(mainframe, text="ใส่เลขที่ต้องการ")
BaseTitle2.grid(row=2, column=2, padx=55)
EntryBaseG = IntVar()
EntryBase = ttk.Entry(width=20, textvariable=EntryBaseG)  # input Number
EntryBase.grid(row=3, column=2, padx=10)
"""--------------------------------------------------------------------"""

# Button Enter
BaseButtonEnter = ttk.Button(
    mainframe, text="Calculate", command=Calculate)  # Calculate
BaseButtonEnter.grid(row=7, column=2, padx=10)
BaseButtonClear = ttk.Button(
    mainframe, text="Clear", command=ClearEntry)  # Clear Entry
BaseButtonClear.grid(row=7, column=0, padx=10)
"""--------------------------------------------------------------------"""

FromBase = ttk.Label(mainframe, text="จากฐานอะไร")
FromBase.grid(row=2, column=0, padx=10)
EnFrombase = IntVar()  # get int
EntryFromBase = ttk.Combobox(mainframe, width=20)
EntryFromBase['values'] = (2, 10)
EntryFromBase.grid(row=3, column=0, padx=10, pady=15)  # input first base

"""--------------------------------------------------------------------"""

ToBase = ttk.Label(text="อยากได้ฐานอะไร")
ToBase.grid(row=2, column=1, padx=10, pady=20)
EnToBase = IntVar()
EntryToBase = ttk.Combobox(mainframe, width=20)
EntryToBase['values'] = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
EntryToBase.grid(row=3, column=1, padx=10)  # input last base

"""--------------------------------------------------------------------"""
# Result
LBResult = ttk.Label(mainframe, text="ผลลัพธ์จ้าาา")
LBResult.grid(row=8, column=1, padx=55)
defult = IntVar(mainframe, 0)
ResultBase = ttk.Entry(textvariable=defult).grid(
    row=9, column=1, padx=55)  # result base


"""--------------------------------------------------------------------"""

# picture
Courage = Image.open("Courage.png")
Courage = Courage.resize((100, 100), Image.ANTIALIAS)
BGCourage = ImageTk.PhotoImage(Courage)

LBCourage = ttk.Label(image=BGCourage)
LBCourage.grid(row=11, column=1, padx=60)

# Am = Image.open("Am.png")
# Am = Am.resize((125,125), Image.ANTIALIAS)
# BGAm = ImageTk.PhotoImage(Am)

# LBAm = ttk.Label(image = BGAm)
# LBAm.grid(row = 11, column = 0, padx = 60)

# Goku1 = Image.open("Goku1.png")
# Goku1 = Goku1.resize((125,125), Image.ANTIALIAS)
# BGGoku1 = ImageTk.PhotoImage(Goku1)

# LBGoku1 = ttk.Label(image = BGGoku1)
# LBGoku1.grid(row = 11, column = 2, padx = 60)

Banana = ttk.Label(mainframe, text="Banana Team")
Banana.grid(row=10, column=0, padx=20)
Banana1 = ttk.Label(mainframe, text="Banana Team")
Banana1.grid(row=10, column=2, padx=20)
"""--------------------------------------------------------------------"""

mainframe.mainloop()
