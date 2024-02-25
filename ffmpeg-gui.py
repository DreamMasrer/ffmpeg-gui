#Hello, this is my ffmpeg Python script with GUI

import tkinter as tk
from tkinter import filedialog
import os
import subprocess

def convert_mp4_to_mov(source_dir, destination_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Convert mp4 files to mov and move to destination directory
    for file in os.listdir(source_dir):
        if file.endswith(".mp4"):
            filename_noext = os.path.splitext(file)[0]
            subprocess.run(['ffmpeg', '-i', os.path.join(source_dir, file), '-c:v', 'prores', '-c:a', 'pcm_s16le', os.path.join(destination_dir, f"{filename_noext}.mov")])

    print("Conversion and moving complete.")

def select_source_dir():
    source_dir = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_dir)

def select_destination_dir():
    destination_dir = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, destination_dir)

def convert():
    source_dir = source_entry.get()
    destination_dir = destination_entry.get()
    convert_mp4_to_mov(source_dir, destination_dir)

# GUI setup
root = tk.Tk()
root.title("MP4 to MOV Converter")

# Source directory selection
source_label = tk.Label(root, text="Source Directory:")
source_label.grid(row=0, column=0, padx=5, pady=5)
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=5, pady=5)
source_button = tk.Button(root, text="Select", command=select_source_dir)
source_button.grid(row=0, column=2, padx=5, pady=5)

# Destination directory selection
destination_label = tk.Label(root, text="Destination Directory:")
destination_label.grid(row=1, column=0, padx=5, pady=5)
destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=1, column=1, padx=5, pady=5)
destination_button = tk.Button(root, text="Select", command=select_destination_dir)
destination_button.grid(row=1, column=2, padx=5, pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
