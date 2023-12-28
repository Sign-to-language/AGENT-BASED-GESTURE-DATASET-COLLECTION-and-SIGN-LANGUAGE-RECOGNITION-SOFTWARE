import tkinter 
from PIL import Image
import customtkinter


def switch_window(window_to_hide, window_to_show):
    window_to_hide.withdraw()
    window_to_show.deiconify()

# First Window
app1 = tkinter.Tk()
width= app1.winfo_screenwidth() 
height= app1.winfo_screenheight()
app1.geometry("%dx%d" % (width, height))
app1.state('zoomed')
app1.title("Sign To Language")
app1.configure(bg="#EEF0E5")


label = customtkinter.CTkLabel(master=app1,text="Sign to Language", width=210, height=150, text_color="#163020" , font=("Castellar", 35))
label.place(relx=0.14,rely=0.06, anchor=tkinter.CENTER)
 

button = customtkinter.CTkButton(master=app1,text="Home",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="Search",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app1, app2))
button.place(relx=0.60, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app1, app3))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app1,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app1, app4))
button.place(relx=0.90, rely=0.06, anchor=tkinter.CENTER)

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
app2 = tkinter.Toplevel()
width= app2.winfo_screenwidth() 
height= app2.winfo_screenheight()
app2.geometry("%dx%d" % (width, height))
app2.state('zoomed')
app2.title("Search")
app2.configure(bg="#EEF0E5")
app2.withdraw()  

label = customtkinter.CTkLabel(master=app2,text="Sign to Language", width=210, height=150, text_color="#163020" , font=("Castellar", 35))
label.place(relx=0.14,rely=0.06, anchor=tkinter.CENTER)


button = customtkinter.CTkButton(master=app2,text="Home",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app2, app1))
button.place(relx=0.45, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app2,text="Search",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.60, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app2,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app2, app3))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app2,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app2, app4))
button.place(relx=0.90, rely=0.06, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=app2,width=1580,height=700,corner_radius=100, fg_color="#88AB8E")
frame.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app2,text="SEARCH A LETTER ", width=210, height=150, text_color="#EEF0E5" , font=("Poor Richard", 35), bg_color="#88AB8E")
label.place(relx=0.52,rely=0.3, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app2,width=240,height=50,corner_radius=10, bg_color="#88AB8E", fg_color="#EEF0E5", placeholder_text="Search in Sign to Language..." , text_color="black")
entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

text = entry.get()

img = Image.open("search1.png")

btn = customtkinter.CTkButton(master=app2, text="", corner_radius=32, bg_color="#88AB8E", fg_color="#EEF0E5",
                hover_color="#88AB8E", border_color="#FFCC70", width=50, height=50, image=customtkinter.CTkImage(dark_image=img, light_image=img))


btn.place(relx=0.62, rely=0.4, anchor="center")

# Third Window
app3 = tkinter.Toplevel()
width= app3.winfo_screenwidth() 
height= app3.winfo_screenheight()
app3.geometry("%dx%d" % (width, height))
app3.state('zoomed')
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
button.place(relx=0.60, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app3,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=app3,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app3,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app3, app4))
button.place(relx=0.90, rely=0.06, anchor=tkinter.CENTER)

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
app4.geometry("%dx%d" % (width, height))
app4.state("withdrawn")
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
button.place(relx=0.60, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app4,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25) , command=lambda: switch_window(app4, app3))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app4,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25))
button.place(relx=0.90, rely=0.06, anchor=tkinter.CENTER)

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
app5.geometry("%dx%d" % (width, height))
app5.state("withdrawn")
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
button.place(relx=0.60, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app5,text="Sign Up",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app5, app3))
button.place(relx=0.75, rely=0.06, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app5,text="Log In",width=120,height=32,border_width=0,corner_radius=8 , fg_color="#EEF0E5", 
                hover_color="#163020", text_color="#AFC8AD", font=("Castellar", 25), command=lambda: switch_window(app5, app4))
button.place(relx=0.90, rely=0.06, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=app5,width=1580,height=700,corner_radius=100, fg_color="#88AB8E")
frame.place(relx=0.55, rely=0.6, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(master=app5,text="PREVIOUSLY LEARNED LETTERS ", width=210, height=150, text_color="#EEF0E5" , font=("Poor Richard", 35), bg_color="#88AB8E")
label.place(relx=0.52,rely=0.3, anchor=tkinter.CENTER)

# Run the main loop
app1.mainloop()