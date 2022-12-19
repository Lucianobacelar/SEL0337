#capture.py
from time import sleep
import time
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

#anotações na imagem
camera.annotate_text = "Luciano Bacelar 11800740 \n Andrey Cortez 11819487"

#preview da camera
camera.start_preview(alpha=250) # aplha: 0 -255
time.sleep(5)
camera.stop_preview()

#inicio captura de imagem
camera.capture("img_luciano_andrey.png")

#inicia da gravação do vídeo
camera.start_recording("vid_luciano_andrey.h264")
time.sleep(5)
camera.stop_recording()
time.sleep(5)