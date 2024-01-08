import tkinter 
from PIL import Image
import customtkinter
from tkinter import ttk
import random
import os
import ASLdataagent as data
import shutil
import json

useremail = ""  
isLogged = False

def switch_window(window_to_hide, window_to_show):
    window_to_hide.withdraw()
    window_to_show.deiconify()


# First Window
app1 = tkinter.Tk()
width= app1.winfo_screenwidth() 
height= app1.winfo_screenheight()
app1.geometry("%d400x%d240" % (width, height))
app1.title("Sign To Language")
app1.configure(bg="#EEF0E5")


label = customtkinter.CTkLabel(master=app1,text="Sign to Language", width=210, height=150, text_color="#163020" , font=("Castellar", 35))
label.place(relx=0.15,rely=0.06, anchor=tkinter.CENTER)


button = customtkinter.CTkButton(master=app1,text="Home",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="Search",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app1, app2))
button.place(relx=0.55, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app1, app3))
button.place(relx=0.65, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app1, app4))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="Admin",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app1, app7))
button.place(relx=0.85, rely=0.06, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app1,text="Search for \n the letter you want\n\n",width=120,height=25,corner_radius=8, text_color="#163020" , font=("Rockwell", 30))
label.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app1,text="Sign To Language is a user-friendly \n\n project designed to assist hearing-impaired \n\n individuals in finding the American Sign Language (ASL) \n\n equivalents of letters they are looking for \n\n anytime and anywhere they desire.",width=120,height=25,corner_radius=8, text_color="#163020" , font=("Poor Richard", 20))
label.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="SEARCH NOW",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 20) , command=lambda: switch_window(app1, app2))
button.place(relx=0.2, rely=0.7, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app1,text="or",width=120,height=25,corner_radius=8, text_color="#163020" , font=("Poor Richard", 20))
label.place(relx=0.2, rely=0.74, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="Go to previously \n learned letters",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 20) , command=lambda: switch_window(app1, app5))
button.place(relx=0.2, rely=0.8, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=app1,width=1000,height=700,corner_radius=100, fg_color="#88AB8E")
frame.place(relx=0.80, rely=0.6, anchor=tkinter.CENTER)

my_image = customtkinter.CTkImage(light_image=Image.open('img3.jpg'),dark_image=Image.open('img3.jpg'),size=(650,390)) 

my_label = customtkinter.CTkLabel(app1, text="", image=my_image)
my_label.place(relx=0.75, rely=0.6, anchor=tkinter.CENTER)


# Second Window
def clickSearch():
    text = entry2.get()
    for widget in content_frame.winfo_children():
        if isinstance(widget, customtkinter.CTkLabel) and widget != content_frame.winfo_children()[0]:
            widget.destroy()

    if len(text) == 1:
        text = text.lower()
        y = 0.15
        x = 0.1
        counter = 0

        files = [os.path.join(f"Data\\{text}", f) for f in os.listdir(f"Data\\{text}") if os.path.isfile(os.path.join(f"Data\\{text}", f))]

        for file in files:
            label = customtkinter.CTkLabel(master=content_frame, text=text.upper(), width=210, height=150, text_color="#EEF0E5",
                               font=("Castellar", 35))
            label.place(relx=x, rely=y-0.05)
            my_image = customtkinter.CTkImage(light_image=Image.open(file), size=(200, 180))
            my_label = customtkinter.CTkLabel(content_frame, text="", image=my_image)
            my_label.place(relx=x, rely=y)
            counter += 1

            if counter == 4:
                y += 0.12
                x = 0.1
                counter = 0
            else:
                x += 0.2

        content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        y = 0.15
        x = 0.1
        counter = 0
        text = text.lower()
        textLength = len(text)
        for k in range(textLength):
            letter = text[k]
            if letter == " ":
                x = 0.1
                y += 0.12
                counter = 0
                continue
            files = [os.path.join(f"Data\\{letter}", f) for f in os.listdir(f"Data\\{letter}") if os.path.isfile(os.path.join(f"Data\\{letter}", f))]
            random1 = random.randint(0, len(files)-1)

            label = customtkinter.CTkLabel(master=content_frame, text=letter.upper(), width=210, height=150, text_color="#EEF0E5",
                               font=("Castellar", 35))
            label.place(relx=x, rely=y-0.05)

            my_image = customtkinter.CTkImage(light_image=Image.open(files[random1]), size=(200, 180))
            my_label = customtkinter.CTkLabel(content_frame, text="", image=my_image)
            my_label.place(relx=x, rely=y)
            counter += 1

            if counter == 4:
                y += 0.12
                x = 0.1
                counter = 0
            else:
                x += 0.2
        content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))                


app2 = tkinter.Toplevel()
width = app2.winfo_screenwidth()
height = app2.winfo_screenheight()
app2.geometry("%d400x%d240" % (width, height))
app2.title("Search")
app2.configure(bg="#EEF0E5")
app2.withdraw()

label = customtkinter.CTkLabel(master=app2, text="Sign to Language", width=210, height=150, text_color="#163020",
                               font=("Castellar", 35))
label.place(relx=0.14, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app2, text="Home", width=120, height=32, border_width=0, corner_radius=8,
                                 fg_color="#EEF0E5",
                                 hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25),
                                 command=lambda: switch_window(app2, app1))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app2, text="Search", width=120, height=32, border_width=0, corner_radius=8,
                                 fg_color="#EEF0E5",
                                 hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.55, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app2, text="Sign Up", width=120, height=32, border_width=0, corner_radius=8,
                                 fg_color="#EEF0E5",
                                 hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25),
                                 command=lambda: switch_window(app2, app3))
button.place(relx=0.65, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app2, text="Log In", width=120, height=32, border_width=0, corner_radius=8,
                                 fg_color="#EEF0E5",
                                 hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25),
                                 command=lambda: switch_window(app2, app4))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app2,text="Admin",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app2, app7))
button.place(relx=0.85, rely=0.06, anchor=tkinter.CENTER)


canvas = tkinter.Canvas(app2)
canvas.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER, width=1580, height=700)

scrollbar = ttk.Scrollbar(app2, orient="vertical", command=canvas.yview)
scrollbar.place(relx=0.98, rely=0.6, anchor=tkinter.CENTER, relheight=0.6)

canvas.configure(yscrollcommand=scrollbar.set)

content_frame = customtkinter.CTkFrame(canvas, width=1580, height=2000, corner_radius=100, fg_color="#88AB8E")
canvas.create_window((0, 0), window=content_frame, anchor="nw")

label = customtkinter.CTkLabel(master=content_frame, text="SEARCH A LETTER ", width=210, height=150, text_color="#EEF0E5",
                               font=("Poor Richard", 35), bg_color="#88AB8E")
label.place(relx=0.46, rely=0.05, anchor=tkinter.CENTER)

entry2 = customtkinter.CTkEntry(master=content_frame, width=240, height=50, corner_radius=10, bg_color="#88AB8E",
                                 fg_color="#EEF0E5", placeholder_text="Search in Sign to Language...", text_color="black")
entry2.place(relx=0.43, rely=0.08, anchor=tkinter.CENTER)

img = Image.open("search1.png")
btn = customtkinter.CTkButton(master=content_frame, text="", corner_radius=32, bg_color="#88AB8E", fg_color="#EEF0E5",
                               hover_color="#88AB8E", border_color="#FFCC70", width=50, height=50,
                               image=customtkinter.CTkImage(dark_image=img, light_image=img), command=clickSearch)
btn.place(relx=0.54, rely=0.08, anchor="center")



# Third Window
app3 = tkinter.Toplevel()
width= app3.winfo_screenwidth() 
height= app3.winfo_screenheight()
app3.geometry("%d400x%d240" % (width, height))
app3.title("Sign Up")
app3.configure(bg="#EEF0E5")
app3.withdraw()  

label = customtkinter.CTkLabel(master=app3,text="Sign to Language", width=210, height=150, text_color="#163020" , font=("Castellar", 35))
label.place(relx=0.14,rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app3,text="Home",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app3, app1))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app3,text="Search",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app3, app2))
button.place(relx=0.55, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app3,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.65, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app3,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app3, app4))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app3,text="Admin",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app3, app7))
button.place(relx=0.85, rely=0.06, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=app3,width=1580,height=700,corner_radius=100, fg_color="#88AB8E")
frame.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app3,text="CREATE ACCOUNT ", width=210, height=150, text_color="#EEF0E5" , font=("Poor Richard", 35), bg_color="#88AB8E")
label.place(relx=0.50,rely=0.3, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app3,text="Name ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.35, anchor=tkinter.CENTER)

entry3 = customtkinter.CTkEntry(master=app3,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your name..." ,text_color="black")
entry3.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

input3 = entry3.get()

label = customtkinter.CTkLabel(master=app3,text="Surname ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.45, anchor=tkinter.CENTER)

entry4 = customtkinter.CTkEntry(master=app3,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your surname...",text_color="black" )
entry4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

input4 = entry4.get()

label = customtkinter.CTkLabel(master=app3,text="E-mail ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.55, anchor=tkinter.CENTER)

entry5 = customtkinter.CTkEntry(master=app3,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your e-mail address..." ,text_color="black")
entry5.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

input5 = entry5.get()

label = customtkinter.CTkLabel(master=app3,text="Password ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.45,rely=0.65, anchor=tkinter.CENTER)

entry6 = customtkinter.CTkEntry(master=app3,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your password..." ,text_color="black", show="*")
entry6.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

input6 = entry6.get()

def signUp():
    # JSON dosyasının adı
    dosya_adi = "veri.json"

    try:
        # Mevcut dosyayı oku
        with open(dosya_adi, 'r') as dosya:
            mevcut_veri = json.load(dosya)
    except FileNotFoundError:
        # Dosya bulunamazsa boş bir dizi oluştur
        mevcut_veri = []

    # Yeni veriyi al
    name = entry3.get()
    surname = entry4.get()
    email = entry5.get()
    password = entry6.get()

    # E-posta kontrolü
    for kayit in mevcut_veri:
        if kayit["email"] == email:
            messagebox.showinfo(title="Sign Up" , message="This email is already registered!")
            return  # E-posta zaten kayıtlıysa işlemi sonlandır
        
    switch_window(app3, app4)
    # Yeni veriyi bir sözlük olarak oluştur
    yeni_veri = {
        "email": email,
        "password": password,
        "name": name,
        "surname": surname,
        "letters" : []
    }

    # Yeni veriyi diziye ekle
    mevcut_veri.append(yeni_veri)

    # JSON dosyasına yazma işlemi
    with open(dosya_adi, 'w') as dosya:
        json.dump(mevcut_veri, dosya)
        messagebox.showinfo(title="Sign Up" , message="Registration successful!")

    entry3.delete(0, tkinter.END)
    entry4.delete(0, tkinter.END)
    entry5.delete(0, tkinter.END)
    entry6.delete(0, tkinter.END)
    
    
button = customtkinter.CTkButton(master=app3,text="SIGN UP",width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5",
                hover_color="#88AB8E", text_color="black", font=("Castellar", 15), command = signUp) 
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)


# Fourth Window
app4 = tkinter.Toplevel()
width= app4.winfo_screenwidth() 
height= app4.winfo_screenheight()
app4.geometry("%d400x%d240" % (width, height))
app4.title("Log In")
app4.configure(bg="#EEF0E5")
app4.withdraw()  

label = customtkinter.CTkLabel(master=app4,text="Sign to Language", width=210, height=150, text_color="#163020" , font=("Castellar", 35))
label.place(relx=0.14,rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app4,text="Home",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app4, app1))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app4,text="Search",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app4, app2))
button.place(relx=0.55, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app4,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app4, app3))
button.place(relx=0.65, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app4,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app4,text="Admin",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app4, app7))
button.place(relx=0.85, rely=0.06, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=app4,width=1580,height=700,corner_radius=100, fg_color="#88AB8E")
frame.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app4,text="LOG IN ", width=210, height=150, text_color="#EEF0E5" , font=("Poor Richard", 35), bg_color="#88AB8E")
label.place(relx=0.50,rely=0.3, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app4,text="E-mail ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.35, anchor=tkinter.CENTER)

entry7 = customtkinter.CTkEntry(master=app4,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your e-mail address..." ,text_color="black")
entry7.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

input7 = entry7.get()

label = customtkinter.CTkLabel(master=app4,text="Password ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.45, anchor=tkinter.CENTER)

entry8 = customtkinter.CTkEntry(master=app4,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your password..." ,text_color="black" , show="*")
entry8.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

input8 = entry8.get()

button = customtkinter.CTkButton(master=app4,text="LOG IN",width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5",
                hover_color="#88AB8E", text_color="black", font=("Castellar", 15))
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Fifth Window
app5 = tkinter.Toplevel()
width= app5.winfo_screenwidth() 
height= app5.winfo_screenheight()
app5.geometry("%d400x%d240" % (width, height))
app5.title("Previously Learned")
app5.configure(bg="#EEF0E5")
app5.withdraw() 

label = customtkinter.CTkLabel(master=app5,text="Sign to Language", width=210, height=150, text_color="#163020" , font=("Castellar", 35))
label.place(relx=0.14,rely=0.06, anchor=tkinter.CENTER)


button = customtkinter.CTkButton(master=app5,text="Home",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app5, app1))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app5,text="Search",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app5, app2))
button.place(relx=0.55, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app5,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app5, app3))
button.place(relx=0.65, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app5,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app5, app4))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app5,text="Admin",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app5, app7))
button.place(relx=0.85, rely=0.06, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=app5,width=1580,height=700,corner_radius=100, fg_color="#88AB8E")
frame.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app5,text="PREVIOUSLY LEARNED LETTERS ", width=210, height=150, text_color="#EEF0E5" , font=("Poor Richard", 35), bg_color="#88AB8E")
label.place(relx=0.52,rely=0.3, anchor=tkinter.CENTER)

# Sixth Window
app6 = tkinter.Toplevel()
width= app6.winfo_screenwidth() 
height= app6.winfo_screenheight()
app6.geometry("%d400x%d240" % (width, height))
app6.title("Admin Panel")
app6.configure(bg="#EEF0E5")
app6.withdraw() 

label = customtkinter.CTkLabel(master=app6,text="Sign to Language", width=210, height=150, text_color="#163020" , font=("Castellar", 35))
label.place(relx=0.14,rely=0.06, anchor=tkinter.CENTER)


button = customtkinter.CTkButton(master=app6,text="Home",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app6, app1))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app6,text="Search",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app6, app2))
button.place(relx=0.55, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app6,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app6, app3))
button.place(relx=0.65, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app6,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app6, app4))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app6,text="Admin",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app6, app7))
button.place(relx=0.85, rely=0.06, anchor=tkinter.CENTER)



canvas1 = tkinter.Canvas(app6)
canvas1.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER, width=1580, height=700)

scrollbar1 = ttk.Scrollbar(app6, orient="vertical", command=canvas1.yview)
scrollbar1.place(relx=0.98, rely=0.6, anchor=tkinter.CENTER, relheight=0.6)

canvas1.configure(yscrollcommand=scrollbar1.set)


content_frame1 = customtkinter.CTkFrame(canvas1, width=1580, height=10000, corner_radius=100, fg_color="#88AB8E")
canvas1.create_window((0, 0), window=content_frame1, anchor="nw")

content_frame1.update_idletasks()
canvas1.configure(scrollregion=canvas1.bbox("all"))      

label = customtkinter.CTkLabel(master=content_frame1,text=" ADMIN PANEL", width=210, height=150, text_color="#EEF0E5" , font=("Poor Richard", 35), bg_color="#88AB8E")
label.place(relx=0.50,rely=0.01, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.signasl.org/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.02, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector1)
button.place(relx=0.7, rely=0.02, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://alphabet.lingvano.com/glossary", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.025, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector2)
button.place(relx=0.7, rely=0.025, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.wikihow.com/Fingerspell-the-Alphabet-in-American-Sign-Language", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.03, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector3)
button.place(relx=0.7, rely=0.03, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.alamy.com/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.035, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector4)
button.place(relx=0.7, rely=0.035, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.alamy.com/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.035, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector5)
button.place(relx=0.7, rely=0.035, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.alamy.com/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.04, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector6)
button.place(relx=0.7, rely=0.04, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.alamy.com/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.045, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector7)
button.place(relx=0.7, rely=0.045, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.alamy.com/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.05, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector8)
button.place(relx=0.7, rely=0.05, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.alamy.com/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.055, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector9)
button.place(relx=0.7, rely=0.055, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.ava.me/asl", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.06, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector10)
button.place(relx=0.7, rely=0.06, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.signingsavvy.com/sign/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.065, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector11)
button.place(relx=0.7, rely=0.065, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.signingsavvy.com/wordlist/fingerspelling", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.07, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector12)
button.place(relx=0.7, rely=0.07, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.spreadthesign.com/en.us/alphabet/21/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.075, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector13)
button.place(relx=0.7, rely=0.075, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.spreadthesign.com/en.us/alphabet/21/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.08, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector14)
button.place(relx=0.7, rely=0.08, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="https://www.handspeak.com/word/", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.4,rely=0.085, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=content_frame1,text="PULL DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= data.dataCollector15)
button.place(relx=0.7, rely=0.085, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=content_frame1,text="DATA", width=10, height=10, text_color="black" , font=("Book Antiqua", 20), bg_color="#88AB8E")
label.place(relx=0.5,rely=0.095, anchor=tkinter.CENTER)

def refresh():
    for widget in content_frame1.winfo_children():
        if isinstance(widget, customtkinter.CTkLabel) and widget._image is not None:
            widget.destroy()
    y = 0.1
    x = 0.02
    err = False
    counter = 0
    for text in "abcdefghijklmnopqrstuvwxyz":
        try:
            files = [os.path.join(f"Data\\{text}", f) for f in os.listdir(f"Data\\{text}") if os.path.isfile(os.path.join(f"Data\\{text}", f))]
        except:
            err = True
        finally:
            if not err:
                for file in files:
                    my_image = customtkinter.CTkImage(light_image=Image.open(file), size=(100, 90))
                    my_label = customtkinter.CTkLabel(content_frame1, text="", image=my_image)
                    my_label.place(relx=x, rely=y)
                    counter += 1

                    if counter == 9:
                        y += 0.01
                        x = 0.02
                        counter = 0
                    else:
                        x += 0.1

            content_frame1.update_idletasks()

    canvas1.configure(scrollregion=canvas1.bbox("all"))

button = customtkinter.CTkButton(master=content_frame1,text="REFRESH" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= refresh)
button.place(relx=0.7, rely=0.095, anchor=tkinter.CENTER)

def deleteData():
    file_path = "Data"

    try:
        # Dosyayı sil
        os.remove(file_path)
        print(f"{file_path} başarıyla silindi.")
    except PermissionError as pe:
        print(f"Izin hatası: {pe}")
        shutil.rmtree(file_path, ignore_errors=True)
        print(f"{file_path} başarıyla silindi.")
    except OSError as e:
        print(f"Hata oluştu: {e}")

button = customtkinter.CTkButton(master=content_frame1,text="DELETE DATA" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command= deleteData)
button.place(relx=0.8, rely=0.095, anchor=tkinter.CENTER)

# Seventh Window
app7 = tkinter.Toplevel()
width= app7.winfo_screenwidth() 
height= app7.winfo_screenheight()
app7.geometry("%d400x%d240" % (width, height))
app7.title("Admin")
app7.configure(bg="#EEF0E5")
app7.withdraw() 

label = customtkinter.CTkLabel(master=app7,text="Sign to Language", width=210, height=150, text_color="#163020" , font=("Castellar", 35))
label.place(relx=0.14,rely=0.06, anchor=tkinter.CENTER)


button = customtkinter.CTkButton(master=app7,text="Home",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app7, app1))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app7,text="Search",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app7, app2))
button.place(relx=0.55, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app7,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app7, app3))
button.place(relx=0.65, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app7,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app7, app4))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app7,text="Admin",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.85, rely=0.06, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=app7,width=1580,height=700,corner_radius=100, fg_color="#88AB8E")
frame.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app7,text=" ADMIN LOG IN ", width=210, height=150, text_color="#EEF0E5" , font=("Poor Richard", 35), bg_color="#88AB8E")
label.place(relx=0.50,rely=0.3, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app7,text=" Admin E-mail ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.35, anchor=tkinter.CENTER)

entry9 = customtkinter.CTkEntry(master=app7,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your e-mail address..." ,text_color="black")
entry9.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

input9 = entry9.get()

label = customtkinter.CTkLabel(master=app7,text=" Admin Password ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.45, anchor=tkinter.CENTER)

entry10 = customtkinter.CTkEntry(master=app7,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your password..." ,text_color="black" , show="*")
entry10.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

input10 = entry10.get()



def adminCheck():
    text = entry9.get()
    text1 = entry10.get()
    print(text, text1)
    if text == "admin" and text1 == "admin":
        switch_window(app7, app6)

button = customtkinter.CTkButton(master=app7,text="LOG IN" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command=adminCheck)
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)




# Run the main loop
app1.mainloop()
