# MP3 to Text Transcription Tool

## Description
This Python application uses Google Cloud's Speech-to-Text API to transcribe audio from MP3 files. The application is designed with a modular architecture and provides a graphical user interface (GUI) for easy user interaction.

## Key Features
- **Transcription of MP3 Files**: Uses Google Cloud Speech-to-Text API for accurate and efficient transcription.
- **Modular Design**: The code is organized into separate modules for specific functionalities - Google Cloud Storage operations, transcription process handling, and the GUI.
- **User-Friendly GUI**: A simple Tkinter-based interface for selecting MP3 files, specifying Google Cloud Storage bucket details, and choosing output locations for transcriptions.
- **Robust Error Handling**: Includes comprehensive error handling, especially for Google Cloud Storage operations and during the transcription process.

## Modules
- `header.py`: Common imports and configurations for the application.
- `gcs_operations.py`: Functions for uploading to and deleting files from Google Cloud Storage.
- `transcription.py`: Handles the transcription of audio files using the Google Cloud Speech-to-Text API.
- `gui.py`: Manages the Tkinter-based graphical user interface.
- `main.py`: The main entry point of the application, integrating all other modules.

## Setup and Installation
1. Ensure Python 3.x is installed.
2. Install required packages: `pip install google-cloud-storage google-cloud-speech tkinter`.
3. Clone the repository: `git clone https://github.com/conoredwards347/mp3_to_text.git`.
4. Navigate to the project directory and run `main.py`.

## Usage
Run `main.py` to start the application. The GUI will guide you through selecting an MP3 file, inputting necessary Google Cloud Storage details, and choosing where to save the transcription.

## Contributions
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under [https://creativecommons.org/publicdomain/zero/1.0/deed.en].

For more details, refer to the LICENSE file in the repository.
