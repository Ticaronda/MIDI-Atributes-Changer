import tkinter as tk
from tkinter import filedialog
import mido

def import_midi():
    def initFile():
        file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.mid")])
        if file_path:
            print("MIDI file loaded successfully!")
            return file_path
        else:
            print('Error Loading File')

    mid = mido.MidiFile(initFile())

    # Find Key Sig
    key_signature = None
    for track in mid.tracks:
        for message in track:
            if message.is_meta and message.type == 'key_signature':
                key_signature = message
                break
        if key_signature:
            break

    key = None
    if key_signature:
        key = key_signature.key
        print("Key:", key)
    else:
        print("No key signature found in the MIDI file")

    # Find Tempo
    tempo = None
    for track in mid.tracks:
        for message in track:
            if message.is_meta and message.type == 'set_tempo':
                tempo = message
                break
        if tempo:
            break

    if tempo:
        tempo = tempo.tempo
        bpm = mido.tempo2bpm(tempo)
        print("Tempo:", bpm)
    else:
        print("No tempo found in the MIDI file")

    # Find Time Sig
    time_signature = None
    for track in mid.tracks:
        for message in track:
            if message.is_meta and message.type == 'time_signature':
                time_signature = message
                break
        if time_signature:
            break

    if time_signature:
        time_signature = f"{time_signature.numerator}/{time_signature.denominator}"
        print("Time Signature:", time_signature)
    else:
        print("No time signature found in the MIDI file")

# Top level window
frame = tk.Tk()
frame.title("MIDI Atributes Changer")
frame.geometry('350x465')

# Title
mainTitle = tk.Label(frame, 
text = "MIDI Atributes Changer",
font = ("Arial bold", 14)
)
mainTitle.place(
    x = 0,
    y = 0
)

importButton = tk.Button(frame,
text = 'Import',
font = ("Arial", 12),
width = 12,
bg = ("#e1eaf2"),
command = import_midi)
importButton.place(
    x=0,
    y=100
)

# BPM Input Title
bgColourTitle = tk.Label(frame,
text = "BPM: ",
font = ("Arial", 12)
)
bgColourTitle.place(
    x = 0,
    y = 30
)

# BPM Input
BPMInput = tk.Text(frame,
    height = 1,
    width = 20)
BPMInput.place(
    x = 0,
    y = 60
)

frame.mainloop()