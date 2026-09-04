import customtkinter as ctk
import app_data

class NoteView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        # 1. Input Section (Bottom Area)
        self.input_frame = ctk.CTkFrame(self, fg_color=("gray85", "gray17"), corner_radius=12)
        self.input_frame.pack(side="bottom", fill="x", pady=(10, 0))

        self.note_textbox = ctk.CTkTextbox(
            self.input_frame,
            height=70,
            corner_radius=8,
            activate_scrollbars=False
        )
        self.note_textbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.add_note_btn = ctk.CTkButton(
            self.input_frame,
            text="Save Note",
            command=self.add_note,
            width=110,
            height=40,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.add_note_btn.pack(side="right", padx=10, pady=10)

        # 2. Notes Container (Scrollable Area)
        self.scroll_note = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            label_text="Saved Notes",
            label_font=ctk.CTkFont(size=14, weight="bold")
        )
        self.scroll_note.pack(side="top", fill="both", expand=True)

        self.load_data()

    def create_note_card(self, text, note_id=None):
        """Helper to create a stylized note card with a quick delete button."""
        card = ctk.CTkFrame(self.scroll_note, fg_color=("gray90", "gray20"), corner_radius=10)
        card.pack(side="top", fill="x", padx=5, pady=6)

        # Note Content
        note_label = ctk.CTkLabel(
            card,
            text=text.strip(),
            wraplength=550,
            justify="left",
            font=ctk.CTkFont(size=13)
        )
        note_label.pack(side="left", padx=15, pady=12, fill="x", expand=True)

        # Quick Delete Button
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
        delete_btn.pack(side="right", padx=10, pady=10)

    def add_note(self):
        text = self.note_textbox.get("1.0", "end")
        if text.strip() != '':
            app_data.add_note_data(text)
            self.create_note_card(text)
            self.note_textbox.delete("1.0", "end")

    def load_data(self):
        notes = app_data.get_notes_data()
        for row in notes:
            self.create_note_card(row[0])