#This script is created by Arthur Lodbrock
from time import sleep
import os

#Downloads folder
current = 'C:\\Users\\user\\Downloads\\'
#Extentions and folders
spaces = [('Images', ['png', 'jpeg', 'bmp', 'tiff', 'gif', 'webp', 'svg', 'jpg', 'psd']),
          ('Documents', ['txt', 'doc', 'pdf', 'csv', 'ics', 'json', 'xlsx', 'djvu']),
          ('Audio', ['mp3', 'wav', 'midi']),
          ('Video', ['mp4', 'avi', 'webm']),
          ('Archive', ['zip', 'rar', 'gz', 'jar']),
          ('Programs', ['exe', 'msi']),
          ('Android App', ['apk']),
          ('Osu files', ['osz']),
          ('Torrents', ['torrent'])]

#File organization function
def file_manager(config, extention, current_path, filename):
  for y in config:
      for x in y[1]:
        if extention == x: #Checking files extention
          dest = current_path + y[0]
          if os.path.exists(dest) == False:
            os.mkdir(dest)
          n_path = dest + '\\' + filename
          
          n_filename = filename

          i = 1
          while os.path.exists(n_path) == True: #Changing files name if it exists in target folder
            con = n_filename.split('.')
            n_filename = ''
            for x in range(len(con) - 1):
              n_filename += con[x]
            
            n_filename += "_copy." + con[-1]
            n_path = dest + '\\' + n_filename
            i += 1
          
          os.rename(os.path.join(current_path, filename), dest + '\\' + n_filename)  #Sending file to specific folder
          return

#Endless word :D
while(True):
  for entry in os.listdir(current):
    path = os.path.join(current, entry)
    if os.path.isfile(path):
      li = entry.split('.')
      file_manager(spaces, li[-1], current, entry)
  sleep(1) #Only 1 second for sleep
  


