import tkinter as tk

form = tk.Tk()
form.title("Log in - Sign up")
form.geometry("500x250")
form.state("zoomed")
form.configure(bg="#AFC8AD")

mail= tk.Label(text='Mail: ' , fg='black', bg='#EEE7DA' , font='Times 10 bold')
mail.place(height=25, width=40, relx=0.2 , rely=0.3)
sifre=tk.Label(text='Şifre: ', fg='black', bg='#EEE7DA' , font='Times 10 bold')
sifre.place(height=25, width=40, relx=0.2 , rely=0.35)

mail_entry=tk.Entry()
mail_entry.place(relx=0.24 , rely=0.3)

sifre_entry=tk.Entry()
sifre_entry.place(relx=0.24 , rely=0.35)

def kayıtol():
    mail= tk.Label(text='Mail: ' , fg='black', bg='#EEE7DA' , font='Times 10 bold')
    mail.place(height=25, width=40, relx=0.2 , rely=0.75)
    sifre=tk.Label(text='Şifre: ', fg='black', bg='#EEE7DA' , font='Times 10 bold')
    sifre.place(height=25, width=40, relx=0.2 , rely=0.80)
    isim=tk.Label(text='İsim: ', fg='black', bg='#EEE7DA' , font='Times 10 bold')
    isim.place(height=25, width=40, relx=0.2 , rely=0.7)

    mail_entry=tk.Entry()
    mail_entry.place(relx=0.24 , rely=0.75)

    sifre_entry=tk.Entry()
    sifre_entry.place(relx=0.24 , rely=0.80)

    isim_entry=tk.Entry()
    isim_entry.place(relx=0.24 , rely=0.7)

def girişyap():
    mail_entry.delete(0, 'end')
    sifre_entry.delete(0,'end')

def sifregizle():
    if sifre_entry.cget("show") == "":
        sifre_entry.config(show="*")
    else:
        sifre_entry.config(show="")
    

kayıtol_btn= tk.Button(form, text='Kayıt Ol', fg='black', bg='#EEE7DA' , font='Times 10 bold', command=kayıtol)
kayıtol_btn.place(relx=0.24 , rely=0.40)

giris_btn= tk.Button(form, text='Giriş Yap', fg='black', bg='#EEE7DA' , font='Times 10 bold', command=girişyap)
giris_btn.place(relx=0.28 , rely=0.40)

sifregizle_btn= tk.Button(form, text='Şifre gizle', fg='black', bg='#EEE7DA' , font='Times 10 bold', command=sifregizle)
sifregizle_btn.place(relx=0.33 , rely=0.35)

form.mainloop()