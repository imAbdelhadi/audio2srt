import os
import requests
from tqdm import tqdm

# Set your OpenAI API key
api_key = 'YOUR_API_KEY'

# Folder containing audio files
audio_folder = 'audio_files'
srt_folder = 'srt_files'

# Ensure the output folder exists
os.makedirs(srt_folder, exist_ok=True)

def transcribe_audio(file_path):
    url = "https://api.openai.com/v1/audio/translations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        # "Content-Type": "multipart/form-data"
    }
    files = {
        "file": open(file_path, "rb"),
        "model": (None, "whisper-1"),
        "response_format": (None, "srt")
    }
    
    response = requests.post(url, headers=headers, files=files)
    
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code} {response.text}")
    
    return response.text

def save_srt_file(srt_content, output_path):
    with open(output_path, 'w') as f:
        f.write(srt_content)

def main():
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3')] # change filetype ("flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm") 
    
    for audio_file in tqdm(audio_files, desc="Processing audio files"):
        audio_path = os.path.join(audio_folder, audio_file)
        try:
            srt_content = transcribe_audio(audio_path)
            srt_file_name = os.path.splitext(audio_file)[0] + '.srt'
            srt_path = os.path.join(srt_folder, srt_file_name)
            save_srt_file(srt_content, srt_path)
        except Exception as e:
            print(f"Error processing {audio_file}: {e}")

if __name__ == "__main__":
    main()
