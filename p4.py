from tkinter import *
from tkinter.messagebox import *
from pymongo import *



root = Tk()
root.title("app bt me")
root.geometry("700x600+100+50")
f=("Arial",30,"bold")

labName=Label(root,text="enter name",font=f)
entName=Entry(root,font=f)
labName.place(x=20,y=20)
entName.place(x=300,y=20)

labPhone=Label(root,text="enter phone",font=f)
entPhone=Entry(root,font=f)
labPhone.place(x=20,y=80)
entPhone.place(x=300,y=80)

py,ja,js = IntVar(), IntVar(),IntVar()
labCourse=Label(root,text="enter course",font=f)
cnPython=Checkbutton(root,text="python",font=f,variable=py)
cnjava=Checkbutton(root,text="java",font=f,variable=ja)
cnjs=Checkbutton(root,text="js",font=f,variable=js)


labCourse.place(x=20,y=150)
cnPython.place(x=300,y=150)
cnjava.place(x=300,y=200)
cnjs.place(x=300,y=250)



def save():
	con=None
	try:
		con = MongoClient("localhost",27017)
		db = con["kit_24dec23"]
		coll = db["student"]
	
		name= entName.get()
		phone = int(entPhone.get())
		course=""
		if py.get():
			course += "python"
		if ja.get():
			course += "java"
		if js.get():
			course += "js"

		info = {"name":name,"phone":phone , "course":course}
		coll.insert_one(info)
		showinfo("success","we will get back to u asap")
		entName.delete(0,END)
		entPhone.delete(0,END)
		py.set(0)
		ja.set(0)
		js.set(0)
		entName.focus()
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

btnSubmit = Button(root,text="Submit",font=f,command=save)
btnSubmit.place(x=300,y=350)

def confirmExit():
	if askyesno('ja rahe ho ','jana hai kya?'):
		if askyesno('sachi','mat jao'):
			root.destroy()

root.protocol('WM_DELETE_WINDOW',confirmExit)








root.mainloop()
			

