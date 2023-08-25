from tkinter import *
from PIL import Image, ImageTk
import os
import shutil
import tempfile

THEME_COLOR = "#375362"
BG_COLOUR = "#e64340"


#This class gets the directory for where the temporary files are located and deletes them
class Delete_temp:
    def __init__(self):
        self.temp_location = tempfile.gettempdir()

        self.temp_files = os.listdir(self.temp_location)

        for file in self.temp_files:
            self.files_in_path = os.path.join(self.temp_location, file)
            try:
                if os.path.isfile(self.files_in_path):
                    os.remove(self.files_in_path)
                elif os.path.isdir(self.files_in_path):
                    shutil.rmtree(self.files_in_path)
            except Exception as e:
                pass


#Class of the GUI. Has a large delete button that, when pressed would delete all the temp
#files on the computer
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.maxsize( 350, 400)
        self.window.minsize(350, 400)
        self.window.title("Temp Cleaner")
        self.window.config(padx = 25, pady = 25, bg = THEME_COLOR)
        self.canvas = Canvas(self.window, width = 300, height = 50, bg = BG_COLOUR, highlightthickness=0)
        self.canvas.grid(row = 0, column = 1)
        self.canvas = self.canvas.create_text(150, 25, text = "Delete All Temp files", fill = "white", font = ("Arial", "20", "bold"))

        photo_image = Image.open("Delete.png")
        resized = photo_image.resize((300, 300))

        new_image = ImageTk.PhotoImage(resized)

        self.temp_delete_button = Button(image = new_image, command = lambda : Delete_temp(), highlightthickness= 0)
        self.temp_delete_button.grid(row = 2, column = 1)
        self.window.mainloop()


GUI()
