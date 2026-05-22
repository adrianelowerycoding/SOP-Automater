import sounddevice as sd

duration = 2 # 10 seconds
fs = 16000 # audio samples per second
sd.default.samplerate = fs
sd.default.channels = 1

recording = sd.rec(int(duration * fs)) # Records an array of audio samples
sd.wait() # waits until recording finishes to run code below

sd.play(recording, fs)
sd.wait() # waits until playback finishes before finishing and shutting script

""" print(sd.default.device) # Tells you what your default input, output devices are 
print(sd.query_devices()) # Gives list of all your possible IO devices """













