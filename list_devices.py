#!/usr/bin/env python

import pyaudio

def list_devices():
    p = pyaudio.PyAudio()
    device_count = p.get_device_count()

    for i in range(0, device_count):
        info = p.get_device_info_by_index(i)
        print(f"Device {i}:")
        print(f"  Name: {info['name']}")
        print(f"  Index: {info['index']}")
        print(f"  Max Input Channels: {info['maxInputChannels']}")
        print(f"  Max Output Channels: {info['maxOutputChannels']}")
        print(f"  Default Sample Rate: {info['defaultSampleRate']}")
        print("-" * 20)  
    p.terminate()

list_devices()
