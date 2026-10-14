import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class NotebookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Buddy")
        self.root.geometry("1200x760")
        self.root.minsize(980, 620)
        self.root.configure(bg="#f7f3ee")

        self.colors = {
            "bg": "#f7f3ee",
            "panel": "#fffdfb",
            "sidebar": "#f0e9e2",
            "sidebar_text": "#2a1f1a",
            "muted": "#6d5a52",
            "border": "#e6d9d0",
            "primary": "#9c5d4d",
            "primary_soft": "#f5e1db",
            "accent": "#e7f4eb",
            "text": "#2d241f",
            "shadow": "#d8c8be",
        }

        self.build_ui()

    def build_ui(self):
        outer = tk.Frame(self.root, bg=self.colors["bg"])
        outer.pack(fill=tk.BOTH, expand=True, padx=18, pady=18)

        self.sidebar = tk.Frame(
            outer,
            bg=self.colors["sidebar"],
            width=260,
            highlightbackground=self.colors["border"],
            highlightthickness=1,
        )
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 14))
        self.sidebar.pack_propagate(False)

        self.build_sidebar()

        self.main_panel = tk.Frame(outer, bg=self.colors["bg"])
        self.main_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.build_topbar()
        self.build_content_area()

    def build_sidebar(self):
        title = tk.Label(
            self.sidebar,
            text="Study Hub",
            bg=self.colors["sidebar"],
            fg=self.colors["sidebar_text"],
            font=("Segoe UI", 16, "bold"),
            anchor="w",
            padx=18,
            pady=12,
        )
        title.pack(fill=tk.X)

        new_note = tk.Button(
            self.sidebar,
            text="+ New study note",
            bg=self.colors["primary"],
            fg="white",
            activebackground="#87513c",
            relief="flat",
            bd=0,
            padx=16,
            pady=10,
            font=("Segoe UI", 10, "bold"),
            command=self.new_note,
        )
        new_note.pack(fill=tk.X, padx=18, pady=(0, 18))

        search = tk.Entry(
            self.sidebar,
            bg="#f8fafc",
            fg=self.colors["text"],
            font=("Segoe UI", 10),
            relief="flat",
            highlightbackground=self.colors["border"],
            highlightthickness=1,
        )
        search.insert(0, "Search topics")
        search.pack(fill=tk.X, padx=18, pady=(0, 16))

        notes = [
            "Biology recap",
            "Math exercises",
            "History summary",
            "Vocabulary",
            "Exam checklist",
        ]

        for note in notes:
            btn = tk.Button(
                self.sidebar,
                text=note,
                bg=self.colors["sidebar"],
                fg=self.colors["sidebar_text"],
                activebackground="#e8edf5",
                relief="flat",
                bd=0,
                anchor="w",
                justify="left",
                padx=18,
                pady=12,
                font=("Segoe UI", 10),
                command=lambda n=note: self.select_note(n),
            )
            btn.pack(fill=tk.X)

        info = tk.Frame(self.sidebar, bg="#f8fafc", highlightbackground=self.colors["border"], highlightthickness=1)
        info.pack(fill=tk.X, padx=18, pady=(24, 18))

        tk.Label(
            info,
            text="Today’s focus",
            bg="#f8fafc",
            fg=self.colors["muted"],
            font=("Segoe UI", 9, "bold"),
            anchor="w",
            padx=12,
            pady=6,
        ).pack(fill=tk.X)

        tk.Label(
            info,
            text="3 topics left\n2 practice sets\n1 revision goal",
            bg="#f8fafc",
            fg=self.colors["text"],
            font=("Segoe UI", 10),
            justify="left",
            padx=12,
            pady=12,
        ).pack(fill=tk.X)

    def build_topbar(self):
        topbar = tk.Frame(self.main_panel, bg=self.colors["panel"], highlightbackground=self.colors["border"], highlightthickness=1)
        topbar.pack(fill=tk.X, pady=(0, 14))

        left = tk.Frame(topbar, bg=self.colors["panel"])
        left.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=18, pady=14)

        title = tk.Label(
            left,
            text="Biology recap",
            bg=self.colors["panel"],
            fg=self.colors["text"],
            font=("Segoe UI", 20, "bold"),
            anchor="w",
        )
        title.pack(anchor="w")

        subtitle = tk.Label(
            left,
            text="Personal study assistant for revision and understanding",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 10),
            anchor="w",
        )
        subtitle.pack(anchor="w", pady=(2, 0))

        actions = tk.Frame(topbar, bg=self.colors["panel"])
        actions.pack(side=tk.RIGHT, padx=18, pady=14)

        ask_btn = tk.Button(
            actions,
            text="Explain it",
            bg=self.colors["primary_soft"],
            fg=self.colors["primary"],
            activebackground="#efd7d1",
            relief="flat",
            bd=0,
            padx=16,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            command=self.run_code,
        )
        ask_btn.pack(side=tk.LEFT)

        save_btn = tk.Button(
            actions,
            text="Save",
            bg=self.colors["panel"],
            fg=self.colors["text"],
            activebackground="#f0f4f8",
            relief="flat",
            bd=1,
            highlightbackground=self.colors["border"],
            padx=14,
            pady=8,
            font=("Segoe UI", 10),
        )
        save_btn.pack(side=tk.LEFT, padx=(8, 0))

    def build_content_area(self):
        body = tk.Frame(self.main_panel, bg=self.colors["bg"])
        body.pack(fill=tk.BOTH, expand=True)

        editor_panel = tk.Frame(
            body,
            bg=self.colors["panel"],
            highlightbackground=self.colors["border"],
            highlightthickness=1,
        )
        editor_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 12))

        editor_header = tk.Frame(editor_panel, bg=self.colors["panel"])
        editor_header.pack(fill=tk.X, padx=16, pady=(14, 8))

        tk.Label(
            editor_header,
            text="Document",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 9, "bold"),
            anchor="w",
        ).pack(anchor="w")

        self.note_title = tk.Entry(
            editor_panel,
            font=("Segoe UI", 16, "bold"),
            bg=self.colors["panel"],
            fg=self.colors["text"],
            relief="flat",
            highlightbackground=self.colors["border"],
            highlightthickness=1,
        )
        self.note_title.insert(0, "Biology recap")
        self.note_title.pack(fill=tk.X, padx=16, pady=(0, 10))

        self.editor = ScrolledText(
            editor_panel,
            wrap=tk.WORD,
            bg="#ffffff",
            fg=self.colors["text"],
            font=("Segoe UI", 12),
            padx=12,
            pady=12,
            relief="flat",
            highlightbackground=self.colors["border"],
            highlightthickness=1,
        )
        self.editor.pack(fill=tk.BOTH, expand=True, padx=16, pady=(0, 16))
        self.editor.insert(tk.END, "Cell structure and function\n\n- Cells are the basic unit of life\n- The nucleus stores genetic information\n- Mitochondria produce energy\n- Membranes control what enters and exits\n\nThis notes page helps summarize difficult content in a clear, personal study format.")

        ai_panel = tk.Frame(
            body,
            bg=self.colors["panel"],
            width=340,
            highlightbackground=self.colors["border"],
            highlightthickness=1,
        )
        ai_panel.pack(side=tk.RIGHT, fill=tk.Y)
        ai_panel.pack_propagate(False)

        ai_header = tk.Frame(ai_panel, bg=self.colors["panel"])
        ai_header.pack(fill=tk.X, padx=16, pady=(14, 8))

        tk.Label(
            ai_header,
            text="Study summary",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 9, "bold"),
            anchor="w",
        ).pack(anchor="w")

        self.output = ScrolledText(
            ai_panel,
            wrap=tk.WORD,
            state=tk.NORMAL,
            bg="#f8fafc",
            fg=self.colors["text"],
            font=("Segoe UI", 11),
            relief="flat",
            highlightbackground=self.colors["border"],
            highlightthickness=1,
            padx=12,
            pady=12,
        )
        self.output.pack(fill=tk.BOTH, expand=True, padx=16, pady=(0, 16))
        self.output.insert(
            tk.END,
            "Important idea: cells are the foundation of all living things.\n\nKey memory cue: nucleus = control center, mitochondria = energy, membrane = boundary.\n\nSuggested revision: turn this into a 3-question self-test before moving to the next topic.",
        )
        self.output.configure(state=tk.DISABLED)

        prompt = tk.Frame(ai_panel, bg=self.colors["panel"])
        prompt.pack(fill=tk.X, padx=16, pady=(0, 16))

        self.prompt_entry = tk.Entry(
            prompt,
            bg="#f8fafc",
            fg=self.colors["text"],
            relief="flat",
            highlightbackground=self.colors["border"],
            highlightthickness=1,
            font=("Segoe UI", 10),
        )
        self.prompt_entry.insert(0, "Ask for help")
        self.prompt_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))

        send_btn = tk.Button(
            prompt,
            text="Send",
            bg=self.colors["primary"],
            fg="white",
            activebackground="#1667d1",
            relief="flat",
            bd=0,
            padx=14,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            command=self.run_code,
        )
        send_btn.pack(side=tk.RIGHT)

    def new_note(self):
        self.note_title.delete(0, tk.END)
        self.note_title.insert(0, "New topic")
        self.editor.delete("1.0", tk.END)
        self.editor.insert(tk.END, "Write your notes here...\n\n- key concept\n- examples\n- questions to review")

    def select_note(self, name):
        self.note_title.delete(0, tk.END)
        self.note_title.insert(0, name)
        self.editor.delete("1.0", tk.END)
        self.editor.insert(tk.END, f"This is your notes for {name}.\n\nAdd concepts, examples, and questions to review before the next study session.")

    def run_code(self, event=None):
        prompt = self.prompt_entry.get().strip()
        content = self.editor.get("1.0", tk.END).strip()

        if prompt and prompt != "Ask for help":
            summary = f"Prompt: {prompt}\n\nStudy note: focus on the main idea first, then add a simple example and one quick test question to make it easier to remember."
        elif content:
            summary = "Main idea: simplify the topic into a few core concepts.\n\nBest next step: create 3 recall questions and review them without looking at the notes."
        else:
            summary = "No notes yet. Write a few key ideas and the app will turn them into a study summary."

        self.output.configure(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, summary)
        self.output.configure(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = NotebookApp(root)
    root.mainloop()