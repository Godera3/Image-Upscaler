from tkinter import filedialog, Tk
import tkinter as tk
import os

def select_photos():
    """Open a file dialog for the user to select image files."""
    root = Tk()
    root.withdraw()  # Hide the root window
    filetypes = [("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    files = filedialog.askopenfilenames(title="Select Photos", filetypes=filetypes)
    return list(files) if files else []

def choose_save_directory():
    """
    Open a dialog to choose the save directory, defaulting to the Desktop.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Get the path to the Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Open the directory selection dialog with the Desktop as the initial directory
    directory = filedialog.askdirectory(initialdir=desktop_path, title="Select Save Directory")

    root.destroy()  # Destroy the root window after the dialog is closed
    return directory