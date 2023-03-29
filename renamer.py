import os
import re
import tkinter as tk
from tkinter import filedialog

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

root = tk.Tk()
root.title("Batch Rename Files")

files_var = tk.StringVar()
prefix_var = tk.StringVar()
suffix_var = tk.StringVar()

tk.Label(root, text="Selected Files:").grid(row=0, column=0, sticky="e")
tk.Button(root, text="Browse", command=browse_files).grid(row=0, column=1)

tk.Label(root, text="Prefix:").grid(row=1, column=0, sticky="e")
tk.Entry(root, textvariable=prefix_var).grid(row=1, column=1)

tk.Label(root, text="Suffix:").grid(row=2, column=0, sticky="e")
tk.Entry(root, textvariable=suffix_var).grid(row=2, column=1)

tk.Button(root, text="Rename", command=start_editing).grid(row=3, column=0, sticky="e")


root.mainloop()