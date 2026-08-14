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
        #note page sitting
        self.scroll_note = ctk.CTkScrollableFrame(self.note)
        self.scroll_note.pack(side="top",fill="both",expand=True)

        self.note_textbox = ctk.CTkTextbox(self.note)
        self.note_textbox.pack(side="right",padx=10,pady=10)
        #===================

        self.todo = ctk.CTkFrame(self)
        ctk.CTkLabel(self.todo, text="To do").pack(side="top")
        #to do page sitting
        self.scroll_todo = ctk.CTkScrollableFrame(self.todo)
        self.scroll_todo.pack(fill="both", expand=True,padx=10,pady=10)

        self.task_enter = ctk.CTkEntry(self.todo,placeholder_text="new task")
        self.task_enter.pack(side="right",padx=60,pady=10)
        #=======================
        self.secret = ctk.CTkFrame(self)
        ctk.CTkLabel(self.secret, text="Password").pack(side="top")
        #secret page sitting
        self.scroll_secret = ctk.CTkScrollableFrame(self.secret)
        self.scroll_secret.pack(fill="both",expand=True,padx=10,pady=10)

        self.secret_entry = ctk.CTkEntry(self.secret,placeholder_text="new secret",show="*")
        self.secret_entry.pack(side="right",padx=6,pady=10)
        self.secret_title = ctk.CTkEntry(self.secret,placeholder_text="new title")
        self.secret_title.pack(side="right",padx=0,pady=10)
        #=======================
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
            #note bottoms
        self.add_note_btn = ctk.CTkButton(self.note,text="save",command= self.add_note)
        self.add_note_btn.pack(side="top",padx=10,pady=10)
            #================
        self.todo_btm = ctk.CTkButton(self.sidebar,text="Todo",command= self.todo_page)
        self.todo_btm.pack(side="top",padx=10,pady=10)
            #to do bottoms
        self.add_task_btm = ctk.CTkButton(self.todo,text='add',command=self.add_task_function)
        self.add_task_btm.pack(side="right",padx=10,pady=10)

        self.clear = ctk.CTkButton(self.todo,text="Clear",command=self.clear_task)
        self.clear.pack(side="right",padx=0,pady=5)
            #=================

        self.secret_btm = ctk.CTkButton(self.sidebar,text="Secret",command= self.secret_page)
        self.secret_btm.pack(side="top",padx=10,pady=10)
            #secret bottoms
        self.add_secret_btn = ctk.CTkButton(self.secret,text="add",command= self.add_secret)
        self.add_secret_btn.pack(side="left",padx=50,pady=10)
            #=================
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
        #note functions
    def add_note(self):
        text = self.note_textbox.get("1.0","end")
        if text != '':
            new_box = ctk.CTkTextbox(self.scroll_note, height=70)
            new_box.insert("1.0", text)
            new_box.pack(side="top", fill="x", padx=5, pady=5)
            self.note_textbox.delete("1.0", "end")
        #====================

    def todo_page(self):
        self.forget_all()
        self.todo.pack(fill="both",padx=10,pady=10,expand=True)

        #to do functions
    def add_task_function(self):
        text = self.task_enter.get()
        if text != '':
            task_check = ctk.CTkCheckBox(self.scroll_todo,text=text)
            task_check.configure(command=lambda cd=task_check:self.on_check(cd))
            task_check.pack(side="top", anchor="w",padx=10,pady=10)
            self.task_enter.delete(0,"end")
    def on_check(self,cb):
        if cb.get() ==1:
            self.after(30000,lambda: cb.destroy())

    def clear_task(self):
        self.task_enter.delete(0,"end")
        #================

    def secret_page(self):
        self.forget_all()
        self.secret.pack(fill="both",padx=10,pady=10, expand=True)
        #secret functions
    def add_secret(self):
        secret = self.secret_entry.get()
        secret_title = self.secret_title.get()
        text= f"{secret_title} : {secret}"
        if secret != '':
            text_box = ctk.CTkLabel(self.scroll_secret,text=text)
            text_box.pack(side="top",anchor="w", fill="x", padx=5, pady=5)
            self.secret_entry.delete(0,"end")
            self.secret_title.delete(0,"end")
        #================
    def photo_page(self):
        self.forget_all()
        self.photo.pack(fill="both",padx=10,pady=10, expand=True)

    def upload_page(self):
        self.forget_all()
        self.upload_download.pack(fill="both",padx=10,pady=10, expand=True)

app = MyMainWindow()
app.mainloop()