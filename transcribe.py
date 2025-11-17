import whisper

# Load the small model
model = whisper.load_model("small")

# Path to your audio file
audio_path = r"C:\Users\prasann\Downloads\Transcribe\india_1.mp3"

# Transcribe and translate Hindi to English automatically
result = model.transcribe(audio_path, task="translate")

# Save transcript with timestamps
with open("transcript-india_1-english.txt", "w", encoding="utf-8") as f:
    for i, segment in enumerate(result["segments"]):
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]

        # Write SRT-like format
        f.write(f"{i+1}\n")
        f.write(f"{start:.2f} --> {end:.2f}\n")
        f.write(f"{text}\n\n")

print("\n✅ Transcription with timestamps completed!")
print("Saved as transcript-india_1-english.txt")
