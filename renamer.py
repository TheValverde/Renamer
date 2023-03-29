import os
import re
import tkinter as tk
from tkinter import filedialog, ttk

def get_prefix_suffix(filename):
    pattern = r'^(.*)_([\w-]+)_(.*)\..+$'
    match = re.match(pattern, filename)
    if match:
        return match.group(1), match.group(3)
    return None, None

def batch_rename_files(files, prefix, suffix):
    for file_path in files:
        directory, filename = os.path.split(file_path)
        current_prefix, current_suffix = get_prefix_suffix(filename)
        
        if current_prefix == prefix and current_suffix == suffix:
            print(f"Skipped {file_path} (already has the desired prefix and suffix)")
            continue

        name, ext = os.path.splitext(filename)
        new_filename = f"{prefix}_{name}_{suffix}{ext}"
        new_file_path = os.path.join(directory, new_filename)
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {new_file_path}")

def edit_prefix_suffix(files, new_prefix, new_suffix):
    for file_path in files:
        directory, filename = os.path.split(file_path)
        current_prefix, current_suffix = get_prefix_suffix(filename)

        if current_prefix == new_prefix and current_suffix == new_suffix:
            print(f"Skipped {file_path} (already has the desired prefix and suffix)")
            continue

        if current_prefix is not None and current_suffix is not None:
            name, ext = os.path.splitext(filename.split('_', 1)[-1].rsplit('_', 1)[0])
            new_filename = f"{new_prefix}_{name}_{new_suffix}{ext}"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_path} to {new_file_path}")

def browse_files():
    files = filedialog.askopenfilenames()
    files_var.set(files)

def start_editing():
    files = files_var.get().split("', '")
    files[0] = files[0].lstrip("('")
    files[-1] = files[-1].rstrip("',)")

    new_prefix = prefix_var.get()
    new_suffix = suffix_var.get()

    if files:
        edit_prefix_suffix(files, new_prefix, new_suffix)
    else:
        print("No files selected. Please try again.")

def create_widgets():
    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(main_frame, text="Selected Files:").grid(row=0, column=0, sticky="e", padx=(0, 10), pady=(0, 5))
    ttk.Button(main_frame, text="Browse", command=browse_files).grid(row=0, column=1, sticky="w", pady=(0, 5))

    ttk.Label(main_frame, text="Prefix:").grid(row=1, column=0, sticky="e", padx=(0, 10), pady=(0, 5))
    ttk.Entry(main_frame, textvariable=prefix_var).grid(row=1, column=1, sticky="w", pady=(0, 5))

    ttk.Label(main_frame, text="Suffix:").grid(row=2, column=0, sticky="e", padx=(0, 10), pady=(0, 5))
    ttk.Entry(main_frame, textvariable=suffix_var).grid(row=2, column=1, sticky="w", pady=(0, 5))

    ttk.Button(main_frame, text="Rename", command=start_editing).grid(row=3, column=0, columnspan=2, pady=(10, 0))

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)

def apply_dark_theme():
    style = ttk.Style()

    # Configure the dark theme colors and settings
    style.configure("TButton", foreground="grey", background="#2d2d2d", relief="flat")
    style.map("TButton", background=[("active", "#4a4a4a"), ("pressed", "#212121")])
    style.configure("TEntry", fieldbackground="#2d2d2d", background="#2d2d2d", foreground="grey")
    style.configure("TLabel", background="#2d2d2d", foreground="grey")
    style.configure("TFrame", background="#2d2d2d")

    # Apply the theme to the root window
    root.configure(background="#2d2d2d")

root = tk.Tk()
root.title("Batch Rename Files")

files_var = tk.StringVar()
prefix_var = tk.StringVar()
suffix_var = tk.StringVar()

create_widgets()
apply_dark_theme()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()