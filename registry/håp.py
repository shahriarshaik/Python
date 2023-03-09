from tkinter import *
#from PIL import Image,ImageTk
import xlsxwriter


FørsteOgAndre = []
TredjeOgFjerde = []
FemteOgSjette = []
SjuendeOgÅttende = []


root = Tk()


canv = Canvas(root, width=1920, height=1080, bg='white')
canv.pack()
pic = PhotoImage(file= 'haap.png')
btn = PhotoImage(file='11.png')
canv.create_image(150, 10, anchor=NW, image=pic)


root.title('Shahriar sitt galeste program')
root.configure(bg='#4b4b4b')
root.geometry('1700x1080')
barn_skr = Label(root,  text='Barnets navn:', fg='#000000', bg='white', font=('calibri', 20, 'bold')).place(x=10, y=10)
alder_skr = Label(root, text='Alder:', fg='black', bg='white', font=('calibri', 20, 'bold')).place(x=10, y=50)
notif = Label(root, text='(Hvor gammel barnet blir i år)', bg = 'white').place(x=332, y = 65)
MHR = Label(root, text=''' Made by
MHR''', bg = 'white').place(x=1640, y = 0)


def knapp ():
    fordele()
    clear()
def fordele():
    if alder.get() < 7:
        FørsteOgAndre.append(str(navn.get()))
    elif alder.get() < 9:
        TredjeOgFjerde.append(str(navn.get()))
    elif alder.get() < 11:
        FemteOgSjette.append(str(navn.get()))
    elif alder.get() < 13:
        SjuendeOgÅttende.append(str(navn.get()))
def clear():
    navn.set('')
    alder.set('')


navn = StringVar()
alder = IntVar()
alder.set('')
navn_boks = Entry(root, textvariable = navn, bg ='#9fd27c', width=40).place(x=180, y = 25)
alder_boks = Entry(root, textvariable = alder, bg ='#9fd27c', width=40).place(x=90, y = 65)
registrer_knapp = Button(root, image=btn, command= knapp, border=0, bg='white').place(x=430, y=20)


root.mainloop()


liste_barn = xlsxwriter.Workbook('liste.xlsx')


enOgto= liste_barn.add_worksheet()
treOgfire= liste_barn.add_worksheet()
femOgseks= liste_barn.add_worksheet()
syvOgåtte= liste_barn.add_worksheet()

row = 0
row2 = 0
row3 = 0
row4 = 0
col = 0

def tittel():
    enOgto.write(row, col, "Barn som går i første og andre:")
    treOgfire.write(row, col, "Barn som går i andre og fjerde:")
    femOgseks.write(row, col, "Barn som går i femte og sjette:")
    syvOgåtte.write(row, col, "Barn som går i sjuende og åttende:")

tittel()

for barn in (FørsteOgAndre):
    enOgto.write(row + 1, col, barn)
    row += 1
for barn in (TredjeOgFjerde):
    treOgfire.write(row2 + 1, col, barn)
    row2 += 1
for barn in (FemteOgSjette):
    femOgseks.write(row3 + 1, col, barn)
    row3 += 1
for barn in (SjuendeOgÅttende):
    syvOgåtte.write(row4 + 1, col, barn)
    row4 += 1


liste_barn.close()