# Transcription Tool

## Description
This Python application uses Google Cloud's Speech-to-Text API to transcribe audio from MP3 and M4A files.

## Key Features
- **Transcription of MP3 and M4A Files**: Uses Google Cloud Speech-to-Text API for accurate and efficient transcription of both MP3 and M4A file formats.
- **User-Friendly GUI**: A simple Tkinter-based interface allows users to select MP3 or M4A files, specify Google Cloud Storage bucket details, choose output locations for transcriptions, and save bucket names for future use.
- **Robust Error Handling**: Comprehensive error handling, especially for Google Cloud Storage operations and during the transcription process.

## Modules
- `header.py`: Common imports and configurations for the application.
- `gcs_operations.py`: Functions for uploading to and deleting files from Google Cloud Storage.
- `transcription.py`: Handles the transcription of audio files using the Google Cloud Speech-to-Text API.
- `gui.py`: Manages the Tkinter-based graphical user interface, with enhanced functionality for user interaction.
- `main.py`: The main entry point of the application, integrating all other modules.

## Setup and Installation
1. Ensure Python 3.x is installed.
2. Install required packages: `pip install google-cloud-storage google-cloud-speech pydub ttkthemes`.
3. Clone the repository: `git clone -b master https://github.com/conoredwards347/audio_to_text.git`.
4. Navigate to the project directory and run `main.py`.

## Usage
Run `main.py` to start the application. The GUI will guide you through selecting an MP3 or M4A file, inputting necessary Google Cloud Storage details, and choosing where to save the transcription. You can also save and select GCS bucket names for ease of future use.

## Contributions
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under [https://creativecommons.org/publicdomain/zero/1.0/deed.en].

For more details, refer to the LICENSE file in the repository.
