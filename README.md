# Audio to SRT Transcription Script using OpenAI Whisper

This script transcribes audio files in a specified folder to SRT (subtitle) format using the OpenAI Whisper API. The script processes multiple audio files and saves the transcriptions in a specified output folder.

## Prerequisites

- Python 3.6 or higher
- `requests` library
- `tqdm` library
- OpenAI API key

## Installation

1. Clone the repository or download the script file.
2. Install the required Python libraries using pip:

```bash
pip install requests tqdm
```

3. Obtain an OpenAI API key by signing up at [OpenAI](https://www.openai.com/).

## Setup

1. Save your OpenAI API key in the script by replacing `'YOUR_API_KEY'` with your actual API key.
2. Ensure you have a folder containing your audio files. The default folder name is `audio_files`, but you can change this in the script if needed.
3. Ensure the output folder (`srt_files`) exists or will be created by the script.

## Usage

1. Place your audio files in the specified input folder (`audio_files` by default). Supported audio file formats include `flac`, `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `ogg`, `wav`, and `webm`.
2. Chnage audio type on the line 39.
3. Run the script:

```bash
python audio2srt.py
```

The script will process each audio file in the input folder, transcribe it using the OpenAI API, and save the resulting SRT file in the output folder (`srt_files` by default).


## Notes

- Ensure you have a stable internet connection while running the script, as it communicates with the OpenAI API.
- Handle your API key with care. Avoid sharing or exposing it in public repositories.

