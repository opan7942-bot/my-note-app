import customtkinter as ctk
import app_data

from views.note_view import NoteView
from views.todo_view import TodoView
from views.secret_view import SecretView
from views.photo_view import PhotoView
from views.data_view import DataView

app_data.init_db()

class MyMainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات المظهر والنافذة الرئيسية
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.geometry("850x550")
        self.title("Notes manager")
        self.minsize(800, 500)

        # 1. شريط التنقل العلوي (Top Header Bar)
        self.navbar = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color=("gray90", "gray13"))
        self.navbar.pack(side="top", fill="x")

        # شعار التطبيق / العنوان في الأعلى يساراً
        self.logo_label = ctk.CTkLabel(
            self.navbar,
            text="⚡ Workspace",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.logo_label.pack(side="left", padx=20, pady=10)

        # إطار أزرار التنقل في المنتصف
        self.nav_buttons_frame = ctk.CTkFrame(self.navbar, fg_color="transparent")
        self.nav_buttons_frame.pack(side="left", expand=True, padx=10)

        # أزرار التبويب بنمط شفاف وأنيق
        self.btn_todo = self.create_nav_button("Todo", self.todo_page)
        self.btn_note = self.create_nav_button("Notes", self.note_page)
        self.btn_secret = self.create_nav_button("Secrets", self.secret_page)
        self.btn_photo = self.create_nav_button("Photos", self.photo_page)
        self.btn_data = self.create_nav_button("Data", self.upload_page)

        # قائمة المظهر (Theme Selector) في الأعلى يميناً
        self.theme_optionmenu = ctk.CTkOptionMenu(
            self.navbar,
            values=["System", "Dark", "Light"],
            command=self.change_appearance_mode_event,
            width=100,
            dynamic_resizing=False
        )
        self.theme_optionmenu.pack(side="right", padx=15, pady=10)

        # 2. إطار المحتوى الرئيسي (Main Content Container)
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        # تهيئة الصفحات داخل إطار المحتوى
        self.note = NoteView(self.container)
        self.todo = TodoView(self.container)
        self.secret = SecretView(self.container)
        self.photo = PhotoView(self.container)
        self.upload_download = DataView(self.container)

        self.nav_buttons = [self.btn_todo, self.btn_note, self.btn_secret, self.btn_photo, self.btn_data]

        # فتح صفحة Todo افتراضياً
        self.todo_page()

    def create_nav_button(self, text, command):
        """إنشاء أزرار تبويب مخصصة بنمط الويب"""
        btn = ctk.CTkButton(
            self.nav_buttons_frame,
            text=text,
            command=command,
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray80", "gray25"),
            corner_radius=8,
            width=90,
            height=32,
            font=ctk.CTkFont(size=13, weight="normal") # تم تعديل weight هنا
        )
        btn.pack(side="left", padx=3)
        return btn

    def set_active_button(self, active_btn):
        """تمييز الزر النشط حالياً وإعادة باقي الأزرار للوضع الشفاف"""
        for btn in self.nav_buttons:
            if btn == active_btn:
                btn.configure(fg_color=("gray80", "gray25"), font=ctk.CTkFont(size=13, weight="bold"))
            else:
                btn.configure(fg_color="transparent", font=ctk.CTkFont(size=13, weight="normal")) # وهنا أيضاً

    def forget_all(self):
        self.note.pack_forget()
        self.todo.pack_forget()
        self.secret.pack_forget()
        self.photo.pack_forget()
        self.upload_download.pack_forget()

    def note_page(self):
        self.forget_all()
        self.set_active_button(self.btn_note)
        self.note.pack(fill="both", expand=True)

    def todo_page(self):
        self.forget_all()
        self.set_active_button(self.btn_todo)
        self.todo.pack(fill="both", expand=True)

    def secret_page(self):
        self.forget_all()
        self.set_active_button(self.btn_secret)
        self.secret.pack(fill="both", expand=True)

    def photo_page(self):
        self.forget_all()
        self.set_active_button(self.btn_photo)
        self.photo.pack(fill="both", expand=True)

    def upload_page(self):
        self.forget_all()
        self.set_active_button(self.btn_data)
        self.upload_download.pack(fill="both", expand=True)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = MyMainWindow()
    app.mainloop()