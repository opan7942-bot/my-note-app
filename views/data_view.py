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
            text="Backup & Data Management",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.title_label.pack(side="top", anchor="w")

        self.subtitle_label = ctk.CTkLabel(
            self.header_frame,
            text="Export your database for safe storage or import an existing backup file.",
            font=ctk.CTkFont(size=12),
            text_color=("gray50", "gray60")
        )
        self.subtitle_label.pack(side="top", anchor="w", pady=(2, 0))

        # Cards Container
        self.cards_container = ctk.CTkFrame(self, fg_color="transparent")
        self.cards_container.pack(side="top", fill="both", expand=True)

        # 1. Export Card (Download / Export Backup)
        self.export_card = ctk.CTkFrame(self.cards_container, fg_color=("gray90", "gray20"), corner_radius=12)
        self.export_card.pack(side="top", fill="x", pady=10, ipady=10)

        self.export_info = ctk.CTkFrame(self.export_card, fg_color="transparent")
        self.export_info.pack(side="left", padx=20, pady=10, fill="both", expand=True)

        ctk.CTkLabel(
            self.export_info,
            text="📤 Export Backup",
            font=ctk.CTkFont(size=15, weight="bold")
        ).pack(side="top", anchor="w")

        ctk.CTkLabel(
            self.export_info,
            text="Save a copy of your current database (.db file) to any location.",
            font=ctk.CTkFont(size=12),
            text_color=("gray40", "gray60")
        ).pack(side="top", anchor="w", pady=(2, 0))

        self.download_btn = ctk.CTkButton(
            self.export_card,
            text="Export Now",
            command=self.download_file,
            width=120,
            height=36,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.download_btn.pack(side="right", padx=20, pady=10)

        # 2. Import Card (Upload / Import Backup)
        self.import_card = ctk.CTkFrame(self.cards_container, fg_color=("gray90", "gray20"), corner_radius=12)
        self.import_card.pack(side="top", fill="x", pady=10, ipady=10)

        self.import_info = ctk.CTkFrame(self.import_card, fg_color="transparent")
        self.import_info.pack(side="left", padx=20, pady=10, fill="both", expand=True)

        ctk.CTkLabel(
            self.import_info,
            text="📥 Import Database",
            font=ctk.CTkFont(size=15, weight="bold")
        ).pack(side="top", anchor="w")

        ctk.CTkLabel(
            self.import_info,
            text="Replace current application data with a previously saved (.db) file.",
            font=ctk.CTkFont(size=12),
            text_color=("gray40", "gray60")
        ).pack(side="top", anchor="w", pady=(2, 0))

        self.upload_btn = ctk.CTkButton(
            self.import_card,
            text="Import File",
            command=self.upload_file,
            fg_color=("gray75", "gray30"),
            hover_color=("gray65", "gray40"),
            text_color=("gray10", "gray90"),
            width=120,
            height=36,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.upload_btn.pack(side="right", padx=20, pady=10)

    def upload_file(self):
        """Import and replace current database file."""
        file_path = filedialog.askopenfilename(filetypes=[("Database File", "*.db")])
        if file_path:
            db_dir = os.path.join(os.getcwd(), "data")
            os.makedirs(db_dir, exist_ok=True)
            target_path = os.path.join(db_dir, "app.db")

            try:
                shutil.copy(file_path, target_path)
                messagebox.showinfo("Success", "Database imported successfully! Please restart the application to apply changes.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import database: {e}")

    def download_file(self):
        """Export and save a backup of current database file."""
        db_path = os.path.join(os.getcwd(), "data", "app.db")
        if not os.path.exists(db_path):
            messagebox.showwarning("Warning", "No active database file found to export!")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".db",
            filetypes=[("Database File", "*.db")],
            initialfile="backup_app.db"
        )
        if save_path:
            try:
                shutil.copy(db_path, save_path)
                messagebox.showinfo("Success", "Backup exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export backup: {e}")