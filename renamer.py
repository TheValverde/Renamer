import os
import tkinter as tk
from tkinter import filedialog

def batch_rename_files(files, prefix, suffix):
    for file_path in files:
        file_path = file_path.strip("('")  # Remove unnecessary characters
        file_path = file_path.rstrip("',")  # Remove trailing characters
        directory, filename = os.path.split(file_path)
        filename, ext = os.path.splitext(filename)
        new_filename = f"{prefix}_{filename}_{suffix}{ext}"
        new_file_path = os.path.join(directory, new_filename)
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {new_file_path}")

def edit_prefix_suffix(files, new_prefix, new_suffix):
    for file_path in files:
        directory, filename = os.path.split(file_path)
        parts = filename.split("_")
        if len(parts) > 2:
            current_prefix, name, current_suffix_ext = parts[0], parts[1], '_'.join(parts[2:])
            current_suffix, ext = os.path.splitext(current_suffix_ext)
            new_filename = f"{new_prefix}_{name}_{new_suffix}{ext}"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_path} to {new_file_path}")
  
def start_editing():
    print("Starting editing...")
    raw_file_paths = files_var.get()
    files = raw_file_paths.split("', '")  # Split the paths using the custom delimiter
    files[0] = files[0].lstrip("('")  # Remove leading characters from the first file path
    files[-1] = files[-1].rstrip("',)")  # Remove trailing characters from the last file path

    new_prefix = prefix_var.get()
    new_suffix = suffix_var.get()

    if files:
        edit_prefix_suffix(files, new_prefix, new_suffix)
    else:
        print("No files selected. Please try again.")

            
def browse_files():
    files = filedialog.askopenfilenames()
    files_var.set(files)

def start_renaming():
    print("Starting renaming...")
    raw_file_paths = files_var.get()
    files = raw_file_paths.split("', '")  # Split the paths using the custom delimiter
    files[0] = files[0].lstrip("('")  # Remove leading characters from the first file path
    files[-1] = files[-1].rstrip("',)")  # Remove trailing characters from the last file path

    prefix = prefix_var.get()
    suffix = suffix_var.get()

    if files:
        batch_rename_files(files, prefix, suffix)
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


tk.Button(root, text="Edit Prefix/Suffix", command=start_editing).grid(row=3, column=2)

tk.Button(root, text="Start Renaming", command=start_renaming).grid(row=3, column=1)

root.mainloop()
