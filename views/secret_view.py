import customtkinter as ctk
import app_data

class SecretView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        # 1. Input Section (Bottom Area)
        self.input_frame = ctk.CTkFrame(self, fg_color=("gray85", "gray17"), corner_radius=12)
        self.input_frame.pack(side="bottom", fill="x", pady=(10, 0))

        self.secret_title = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Account / Title...",
            height=40,
            corner_radius=8
        )
        self.secret_title.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

        self.secret_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Password / Secret...",
            show="*",
            height=40,
            corner_radius=8
        )
        self.secret_entry.pack(side="left", fill="x", expand=True, padx=(0, 5), pady=10)

        self.add_secret_btn = ctk.CTkButton(
            self.input_frame,
            text="Save Secret",
            command=self.add_secret,
            width=110,
            height=40,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.add_secret_btn.pack(side="right", padx=(0, 10), pady=10)

        # 2. Secrets Container (Scrollable Area)
        self.scroll_secret = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            label_text="Saved Passwords & Secrets",
            label_font=ctk.CTkFont(size=14, weight="bold")
        )
        self.scroll_secret.pack(side="top", fill="both", expand=True)

        self.load_data()

    def create_secret_card(self, title, secret):
        """Helper to create a secure, toggleable secret card with a copy-ready feel."""
        card = ctk.CTkFrame(self.scroll_secret, fg_color=("gray90", "gray20"), corner_radius=10)
        card.pack(side="top", fill="x", padx=5, pady=4)

        # Account Title
        title_label = ctk.CTkLabel(
            card,
            text=title if title.strip() else "Untitled",
            font=ctk.CTkFont(size=13, weight="bold"),
            anchor="w"
        )
        title_label.pack(side="left", padx=(15, 5), pady=12)

        # Separator colon
        ctk.CTkLabel(card, text=":", font=ctk.CTkFont(size=13, weight="bold")).pack(side="left", padx=2)

        # Secret Value (masked by default using a CTkEntry)
        secret_field = ctk.CTkEntry(
            card,
            font=ctk.CTkFont(size=13),
            fg_color="transparent",
            border_width=0,
            show="*"
        )
        secret_field.insert(0, secret)
        secret_field.configure(state="readonly")
        secret_field.pack(side="left", padx=5, fill="x", expand=True)

        # Show/Hide Toggle Button
        toggle_btn = ctk.CTkButton(
            card,
            text="👁",
            width=30,
            height=28,
            corner_radius=6,
            fg_color="transparent",
            hover_color=("gray75", "gray30"),
            text_color=("gray30", "gray70"),
            command=lambda: self.toggle_secret_visibility(secret_field, toggle_btn)
        )
        toggle_btn.pack(side="right", padx=(2, 5), pady=10)

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

    def toggle_secret_visibility(self, field, btn):
        """Toggle between hidden asterisks and plain text."""
        if field.cget("show") == "*":
            field.configure(show="")
            btn.configure(text="🔒")
        else:
            field.configure(show="*")
            btn.configure(text="👁")

    def add_secret(self):
        secret = self.secret_entry.get()
        secret_title = self.secret_title.get()
        if secret.strip() != '':
            app_data.add_secret_data(secret_title, secret)
            self.create_secret_card(secret_title, secret)
            self.secret_entry.delete(0, "end")
            self.secret_title.delete(0, "end")

    def load_data(self):
        secrets = app_data.get_secret_data()
        for row in secrets:
            self.create_secret_card(row[0], row[1])