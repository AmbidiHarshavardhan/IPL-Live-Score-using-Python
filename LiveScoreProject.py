from tkinter import *
from PIL import ImageTk, Image
from os import *
from bs4 import BeautifulSoup as BS
from urllib import *

url = 'http://static.cricinfo.com/rss/livescores.xml'
score_link = request.urlopen(url)

scrap = BS(score_link, 'html.parser')
res = scrap.find_all('description')


liveScore = []
for score_part in res:
	liveScore.append(score_part.get_text())

def score():
	T.insert(END, liveScore)

def clear():
	T.delete(1.0, END)

root = Tk()
root.title("IPL LIVE SCORES 2020")
root.geometry('800x600')
root.configure(background="black")



img = ImageTk.PhotoImage(file='C:/Users/Harsha Vardhan/Downloads/AH.png')
panel = Label(root, image=img)
panel.place(x=0, y=0)

T = Text(root)
T.place(x=200, y=250, height=100, width=400)

l = Label(root, text="LIVE SCORE", fg="white", bg="red")
l.place(x=200, y=350, height=30, width=400)

b1 = Button(root, text="DISPLAY SCORE", bg="blue", fg="white", command=score)
b1.place(x=120, y=450, height=80, width=250)

b2 = Button(root, text="CLEAR SCORE", bg="blue", fg="white", command=clear)
b2.place(x=420, y=450, height=80, width=250)

root.mainloop()