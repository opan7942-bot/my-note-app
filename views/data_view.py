import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import shutil


class DataView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        # Header Section
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(side="top", fill="x", pady=(0, 20))

        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="Database Management",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.title_label.pack(side="top", anchor="w")

        # Cards Container
        self.cards_container = ctk.CTkFrame(self, fg_color="transparent")
        self.cards_container.pack(side="top", fill="both", expand=True)

        # 1. Export Card
        self.export_card = ctk.CTkFrame(self.cards_container, fg_color=("gray90", "gray20"), corner_radius=12)
        self.export_card.pack(side="top", fill="x", pady=10, ipady=10)

        ctk.CTkLabel(
            self.export_card,
            text="📤 Export Database",
            font=ctk.CTkFont(size=15, weight="bold")
        ).pack(side="left", padx=20)

        self.download_btn = ctk.CTkButton(
            self.export_card,
            text="Export Database",
            command=self.download_file,
            width=140,
            height=36
        )
        self.download_btn.pack(side="right", padx=20)

        # 2. Import Card
        self.import_card = ctk.CTkFrame(self.cards_container, fg_color=("gray90", "gray20"), corner_radius=12)
        self.import_card.pack(side="top", fill="x", pady=10, ipady=10)

        ctk.CTkLabel(
            self.import_card,
            text="📥 Import External Database",
            font=ctk.CTkFont(size=15, weight="bold")
        ).pack(side="left", padx=20)

        self.upload_btn = ctk.CTkButton(
            self.import_card,
            text="Import & Replace",
            command=self.upload_file,
            width=140,
            height=36
        )
        self.upload_btn.pack(side="right", padx=20)


    @staticmethod
    def get_base_dir() -> str:
        """تحديد المسار الحقيقي لمجلد المشروع بصيغة نصية صريحة"""
        return str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


    def download_file(self):
        """تصدير قاعدة البيانات لمجلد Exports بجانب البرنامج وفتحه مباشرة"""
        base_dir: str = self.get_base_dir()
        db_path: str = os.path.join(base_dir, "data", "my_app_data.db")

        if not os.path.exists(db_path):
            messagebox.showwarning("Warning", f"No database found at:\n{db_path}")
            return

        export_dir: str = os.path.join(base_dir, "Exports")
        os.makedirs(export_dir, exist_ok=True)

        destination: str = os.path.join(export_dir, "my_app_data.db")

        try:
            shutil.copy(str(db_path), str(destination))
            os.startfile(export_dir)
            messagebox.showinfo("Success", "Database exported to 'Exports' folder!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {e}")


    def upload_file(self):
        """استيراد ملف واستبدال قاعدة البيانات الحالية"""
        file_path = filedialog.askopenfilename(filetypes=[("Database File", "*.db")])
        if file_path:
            base_dir: str = self.get_base_dir()
            db_dir: str = os.path.join(base_dir, "data")
            os.makedirs(db_dir, exist_ok=True)
            db_path: str = os.path.join(db_dir, "my_app_data.db")

            try:
                shutil.copy(str(file_path), str(db_path))
                messagebox.showinfo("Success", "Database imported successfully!\nPlease restart the app.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to replace file: {e}")