import tkinter as tk
from tkinter import filedialog, messagebox

from organizer import organize_folder


class SmartFileOrganizerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("📂 Smart File Organizer")
        self.window.geometry("560x520")
        self.window.resizable(False, False)

        self.selected_folder = ""

        tk.Label(
            self.window,
            text="Smart File Organizer",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        self.folder_label = tk.Label(
            self.window,
            text="Henüz klasör seçilmedi.",
            wraplength=500
        )
        self.folder_label.pack(pady=10)

        tk.Button(
            self.window,
            text="📁 Klasör Seç",
            command=self.select_folder,
            width=24,
            height=2
        ).pack(pady=10)

        tk.Button(
            self.window,
            text="🚀 Organize Et",
            command=self.organize,
            width=24,
            height=2
        ).pack(pady=5)

        self.result_box = tk.Text(
            self.window,
            height=12,
            width=60,
            state="disabled",
            font=("Consolas", 11)
        )
        self.result_box.pack(pady=20)

    def select_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=folder)

    def organize(self):
        if not self.selected_folder:
            messagebox.showwarning("Uyarı", "Önce bir klasör seç.")
            return

        moved, log_file = organize_folder(self.selected_folder)

        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)

        self.result_box.insert(
            tk.END,
            f"Toplam {len(moved)} dosya organize edildi.\n\n"
        )

        if moved:
            for item in moved:
                self.result_box.insert(tk.END, f"✔ {item}\n")
        else:
            self.result_box.insert(tk.END, "Taşınacak dosya bulunamadı.\n")

        self.result_box.insert(
            tk.END,
            f"\n📄 Log kaydedildi:\n{log_file}\n"
        )

        self.result_box.config(state="disabled")

    def run(self):
        self.window.mainloop()