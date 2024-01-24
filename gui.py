# gui.py
import tkinter as tk
from tkinter import filedialog, simpledialog, ttk, messagebox
from ttkthemes import ThemedTk
import gcs_operations
import transcription

BUCKET_NAME_FILE = "bucket_names.txt"

def save_bucket_name(bucket_name):
    with open(BUCKET_NAME_FILE, "a") as file:
        file.write(bucket_name + "\n")

def load_bucket_names():
    try:
        with open(BUCKET_NAME_FILE, "r") as file:
            return [name.strip() for name in file.readlines()]
    except FileNotFoundError:
        return []

def prompt_bucket_name(root, bucket_names):
    def save_name():
        new_name = name_var.get()
        if new_name and new_name not in bucket_names:
            save_bucket_name(new_name)
            bucket_names.append(new_name)
            name_dropdown['values'] = bucket_names
            messagebox.showinfo("Saved", "Bucket name saved.")
        elif new_name:
            messagebox.showerror("Duplicate", "This bucket name already exists.")

    def submit_name():
        selected_name = name_var.get()
        if selected_name:
            top.destroy()
            return selected_name

    top = tk.Toplevel(root)
    top.title("Enter GCS Bucket Name")

    name_var = tk.StringVar()
    name_dropdown = ttk.Combobox(top, textvariable=name_var, values=bucket_names)
    name_dropdown.pack(padx=20, pady=5)

    save_button = tk.Button(top, text="Save Bucket Name", command=save_name)
    save_button.pack(side=tk.LEFT, padx=10, pady=5)

    submit_button = tk.Button(top, text="Submit", command=submit_name)
    submit_button.pack(side=tk.RIGHT, padx=10, pady=5)

    top.transient(root)  # Make the new window stay on top of the root window
    return name_var, top

def select_file(root, bucket_names, file_type):
    file_types = [("MP3 files", "*.mp3")] if file_type == "MP3" else [("M4A files", "*.m4a")]
    local_file_path = filedialog.askopenfilename(filetypes=file_types)
    
    if local_file_path:
        name_var, top_level_window = prompt_bucket_name(root, bucket_names)
        root.wait_window(top_level_window)  # Wait for the top-level window to close

        bucket_name = name_var.get()
        if bucket_name:
            gcs_uri, file_name = gcs_operations.upload_to_gcs(local_file_path, bucket_name)
            output_path = filedialog.askdirectory()
            if output_path:
                transcription.transcribe_file(gcs_uri, output_path, bucket_name, file_name, local_file_path, file_type)

def setup_gui():
    root = ThemedTk(theme="equilux")
    root.title("Speech to Text Transcription Tool")
    root.geometry("500x350")

    # Set the background color to a dark shade
    dark_background = "#383838"
    light_text = "#ffffff"
    dark_button = "#2f2f2f"

    # Apply the dark theme to the root window
    root.configure(background=dark_background)

    # Configure style for ttk elements
    style = ttk.Style(root)
    style.theme_use("equilux")  # Use the Equilux theme if installed

    # Style configuration for ttk widgets to match the dark theme
    style.configure('TFrame', background=dark_background)
    style.configure('TButton', background=dark_button, foreground=light_text)
    style.configure('TLabel', background=dark_background, foreground=light_text)
    style.configure('TEntry', fieldbackground=dark_background, foreground=light_text)
    style.configure('TCombobox', fieldbackground=dark_background, foreground=light_text)
    style.configure('Horizontal.TScale', background=dark_background)

    # Map style for active and disabled states of the widgets
    style.map('TButton', background=[('active', dark_button), ('disabled', dark_background)], foreground=[('active', light_text), ('disabled', light_text)])
    style.map('TEntry', fieldbackground=[('disabled', dark_background)], foreground=[('disabled', light_text)])
    style.map('TCombobox', fieldbackground=[('readonly', dark_background)], foreground=[('readonly', light_text)])
    style.map('Horizontal.TScale', troughcolor=[('disabled', dark_background)])

    # Load bucket names for the dropdown
    bucket_names = load_bucket_names()

    # Header Frame
    header_frame = tk.Frame(root, background=dark_background)
    header_frame.pack(fill=tk.X, pady=10)
    header_label = tk.Label(header_frame, text="Transcription Tool", font=('Helvetica', 14, 'bold'), bg=dark_background, fg=light_text)
    header_label.pack()

    # Content Frame
    content_frame = tk.Frame(root, background=dark_background)
    content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    # Dropdown for file type
    file_type_label = tk.Label(content_frame, text="Select File Type:", background=dark_background, foreground=light_text)
    file_type_label.pack()
    file_type = tk.StringVar(value="MP3")
    file_type_dropdown = ttk.Combobox(content_frame, textvariable=file_type, values=["MP3", "M4A"], background=dark_background, foreground=light_text)
    file_type_dropdown.pack(pady=5)

    # Button to select file and transcribe
    transcribe_button = ttk.Button(content_frame, text="Select File and Transcribe", style='TButton', command=lambda: select_file(root, bucket_names, file_type.get()))
    transcribe_button.pack(pady=20)

    return root

if __name__ == "__main__":
    app_root = setup_gui()
    app_root.mainloop()
