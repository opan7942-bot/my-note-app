import customtkinter as ctk
import app_data

class TodoView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        # 1. Input Section (Bottom Area)
        self.input_frame = ctk.CTkFrame(self, fg_color=("gray85", "gray17"), corner_radius=12)
        self.input_frame.pack(side="bottom", fill="x", pady=(10, 0))

        self.task_enter = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Write a new task...",
            height=40,
            corner_radius=8
        )
        self.task_enter.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

        self.add_task_btn = ctk.CTkButton(
            self.input_frame,
            text="Add Task",
            command=self.add_task_function,
            width=100,
            height=40,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.add_task_btn.pack(side="right", padx=(0, 5), pady=10)

        self.clear_btn = ctk.CTkButton(
            self.input_frame,
            text="Clear Input",
            command=self.clear_task,
            fg_color="transparent",
            hover_color=("gray75", "gray25"),
            text_color=("gray30", "gray70"),
            width=80,
            height=40,
            corner_radius=8
        )
        self.clear_btn.pack(side="right", padx=(0, 10), pady=10)

        # 2. Tasks Container (Scrollable Area)
        self.scroll_todo = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            label_text="Active Tasks",
            label_font=ctk.CTkFont(size=14, weight="bold")
        )
        self.scroll_todo.pack(side="top", fill="both", expand=True)

        self.load_data()

    def create_task_row(self, text,task_id=None):
        """Helper to create a clean task item card with a delete button."""
        card = ctk.CTkFrame(self.scroll_todo, fg_color=("gray90", "gray20"), corner_radius=10)
        card.pack(side="top", fill="x", padx=5, pady=4)

        task_check = ctk.CTkCheckBox(
            card,
            text=text,
            font=ctk.CTkFont(size=13),
            corner_radius=6
        )
        task_check.configure(command=lambda cb=task_check, parent_card=card: self.on_check(cb, parent_card,task_id))
        task_check.pack(side="left", padx=15, pady=12, fill="x", expand=True)

        delete_btn = ctk.CTkButton(
            card,
            text="✕",
            width=28,
            height=28,
            corner_radius=6,
            fg_color="transparent",
            hover_color=("gray75", "gray30"),
            text_color=("gray40", "gray60"),
            command=lambda: self.delete_task(card,task_id)
        )
        delete_btn.pack(side="right", padx=10, pady=10)
    def delete_task(self,card,task_id):
        if task_id is not None:
            app_data.delete_todo_data(task_id)
        card.destroy()

    def add_task_function(self):
        text = self.task_enter.get()
        if text.strip() != '':
            app_data.add_todo_data(text)
            self.create_task_row(text)
            self.task_enter.delete(0, "end")

    def on_check(self, cb, parent_card,task_id):
        if cb.get() == 1:
            # Auto-destroy task after brief feedback delay
            self.after(1500, lambda: parent_card.destroy())
            self.delete_task(cb,task_id)

    def clear_task(self):
        self.task_enter.delete(0, "end")

    def load_data(self):
        todos = app_data.get_todos_data()
        for row in todos:
            self.create_task_row(task_id=row[0],text=row[1])