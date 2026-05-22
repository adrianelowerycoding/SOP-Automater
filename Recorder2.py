import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import subprocess


# Setting working directory
os.chdir(r"C:\Users\adrian.lowery\python-scripts\src\Big Projects\SOP Automator")
print(os.getcwd())

frames = []
isRecording = False
fs = 16000
sd.default.samplerate = fs 

# Python builds this function. It's not called yet. 
# We're ignoring some of the parameters, but we still have include them in the signature. 
def callback(indata, frames_count, time, status): 
    if isRecording:
        frames.append(indata.copy()) # Creates a separate copy of the audio chunk data.

# Does not call callback function. Registers it with the audio system. It sets up the microphone pipeline. 
stream = sd.InputStream(callback=callback, samplerate=fs, channels=1) 

input("Press ENTER to start recording\n")
isRecording = True
# Callback function is called here by the audio backend (C code). 
# Data is collected around 20-100 times per second.
stream.start()

input("Press Enter to stop recording...\n")
isRecording = False
# Callback function stops being called. 
stream.stop()
stream.close()

audio = np.concatenate(frames, axis=0)

# Play the audio back 
sd.play(audio, fs)
sd.wait()

# The user should be able to choose the name.
fileName = input("Name sound file: ").strip()
# Adding consistent end to the name
if not fileName.endswith(".wav"):
    fileName += ".wav"
# Creating the file
wav.write(fileName, fs, audio)

# Starting Whisper script and passing wav file to it
subprocess.run(["python", "Whisper.py", fileName])










