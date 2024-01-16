import tkinter as tk
from tkinter import filedialog
import zipfile
import os

def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def get_zip_file():
    zip_file_path = filedialog.askopenfilename(title="Select Zip File", filetypes=[("Zip files", "*.zip")])
    zip_entry.delete(0, tk.END)
    zip_entry.insert(0, zip_file_path)

def get_extract_location():
    extract_location = filedialog.askdirectory(title="Select Extract Location")
    extract_entry.delete(0, tk.END)
    extract_entry.insert(0, extract_location)

def unzip_and_save():
    zip_path = zip_entry.get()
    extract_path = extract_entry.get()

    if not zip_path or not extract_path:
        status_label.config(text="Please provide both zip file and extract location.")
        return

    try:
        unzip_file(zip_path, extract_path)
        status_label.config(text="Unzipping complete!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Zip File Unzipper")

# Zip file entry
zip_label = tk.Label(root, text="Select Zip File:")
zip_label.pack(pady=10)
zip_entry = tk.Entry(root, width=40)
zip_entry.pack(pady=5)
zip_button = tk.Button(root, text="Browse", command=get_zip_file)
zip_button.pack(pady=10)

# Extract location entry
extract_label = tk.Label(root, text="Select Extract Location:")
extract_label.pack(pady=10)
extract_entry = tk.Entry(root, width=40)
extract_entry.pack(pady=5)
extract_button = tk.Button(root, text="Browse", command=get_extract_location)
extract_button.pack(pady=10)

# Unzip button
unzip_button = tk.Button(root, text="Unzip and Save", command=unzip_and_save)
unzip_button.pack(pady=20)

# Status label
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
