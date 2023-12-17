import tkinter as tk

form = tk.Tk()
form.title("Sign Language")
form.geometry("500x250")
form.state("zoomed")
form.configure(bg="beige")
label=tk.Label(form,text="Sign to Football", fg="#88AB8E",bg="beige", font="Times 25 italic") 

def search():
    pass



button = tk.Button(form,text="Home",fg="#EEE7DA",bg="#88AB8E",font="Times 10 italic bold",command=search)
button2 = tk.Button(form,text="Search",fg="#EEE7DA",bg="#88AB8E",font="Times 10 italic bold",command=search)
button3 = tk.Button(form,text="Sign Up",fg="#EEE7DA",bg="#88AB8E",font="Times 10 italic bold",command=search)
button4 = tk.Button(form,text="Log In",fg="#EEE7DA",bg="#88AB8E",font="Times 10 italic bold",command=search)

giris = tk.Entry(form,fg="#EEE7DA",bg="#AFC8AD")
giris.pack()
giris.place(height=25, width=200, relx=0.5, rely=0.06)

def verial():
    etiket['text']=giris.get()

def sil():
    giris.delete(0,'end')
    

buton = tk.Button(text='search', fg="#EEE7DA",bg="#88AB8E",font="Times 10 italic bold", command=verial)
buton.pack()
buton.place(height=17, width=45, relx=0.5, rely=0.10)
buton1=tk.Button(text='delete', fg="#EEE7DA",bg="#88AB8E",font="Times 10 italic bold", command=sil)
buton1.pack()
buton1.place(height=17, width=45, relx=0.5, rely=0.13)

etiket=tk.Label(text='entryler burada')
etiket.pack()

label.pack()
label.place(height=50,relx=0.05,rely=0.05)

button.pack()
button.place(height=50, width=60, relx=0.7,rely=0.05)
button2.pack()
button2.place(height=50,width=60, relx=0.75,rely=0.05)
button3.pack()
button3.place(height=50, width=60, relx=0.80,rely=0.05)
button4.pack()
button4.place(height=50, width=60, relx=0.85,rely=0.05) 
form.mainloop()