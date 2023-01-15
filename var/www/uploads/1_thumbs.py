from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
import urllib.request
from moviepy.editor import * # import everythings (variables, classes, methods...) inside moviepy.editor
from PIL import Image
import subprocess

#with open('nume_fisier.txt', 'r') as f:
        #numele = str(f.readline())
#print('' + numele)
#url = ('' + numele)
#print(url)
#print('==================')
#urllib.request.urlretrieve(url, "cocofinal.mp4")
#output = subprocess.run(["mv", "cocos_spatiu.mp4", "/var/www/uploads/data/inputs/"], capture_output=True)

source_path = os.path.join(SAMPLE_INPUTS, 'cocos_spatiu.mp4') # get the path to our sample video
thumbnails_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
os.makedirs(thumbnails_dir, exist_ok=True) # create the folder 'thumbnails'  at Ex : path/to/your/project/folder/data/outputs/thumbnails

clip = VideoFileClip(source_path) #

with open('/var/www/uploads/fisier_nume.txt', 'r') as f:
        valoare = int(f.readline())



#fbs = clip.reader.fps # return number of frame per second
#nframes = clip.reader.nframes # return number of frame in the video
#duration = clip.duration # return duration of the video in second
#max_duration = int(clip.duration) + 1
#print(max_duration) # print on the console the value of max_duration
frame_at_second = 5 # here is the time where you want to take the thumbnail at second, it should be smaller than max_duration
frame = clip.get_frame(frame_at_second) # Gets a numpy array representing the RGB picture of the clip at time frame_at_second
new_image_filepath = os.path.join(thumbnails_dir,f"{valoare}.jpg")
new_image = Image.fromarray(frame ) # convert numpy array to image
new_image.save(new_image_filepath) # save the image

valoare += 1
with open('/var/www/uploads/fisier_nume.txt', 'w') as f:
        f.write(str(valoare))


#for i in range(0, max_duration):
   # frame = clip.get_frame(i)
   # new_image_filepath = os.path.join(thumbnails_dir,f"{i}.jpg")
   # new_image = Image.fromarray(frame)
   # new_image.save(new_image_filepath)