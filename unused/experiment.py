from openai import OpenAI

client = OpenAI()
audio_file= open("audios/sample.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-transcribe", 
    file=audio_file
)

print(transcription.text)