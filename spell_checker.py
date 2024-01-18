from textblob import TextBlob 

from tkinter import *

def correct_spell():
    get_data=enter1.get()
    corr=TextBlob(get_data)
    data=corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)


def main_window():
    global enter1,enter2
    win=Tk()
    win.geometry("500x400")
    win.resizable(False,False)
    win.config(bg="Light Blue")
    win.title("Spell checker")
    
    label1=Label(win,text="Incorrect Spelling",bg="Light Blue", font=("Time New Roman",20,"bold"),fg="white")
    label1.place(x=20,y=20,height=50,width=300)
    
    enter1=Entry(win,font=("Time New Roman",20),bg='white',fg="Black")
    enter1.place(x=50,y=70,height=35,width=300)
    
    label1=Label(win,text="Correct Spelling",bg="Light Blue", font=("Time New Roman",20,"bold"),fg="white")
    label1.place(x=20,y=100,height=50,width=300)
    
    enter2=Entry(win,font=("Time New Roman",20),bg='white',fg="Black")
    enter2.place(x=50,y=160,height=35,width=300)

    button=Button(win,text="Done",bg="Blue", font=("Time New Roman",20,"bold"),fg="white",command=correct_spell)
    button.place(x=50,y=200,height=40,width=100)

    win.mainloop()

main_window()

# obj =TextBlob("lavaa") 
# print(obj.correct())