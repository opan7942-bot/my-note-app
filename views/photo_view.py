import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import os


class PhotoView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        # 1. Action Section (Bottom Area)
        self.input_frame = ctk.CTkFrame(self, fg_color=("gray85", "gray17"), corner_radius=12)
        self.input_frame.pack(side="bottom", fill="x", pady=(10, 0))

        self.info_label = ctk.CTkLabel(
            self.input_frame,
            text="Manage and view your stored images",
            text_color=("gray40", "gray60"),
            font=ctk.CTkFont(size=12)
        )
        self.info_label.pack(side="left", padx=15, pady=10)

        self.add_photo_btn = ctk.CTkButton(
            self.input_frame,
            text="Add Photo",
            command=self.get_photo,
            width=110,
            height=40,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.add_photo_btn.pack(side="right", padx=10, pady=10)

        # 2. Photos Container (Scrollable Area)
        self.scroll_photo = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            label_text="Photo Gallery",
            label_font=ctk.CTkFont(size=14, weight="bold")
        )
        self.scroll_photo.pack(side="top", fill="both", expand=True)

    def add_photo_card(self, file_path):
        """Helper to create a stylized photo item card with name, preview, and actions."""
        card = ctk.CTkFrame(self.scroll_photo, fg_color=("gray90", "gray20"), corner_radius=10)
        card.pack(side="top", fill="x", padx=5, pady=4)

        try:
            # Thumbnail Preview
            img = Image.open(file_path)
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(60, 60))

            preview_btn = ctk.CTkButton(
                card,
                image=ctk_img,
                text="",
                width=60,
                height=60,
                corner_radius=8,
                fg_color="transparent",
                hover_color=("gray80", "gray30"),
                command=lambda: self.show_full_image(file_path)
            )
            preview_btn.pack(side="left", padx=10, pady=10)
        except Exception:
            # Fallback if image path fails to load
            ctk.CTkLabel(card, text="🖼️", font=ctk.CTkFont(size=24)).pack(side="left", padx=15, pady=10)

        # Image File Details
        file_name = os.path.basename(file_path)
        details_frame = ctk.CTkFrame(card, fg_color="transparent")
        details_frame.pack(side="left", fill="x", expand=True, padx=10)

        name_label = ctk.CTkLabel(
            details_frame,
            text=file_name,
            font=ctk.CTkFont(size=13, weight="bold"),
            anchor="w"
        )
        name_label.pack(side="top", fill="x")

        path_label = ctk.CTkLabel(
            details_frame,
            text=file_path,
            font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray60"),
            anchor="w"
        )
        path_label.pack(side="top", fill="x")

        # View Fullscreen Button
        view_btn = ctk.CTkButton(
            card,
            text="View",
            width=60,
            height=32,
            corner_radius=6,
            fg_color=("gray75", "gray30"),
            hover_color=("gray65", "gray40"),
            text_color=("gray10", "gray90"),
            command=lambda: self.show_full_image(file_path)
        )
        view_btn.pack(side="right", padx=5, pady=10)

        # Delete Button
        delete_btn = ctk.CTkButton(
            card,
            text="✕",
            width=28,
            height=28,
            corner_radius=6,
            fg_color="transparent",
            hover_color=("gray75", "gray30"),
            text_color=("gray40", "gray60"),
            command=lambda: card.destroy()
        )
        delete_btn.pack(side="right", padx=(5, 10), pady=10)

    def get_photo(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if file_path:
            self.add_photo_card(file_path)

    def show_full_image(self, file_path):
        """Displays a popup with an auto-scaled view of the photo."""
        popup = ctk.CTkToplevel(self)
        popup.title("Photo Viewer")
        popup.geometry("600x600")
        popup.grab_set()  # Focus popup window

        try:
            full_image = Image.open(file_path)
            # Maintain aspect ratio thumbnail max size for full view
            full_image.thumbnail((550, 550))

            full_ctk_img = ctk.CTkImage(
                light_image=full_image,
                dark_image=full_image,
                size=full_image.size
            )

            image_label = ctk.CTkLabel(popup, image=full_ctk_img, text="")
            image_label.pack(expand=True, fill="both", padx=20, pady=20)
        except Exception as e:
            ctk.CTkLabel(popup, text=f"Failed to load image:\n{e}").pack(expand=True)