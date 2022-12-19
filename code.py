from time import sleep
import time
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1024, 768)
#camera.annotate_text = "Leonardo Zaniboni 11801049 \n Guilherme Yukio 11800796"
camera.annotate_text = "Luciano Bacelar 11800740 \n Andrey Cortez 11819487"
camera.start_preview(alpha=250) # aplha: 0 -255
#anotações na imagem
time.sleep(5)
camera.stop_preview()
#gravando video
camera.start_recording("vid_luciano_andrey.h264")
time.sleep(5)
camera.stop_recording()
time.sleep(5)