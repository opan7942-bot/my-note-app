import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import os ,shutil
import app_data

app_data.init_db()

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
        #photo page sitting
        self.scroll_photo = ctk.CTkScrollableFrame(self.photo)
        self.scroll_photo.pack(fill="both",expand=True,padx=10,pady=10)


        #======================

        self.upload_download = ctk.CTkFrame(self)
        ctk.CTkLabel(self.upload_download, text="Data").pack(side="top")
        #data page sitting
        self.button_place = ctk.CTkFrame(self.upload_download,width=180)
        self.button_place.pack(side="top",padx=10,pady=10)
        #=====================

        #frames for the app
        self.sidebar = ctk.CTkFrame(self,width=180)
        self.sidebar.pack(side="left", fill="y")

        #labels
        sidebar_label = ctk.CTkLabel(self.sidebar,text="Menu")
        sidebar_label.pack(side="top",padx=10,pady=10)


        #buttons
        self.note_btm = ctk.CTkButton(self.sidebar,text="Note",command= self.note_page)
        self.note_btm.pack(side="top",padx=10,pady=10)
            #note buttons
        self.add_note_btn = ctk.CTkButton(self.note,text="save",command= self.add_note)
        self.add_note_btn.pack(side="top",padx=10,pady=10)
            #================
        self.todo_btm = ctk.CTkButton(self.sidebar,text="Todo",command= self.todo_page)
        self.todo_btm.pack(side="top",padx=10,pady=10)
            #to do buttons
        self.add_task_btm = ctk.CTkButton(self.todo,text='add',command=self.add_task_function)
        self.add_task_btm.pack(side="right",padx=10,pady=10)

        self.clear = ctk.CTkButton(self.todo,text="Clear",command=self.clear_task)
        self.clear.pack(side="right",padx=0,pady=5)
            #=================

        self.secret_btm = ctk.CTkButton(self.sidebar,text="Secret",command= self.secret_page)
        self.secret_btm.pack(side="top",padx=10,pady=10)
            #secret buttons
        self.add_secret_btn = ctk.CTkButton(self.secret,text="add",command= self.add_secret)
        self.add_secret_btn.pack(side="left",padx=50,pady=10)
            #=================
        self.photo_btm = ctk.CTkButton(self.sidebar,text="Photo",command= self.photo_page)
        self.photo_btm.pack(side="top",padx=10,pady=10)
            # photo buttons
        self.add_photo = ctk.CTkButton(self.photo,text="add",command= self.get_photo)
        self.add_photo.pack(side="right",padx=10,pady=10)

            #================

        self.upload_download_btm = ctk.CTkButton(self.sidebar,text="Upload/download",command= self.upload_page)
        self.upload_download_btm.pack(side="top",padx=10,pady=10)
            # data buttons
        self.upload_btn = ctk.CTkButton(self.button_place,text="upload",command= self.upload_file)
        self.upload_btn.pack(side="left",padx=10,pady=10)

        self.download_btn = ctk.CTkButton(self.button_place,text="download",command= self.download_file)
        self.download_btn.pack(side="right",padx=10,pady=10)

        self.download = ctk.CTkButton(self)
            #===============
        self.load_saved_data()

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
            app_data.add_note_data(text)
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
            app_data.add_todo_data(text)
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
            app_data.add_secret_data(secret_title,secret)
            text_box = ctk.CTkLabel(self.scroll_secret,text=text)
            text_box.pack(side="top",anchor="w", fill="x", padx=5, pady=5)
            self.secret_entry.delete(0,"end")
            self.secret_title.delete(0,"end")
        #================
    def photo_page(self):
        self.forget_all()
        self.photo.pack(fill="both",padx=10,pady=10, expand=True)
        #photo functions
    def get_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
        if file_path:
            img = Image.open(file_path)
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(50, 50))

            btn = ctk.CTkButton(
                self.scroll_photo,
                image=ctk_img,
                text="",
                fg_color="transparent",  # يجعل خلفية الزر شفافة لتظهر الصورة فقط
                command=lambda: self.show_full_image(file_path)
            )
            btn.pack(side="right", pady=10)

    def show_full_image(self, file_path):
        popup = ctk.CTkToplevel(self)
        popup.title("Full Image")
        popup.geometry("500x500")

        full_image = Image.open(file_path)
        full_ctk_img = ctk.CTkImage(light_image=full_image, dark_image=full_image, size=(450, 450))
        image_label = ctk.CTkLabel(popup, image=full_ctk_img, text="")
        image_label.pack(expand=True)
        #================

    def upload_page(self):
        self.forget_all()
        self.upload_download.pack(fill="both",padx=10,pady=10, expand=True)
        #data function
        """this functions aren't complete yet (upload , download)"""
    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("file", "*.db")])
        if file_path:
            print(file_path)
    def download_file(self):
        current = os.getcwd()
        data_path = os.path.join(current,"data")
        folder_in = os.listdir(data_path)
        if "test.txt" in folder_in:
            print(True)
        else:
            print(False)
        #===============
        #reload data to app
    def load_saved_data(self):
        # 1. تحميل الملاحظات
        notes = app_data.get_notes_data()
        for row in notes:
            # row عبارة عن tuple يحتوي عل النص في العنصر الأول row[0]
            new_box = ctk.CTkTextbox(self.scroll_note, height=70)
            new_box.insert("1.0", row[0])
            new_box.pack(side="top", fill="x", padx=5, pady=5)

        # 2. تحميل المهام
        todos = app_data.get_todos_data()
        for row in todos:
            task_check = ctk.CTkCheckBox(self.scroll_todo, text=row[0])
            task_check.configure(command=lambda cd=task_check: self.on_check(cd))
            task_check.pack(side="top", anchor="w", padx=10, pady=10)

        # 3. تحميل الأسرار
        secrets = app_data.get_secret_data()
        for row in secrets:
            # row[0] هي العنوان و row[1] هي كلمة السر
            text = f"{row[0]} : {row[1]}"
            text_box = ctk.CTkLabel(self.scroll_secret, text=text)
            text_box.pack(side="top", anchor="w", fill="x", padx=5, pady=5)

        #=================
app = MyMainWindow()
app.mainloop()