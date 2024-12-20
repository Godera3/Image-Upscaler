"""



import tkinter as tk
from tkinter import messagebox


def show_welcome_message():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Show a message box with a welcome message
    messagebox.showinfo("Welcome", "Welcome to the Photo Upscaling Program!")

    root.destroy()  # Destroy the root window after the message box is closed

if __name__ == "__main__":
    show_welcome_message() 

    
    
"""