# transcription.py

from header import *
from gcs_operations import delete_from_gcs
import gcs_operations

def transcribe_file(gcs_uri, output_path, bucket_name, file_name):
    # Initialise the Google Speech Client
    client = speech_v1.SpeechClient()

    # Configure the GCS URI for the API
    audio = speech_v1.RecognitionAudio(uri=gcs_uri)
    config = speech_v1.RecognitionConfig(
        encoding=speech_v1.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=48000,  # Adjust to your file's sample rate
        language_code='en-US'
    )

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
    delete_from_gcs(bucket_name, file_name)
