import tkinter as tk
import tkinter.filedialog as fd
import tkinter.simpledialog as sd
import json
import os
import subprocess


class ExeLibrary:
    def __init__(self, master):
        self.master = master
        master.title("ExeLib - Библиотека для exe-файлов")
        master.geometry("715x400")

        # Создаем фрейм для кнопок и список
        button_frame = tk.Frame(master, bg="#2c3e50")
        button_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

        self.listbox = tk.Listbox(master, width=50, height=20, bg="#ecf0f1", font=("Arial", 12))
        self.listbox.pack(padx=10, pady=0, fill=tk.BOTH, expand=True)

        add_button = tk.Button(button_frame, text="Добавить", width=17, bg="#3498db", fg="white", command=self._add_path)
        add_button.pack(side=tk.LEFT, padx=5, pady=5)

        remove_button = tk.Button(button_frame, text="Удалить", width=17, bg="#e74c3c", fg="white", command=self._remove_path)
        remove_button.pack(side=tk.LEFT, padx=5, pady=5)

        rename_button = tk.Button(button_frame, text="Переименовать", width=17, bg="#f1c40f", fg="white", command=self._rename_path)
        rename_button.pack(side=tk.LEFT, padx=5, pady=5)

        run_button = tk.Button(button_frame, text="Запустить", width=17, bg="#2ecc71", fg="white", command=self._run_path)
        run_button.pack(side=tk.LEFT, padx=5, pady=5)

        save_button = tk.Button(button_frame, text="Сохранить", width=17, bg="#34495e", fg="white", command=self._save_paths)
        save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self._load_paths()

    def _add_path(self):
        file_path = fd.askopenfilename(title="Выберите exe-файл", filetypes=(("Executable files", "*.exe"),))
        if file_path:
            name = sd.askstring("Введите название", "Введите название файла:")
            if name:
                self.listbox.insert(tk.END, (name, file_path))

    def _remove_path(self):
        selection = self.listbox.curselection()
        if selection:
            self.listbox.delete(selection)

    def _rename_path(self):
        selection = self.listbox.curselection()
        if selection:
            old_name, old_path = self.listbox.get(selection[0])
            new_name = sd.askstring("Введите новое название", f"Введите новое название для {old_name}:")
            if new_name:
                new_path = fd.askopenfilename(initialdir=old_path, title="Выберите exe-файл", filetypes=(("Executable files", "*.exe"),))
                if new_path:
                    self.listbox.delete(selection)
                    self.listbox.insert(selection[0], (new_name, new_path))

    def _run_path(self):
        selection = self.listbox.curselection()
        if selection:
            _, file_path = self.listbox.get(selection[0])
            file_dir = os.path.dirname(file_path)
            subprocess.run(['cmd', '/c', 'start', '/wait', file_path], cwd=file_dir, shell=True)

    def _save_paths(self):
        with open("paths.json", "w") as f:
            json.dump(self.listbox.get(0, tk.END), f)

    def _load_paths(self):
        try:
            with open("paths.json", "r") as f:
                paths = json.load(f)
                for path in paths:
                    self.listbox.insert(tk.END, tuple(path))
        except FileNotFoundError:
            pass

root = tk.Tk()
app = ExeLibrary(root)
root.mainloop()
