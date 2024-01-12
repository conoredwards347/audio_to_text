# gui.py

from header import *
import gcs_operations
import transcription
import tkinter.filedialog as filedialog
import tkinter.simpledialog as simpledialog

def select_file(root):
    # Dialog to select local MP3 file
    local_file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if local_file_path:
        # Dialog to input GCS Bucket name
        bucket_name = simpledialog.askstring("Enter GCS Bucket Name", "Enter the name of your GCS Bucket:", parent=root)
        if bucket_name:
            # Upload the file to GCS
            gcs_uri, file_name = gcs_operations.upload_to_gcs(local_file_path, bucket_name)

            # Dialog to choose where to save the transcription
            output_path = filedialog.askdirectory()
            if output_path:
                transcription.transcribe_file(gcs_uri, output_path, bucket_name, file_name)

def setup_gui():
    root = tk.Tk()
    root.title("Speech to Text Transcription Tool")
    root.geometry("400x200")
    tk.Button(root, text="Select MP3 and Transcribe", command=lambda: select_file(root)).pack(expand=True, padx=20, pady=20)
    return root