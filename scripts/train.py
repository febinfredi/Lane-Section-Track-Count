import os
from ultralytics import YOLO

# Load a pretrained YOLO model 
model = YOLO(os.getcwd() + "/models/" + "yolov8n.pt")

# Train the model
results = model.train(data=os.getcwd() + '/scripts/config.yaml', epochs=16, batch=16, imgsz=640, optimizer='auto', cache=True)

# Evaluate the model's performance on the validation set
# results = model.val()

# Perform object detection on an image using the model
results = model(os.path.dirname(os.getcwd()) + '/test/images/frame_001229.PNG')

# Export the model to ONNX format
success = model.export(format='onnx')
