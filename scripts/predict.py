from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("/home/febin/yolov8/runs/detect/train4/weights/best.pt")

# from PIL
# im1 = Image.open("/home/febin/yolov8/test/images/frame_001229.PNG")
# results = model.predict(source=im1, save=True)  # save plotted images
results = model.track(source="/home/febin/yolov8/test/test.mp4", show=True)