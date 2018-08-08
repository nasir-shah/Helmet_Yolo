from subprocess import call
from moviepy.editor import VideoFileClip
import imageio
import cv2
from time import time

def process_image(image):
  cv2.imwrite('test.jpg',image)

  call(['./darknet','detector','test','cfg/obj.data','cfg/yolo-obj.cfg','backup/yolo-obj_1000.weights','test.jpg'])
  img = cv2.imread('predictions.png')
  return img


white_output = './helmet_detection.mp4'
clip1 = VideoFileClip("./Media1.mp4")
white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!
white_clip.write_videofile(white_output, audio=False)
  