import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

from organizer import organize_folder


class SmartFileOrganizerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Smart File Organizer")
        self.window.geometry("650x560")
        self.window.resizable(False, False)
        self.window.configure(bg="#f4f6f8")

        self.selected_folder = ""

        self.title_label = tk.Label(
            self.window,
            text="📂 Smart File Organizer",
            font=("Arial", 24, "bold"),
            bg="#f4f6f8",
            fg="#1f2937"
        )
        self.title_label.pack(pady=25)

        self.subtitle_label = tk.Label(
            self.window,
            text="Organize your files by category with one click.",
            font=("Arial", 12),
            bg="#f4f6f8",
            fg="#6b7280"
        )
        self.subtitle_label.pack()

        self.folder_label = tk.Label(
            self.window,
            text="No folder selected.",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#374151",
            wraplength=560,
            padx=15,
            pady=12
        )
        self.folder_label.pack(pady=20, ipadx=10, ipady=5)

        self.select_button = tk.Button(
            self.window,
            text="📁 Select Folder",
            command=self.select_folder,
            width=22,
            height=2,
            bg="#2563eb",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat"
        )
        self.select_button.pack(pady=5)

        self.organize_button = tk.Button(
            self.window,
            text="🚀 Organize Files",
            command=self.organize,
            width=22,
            height=2,
            bg="#16a34a",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat"
        )
        self.organize_button.pack(pady=10)

        self.progress = ttk.Progressbar(
            self.window,
            orient="horizontal",
            length=500,
            mode="determinate"
        )
        self.progress.pack(pady=10)

        self.result_box = tk.Text(
            self.window,
            height=11,
            width=70,
            state="disabled",
            font=("Consolas", 10),
            bg="#111827",
            fg="#e5e7eb",
            relief="flat"
        )
        self.result_box.pack(pady=15)

    def select_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=folder)

    def organize(self):
        if not self.selected_folder:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return

        self.progress["value"] = 20
        self.window.update_idletasks()

        moved, log_file = organize_folder(self.selected_folder)

        self.progress["value"] = 100
        self.window.update_idletasks()

        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)

        self.result_box.insert(
            tk.END,
            f"✅ Organization completed.\n\n"
        )

        self.result_box.insert(
            tk.END,
            f"Total moved files: {len(moved)}\n\n"
        )

        if moved:
            for item in moved:
                self.result_box.insert(tk.END, f"✔ {item}\n")
        else:
            self.result_box.insert(tk.END, "No files found to organize.\n")

        self.result_box.insert(
            tk.END,
            f"\n📄 Log saved:\n{log_file}\n"
        )

        self.result_box.config(state="disabled")

    def run(self):
        self.window.mainloop()