import customtkinter as ctk

class MyMainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.geometry("700x400")
        self.title("Note")

        #pages
        self.note = ctk.CTkFrame(self)
        ctk.CTkLabel(self.note, text="Note").pack(side="top")

        self.todo = ctk.CTkFrame(self)
        ctk.CTkLabel(self.todo, text="To do").pack(side="top")

        self.secret = ctk.CTkFrame(self)
        ctk.CTkLabel(self.secret, text="Password").pack(side="top")

        self.photo = ctk.CTkFrame(self)
        ctk.CTkLabel(self.photo, text="Pics").pack(side="top")

        self.upload_download = ctk.CTkFrame(self)
        ctk.CTkLabel(self.upload_download, text="Data").pack(side="top")

        #frames for the app
        self.sidebar = ctk.CTkFrame(self,width=180)
        self.sidebar.pack(side="left", fill="y")

        #labels
        sidebar_label = ctk.CTkLabel(self.sidebar,text="Menu")
        sidebar_label.pack(side="top",padx=10,pady=10)


        #bottoms
        self.note_btm = ctk.CTkButton(self.sidebar,text="Note",command= self.note_page)
        self.note_btm.pack(side="top",padx=10,pady=10)

        self.todo_btm = ctk.CTkButton(self.sidebar,text="Todo",command= self.todo_page)
        self.todo_btm.pack(side="top",padx=10,pady=10)

        self.secret_btm = ctk.CTkButton(self.sidebar,text="Secret",command= self.secret_page)
        self.secret_btm.pack(side="top",padx=10,pady=10)

        self.photo_btm = ctk.CTkButton(self.sidebar,text="Photo",command= self.photo_page)
        self.photo_btm.pack(side="top",padx=10,pady=10)

        self.upload_download_btm = ctk.CTkButton(self.sidebar,text="Upload/download",command= self.upload_page)
        self.upload_download_btm.pack(side="top",padx=10,pady=10)


        self.todo_page()
        #functions
    def forget_all(self):
        self.note.pack_forget()
        self.todo.pack_forget()
        self.secret.pack_forget()
        self.photo.pack_forget()
        self.upload_download.pack_forget()

    def note_page(self):
        self.forget_all()
        self.note.pack(fill="both",padx=10,pady=10,expand=True)

    def todo_page(self):
        self.forget_all()
        self.todo.pack(fill="both",padx=10,pady=10,expand=True)

    def secret_page(self):
        self.forget_all()
        self.secret.pack(fill="both",padx=10,pady=10, expand=True)

    def photo_page(self):
        self.forget_all()
        self.photo.pack(fill="both",padx=10,pady=10, expand=True)

    def upload_page(self):
        self.forget_all()
        self.upload_download.pack(fill="both",padx=10,pady=10, expand=True)

app = MyMainWindow()
app.mainloop()

