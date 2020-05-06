from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

class myHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print("event triggered")
        for filename in os.listdir(folder_to_track):
            print("moving file" + filename)
            file_extension = os.path.splitext(filename)[1]
            print(file_extension)
            src = folder_to_track + "\\" + filename     # Path for file to be moved

            if file_extension == ".pdf":    # Locates destination folder
                folder_destination = "C:\\DATA\\PDF_downloads\\"
            elif file_extension == ".txt":
                folder_destination = "C:\\DATA\\TXT_downloads\\"
            elif file_extension == ".jpg" or file_extension == ".png":
                folder_destination = "C:\\DATA\\IMAGE_downloads\\"
            else:
                folder_destination = "C:\\DATA\\MISC_downloads\\"
            new_destination = folder_destination + filename     # Path to be moved too
            os.rename(src, new_destination)


folder_to_track = "C:\\users\\DomRi\\Downloads"
folder_destination = "placeHolder_value"

event_handler = myHandler()  # initialises myHandler
my_observer = Observer()    # initialises observer (imported from watchdog)
my_observer.schedule(event_handler, folder_to_track, recursive=True)
my_observer.start()
i = 1
try:
    while True:
        time.sleep(10)
        i = i + 1
        print("check" + folder_to_track)
        print(i)
except KeyboardInterrupt:
    my_observer.stop()
my_observer.join()
