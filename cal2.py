from tkinter import *
import time
root=Tk()
root.title("Cal")
root.configure(background='red')
def Show(x):
    global s
    s=s+x
    data.set(s)
def Result():
    global s
    try:
        s=str(eval(data.get()))
        data.set(s)
    except Exception as e: 
        s=e
        data.set(s)
def Clear():
    global s
    s=''
    data.set(s)
def Clear1():
    global s
    s=s[:len(s)-1]
    data.set(s)
def Clock():
    global lb
    lb['text']=time.ctime()
    lb.after(1000,Clock)
data=StringVar()
s=''
e=Entry(root,width=25,textvariable=data,font=("arial",25,"bold"),justif='right',bg='powder blue',
        bd=5,relief='raised')
e.grid(row=0,column=0,padx=5,pady=5,sticky='nswe',columnspan=4)
l=["789/","456*","123+",".0-"]
k=1
for text in l:
    j=0
    for c in text:
        Button(root,text=c,command=lambda x=c:Show(x),bg='powder blue',font=("arial",25,"bold"),
               bd=5,relief='raised').grid(row=k,column=j,padx=5,pady=5,sticky='nswe')
        j=j+1
    k=k+1

Button(root,text="=",command=Result,bg='powder blue',font=("arial",25,"bold"),bd=5,relief='raised'
               ).grid(row=4,column=3,padx=5,pady=5,sticky='nswe')
Button(root,text="C",command=Clear,bg='powder blue',font=("arial",25,"bold"),bd=5,relief='raised'
               ).grid(row=5,column=0,padx=5,pady=5,sticky='nswe',columnspan=2)
Button(root,text="CE",command=Clear1,bg='powder blue',font=("arial",25,"bold"),bd=5,relief='raised'
               ).grid(row=5,column=2,padx=5,pady=5,sticky='nswe',columnspan=2)

lb=Label(root,bg='powder blue',font=("arial",25,"bold"),bd=5,relief='raised')
lb.grid(row=6,column=0,padx=5,pady=5,sticky='nswe',columnspan=4)

Button(root,text="Close",command=root.destroy,bg='powder blue',font=("arial",25,"bold"),
       bd=5,relief='raised').grid(row=7,column=0,padx=5,pady=5,sticky='nswe',columnspan=4)
for i in range(8):
    root.grid_rowconfigure(i,weight=1)
for i in range(4):
    root.grid_columnconfigure(i,weight=1)
    
Clock()
root.mainloop()
