import tkinter 
from PIL import Image
import customtkinter
from tkinter import ttk
import random
import os

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
app3.title("Search")
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

entry = customtkinter.CTkEntry(master=app3,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your name..." ,text_color="black")
entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

text = entry.get()

label = customtkinter.CTkLabel(master=app3,text="Surname ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.45, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app3,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your surname...",text_color="black" )
entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

text = entry.get()

label = customtkinter.CTkLabel(master=app3,text="E-mail ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.55, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app3,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your e-mail address..." ,text_color="black")
entry.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

text = entry.get()

label = customtkinter.CTkLabel(master=app3,text="Password ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.45,rely=0.65, anchor=tkinter.CENTER)

entry1 = customtkinter.CTkEntry(master=app3,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your password..." ,text_color="black", show="*")
entry1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app3,text="SIGN UP",width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5",
                hover_color="#88AB8E", text_color="black", font=("Castellar", 15)) 
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

# Fourth Window
app4 = tkinter.Toplevel()
width= app4.winfo_screenwidth() 
height= app4.winfo_screenheight()
app4.geometry("%d400x%d240" % (width, height))
app4.title("Search")
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

entry = customtkinter.CTkEntry(master=app4,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your e-mail address..." ,text_color="black")
entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

text = entry.get()

label = customtkinter.CTkLabel(master=app4,text="Password ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.45, anchor=tkinter.CENTER)

entry1 = customtkinter.CTkEntry(master=app4,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your password..." ,text_color="black" , show="*")
entry1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app4,text="LOG IN",width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5",
                hover_color="#88AB8E", text_color="black", font=("Castellar", 15))
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Fifth Window
app5 = tkinter.Toplevel()
width= app5.winfo_screenwidth() 
height= app5.winfo_screenheight()
app5.geometry("%d400x%d240" % (width, height))
app5.title("Search")
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
app6.title("Search")
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

frame = customtkinter.CTkFrame(master=app6,width=1580,height=700,corner_radius=100, fg_color="#88AB8E")
frame.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER)

# Seventh Window
app7 = tkinter.Toplevel()
width= app7.winfo_screenwidth() 
height= app7.winfo_screenheight()
app7.geometry("%d400x%d240" % (width, height))
app7.title("Search")
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

entry = customtkinter.CTkEntry(master=app7,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your e-mail address..." ,text_color="black")
entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

text = entry.get()

label = customtkinter.CTkLabel(master=app7,text=" Admin Password ", width=10, height=10, text_color="black" , font=("Book Antiqua", 13), bg_color="#88AB8E")
label.place(relx=0.44,rely=0.45, anchor=tkinter.CENTER)

entry1 = customtkinter.CTkEntry(master=app7,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Enter your password..." ,text_color="black" , show="*")
entry1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app7,text="LOG IN" ,width=75,height=25,border_width=0,corner_radius=8 , bg_color="#88AB8E", fg_color="#EEF0E5", hover_color="#88AB8E", text_color="black", font=("Castellar", 15) , command=lambda: switch_window(app7, app6))
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Run the main loop
app1.mainloop()
