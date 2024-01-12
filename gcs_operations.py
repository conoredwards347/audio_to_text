# gcs_operations.py

from header import *

def upload_to_gcs(local_file_path, bucket_name):
    # Initialise the GCS client
    storage_client = storage.Client()

    # Extract the file name from the local file path
    file_name = os.path.basename(local_file_path)

    # Create a GCS blob object
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Upload the file to GCS
    blob.upload_from_filename(local_file_path)

    # Return the GCS URI
    return f"gs://{bucket_name}/{file_name}", file_name

def delete_from_gcs(bucket_name, file_name):
    # Initialise the GCS client
    storage_client = storage.Client()

    # Create a GCS blob object
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Attempt to delete the file from GCS
    try:
        blob.delete()
    except Forbidden as e:
        messagebox.showerror("Permission Error", "Access denied: Cannot delete file from GCS. Check permissions.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while deleting the file: {e}")
