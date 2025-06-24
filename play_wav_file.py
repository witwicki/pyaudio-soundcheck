#!/usr/bin/env python

import sys
import pyaudio
import wave


def get_device_name(pyaudio_object, device_index):
    return pyaudio_object.get_device_info_by_index(device_index)['name']


def play_wav_file(filename, device_index=-1):
    """Plays a WAV file."""

    # Open the WAV file
    wf = wave.open(filename, 'rb')

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output_device_index=device_index,
                    output=True)

    # Read data in chunks
    data = wf.readframes(1024)

    # Announce
    device_name = get_device_name(p,device_index) if (device_index >= 0) else "default output device"
    print(f"\nPlaying {filename} on {device_name}... ")

    # Play the sound by writing the audio data to the stream
    while data != b'':
        stream.write(data)
        data = wf.readframes(1024)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()

    # Terminate the PortAudio interface
    p.terminate()

    print("...done.")


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print(f"\nUSAGE:  {sys.argv[0]} <path/to/wave_file.wav> [<audio_output_device_index>]\n") 
    else:
        filename = sys.argv[1]
        if len(sys.argv) < 3:
            play_wav_file(filename)
        else:
            
            play_wav_file(filename, device_index=int(sys.argv[2]))

    
