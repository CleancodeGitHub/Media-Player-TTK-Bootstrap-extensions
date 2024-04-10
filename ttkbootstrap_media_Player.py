import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

def play():
    print("Play")

def pause():
    print("Pause")

def stop():
    print("Stop")

def open_file():
    print("Open File")

def update_volume(value):
    print("Volume:", value)

def update_progress(value):
    print("Progress:", value)

# Create the main Tkinter window
root = tk.Tk()
root.title("Media Player")

# Set the window size
root.geometry("800x600")

# Apply ttkbootstrap style
style = Style(theme='minty')

# Load background image
background_image = Image.open("Default_Create.PNG")  # your_background_image
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas for the background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, image=background_photo, anchor=tk.NW)

# Create a frame to hold the widgets
frame = ttk.Frame(canvas)
frame.pack(padx=20, pady=20)

# Create control buttons
control_frame = ttk.Frame(frame)
control_frame.pack(fill='x', expand='yes')

# Define control button texts
controls = {
    'play': '\u25B6',
    'skip-previous': '⏮',
    'skip-next': '⏭',
    'pause': '\u23F8',
    'stop': '\u23F9',
    'open-file': 'Open File'
}

# Create control buttons
buttons = {}
for button_name, button_text in controls.items():
    buttons[button_name] = ttk.Button(control_frame, text=button_text)
    buttons[button_name].pack(side='left', fill='x', expand='yes', ipadx=5, ipady=5, padx=2, pady=2)

# Bind actions to control buttons
buttons['play'].config(command=play)
buttons['pause'].config(command=pause)
buttons['stop'].config(command=stop)
buttons['open-file'].config(command=open_file)

# Create volume scale
volume_scale = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, style='info.Horizontal.TScale',
                         command=update_volume)
volume_scale.pack(fill='x', expand='yes', pady=10)

# Create progress scale
progress_scale = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, style='info.Horizontal.TScale',
                           command=update_progress)
progress_scale.pack(fill='x', expand='yes', pady=10)

# Start the Tkinter event loop
root.mainloop()
