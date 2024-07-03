import os
import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize Pygame mixer
pygame.mixer.init()

# Initialize the main window
root = tk.Tk()
root.title("Music Player")
root.geometry("400x200")

# Global variable to store the currently playing music
current_music = None

def load_music():
    global current_music
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        current_music = file_path
        pygame.mixer.music.load(current_music)
        pygame.mixer.music.play(loops=0)
        song_title.config(text=os.path.basename(current_music))

def play_music():
    if current_music:
        pygame.mixer.music.play(loops=0)

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

# Add buttons and labels to the main window
load_button = tk.Button(root, text="Load Music", command.load_music)
play_button = tk.Button(root, text="Play", command=play_music)
pause_button = tk.Button(root, text="Pause", command=pause_music)
stop_button = tk.Button(root, text="Stop", command=stop_music)

load_button.pack(pady=10)
play_button.pack(pady=10)
pause_button.pack(pady=10)
stop_button.pack(pady=10)

song_title = tk.Label(root, text="No song loaded")
song_title.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
