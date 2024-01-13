# transcription.py

from google.cloud import speech_v1
from google.cloud.speech_v1 import RecognitionConfig
import gcs_operations
import tkinter.messagebox as messagebox
from pydub.utils import mediainfo
import os

def get_sample_rate(audio_file_path):
    # Use pydub to analyze the audio file and extract sample rate
    info = mediainfo(audio_file_path)
    return int(info['sample_rate'])

def transcribe_file(gcs_uri, output_path, bucket_name, file_name, local_file_path, file_type):
    # Determine the sample rate of the audio file
    sample_rate_hertz = get_sample_rate(local_file_path)

    # Set the correct encoding based on file type
    encoding = speech_v1.RecognitionConfig.AudioEncoding.MP3 if file_type == "MP3" else speech_v1.RecognitionConfig.AudioEncoding.AAC

    config = speech_v1.RecognitionConfig(
        encoding=encoding,
        sample_rate_hertz=sample_rate_hertz,
        language_code='en-US'
    )

    # Initialize the Google Speech Client
    client = speech_v1.SpeechClient()

    # Configure the GCS URI for the API
    audio = speech_v1.RecognitionAudio(uri=gcs_uri)

    # Asynchronously send the GCS URI of the audio file to the API for transcription
    operation = client.long_running_recognize(config=config, audio=audio)

    try:
        response = operation.result(timeout=180)  # Increased to 180 seconds
    except TimeoutError:
        messagebox.showerror("Timeout Error", "Transcription timed out. Please try again.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return

    # Process the response and compile the transcription
    transcription = ''
    for result in response.results:
        transcription += result.alternatives[0].transcript

    # Determine the filename for the output
    output_filename = os.path.basename(gcs_uri).split('.')[0] + "-Transcription.txt"
    output_file = os.path.join(output_path, output_filename)
    
    # Save the transcription to a file
    with open(output_file, 'w') as file:
        file.write(transcription)
    
    # Notify the user that transcription is complete
    messagebox.showinfo("Transcription Complete", f"Transcription of {output_filename} is complete.")

    # Delete the file from GCS after transcription is complete
    gcs_operations.delete_from_gcs(bucket_name, file_name)
