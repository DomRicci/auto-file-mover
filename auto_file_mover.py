from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

class myHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("event triggered")
        for filename in os.listdir(folder_to_track):
            print("moving file" + filename)
            src = folder_to_track + "\\" + filename          # folder and file name in tracked folder
            new_destination = folder_destination + filename      #  Destination folder and file name 
            os.rename(src, new_destination)


folder_to_track = "C:\\DATA\\Cs\\pythonLearning\\first_folder"
folder_destination = "C:\\DATA\\Cs\\pythonLearning\\second_folder\\"

event_handler = myHandler()  # initialises myHandler
my_observer = Observer()    # initialises observer (imported from watchdog)
my_observer.schedule(event_handler, folder_to_track, recursive=True)     
my_observer.start()
i = 1
try:
    while True:
        time.sleep(1)
        i = i + 1
        print("check" + folder_to_track)
        print(i)
except KeyboardInterrupt:
    my_observer.stop()
my_observer.join()

