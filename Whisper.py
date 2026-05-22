import sys
import subprocess
from faster_whisper import WhisperModel

fileName = sys.argv[1] # what does this do? 

model = WhisperModel("base")  # or "small" for better accuracy
segments, info = model.transcribe(fileName)

print("Language:", info.language)

for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

