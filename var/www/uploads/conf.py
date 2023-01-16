from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import * # import everythings (variables, classes, methods...) inside moviepy.editor
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4') # get the path to our sample video
thumbnails_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails') 
os.makedirs(thumbnails_dir, exist_ok=True)
