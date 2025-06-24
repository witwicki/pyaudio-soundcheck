#!/usr/bin/env python

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
DURATION = 3 # seconds

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print(f"Recording for {DURATION} seconds...")

frames = []
seconds = 3
for i in range(0, int(RATE / CHUNK * seconds)):
    data = stream.read(CHUNK)
    frames.append(data)

print("...recording stopped")

stream.stop_stream()
stream.close()

print("Playing back...")

stream = p.open(format=FORMAT,
                channels=1,
                rate=RATE,
                output=True)

for data in frames:
    stream.write(data)

stream.stop_stream()
stream.close()

p.terminate()
