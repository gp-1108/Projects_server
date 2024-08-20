from flask import request, jsonify
import base64
import io
from PIL import Image
from utils.yoloseg import YOLOSeg
import cv2
import numpy as np

def seg_player():
    data = request.json
    image_data = data['image'].split(',')[1]  # Remove the "data:image/jpeg;base64," part
    image_bytes = base64.b64decode(image_data)

    # Convert the byte data to a NumPy array
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)

    # Decode the image from the array
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    
    # Initialize the YOLOSeg model
    yolo_seg = YOLOSeg("models/best.onnx")
    boxes, scores, class_ids, masks = yolo_seg(img)
    combined_img = yolo_seg.draw_masks(img)
    # Convert to RGB
    combined_img = cv2.cvtColor(combined_img, cv2.COLOR_BGR2RGB)
    combined_img = Image.fromarray(combined_img)

    # Scaling the image to max of 500px
    width, height = combined_img.size
    max_size = 500
    if width > height:
        new_width = max_size
        new_height = int(max_size * height / width)
    else:
        new_height = max_size
        new_width = int(max_size * width / height)
    combined_img = combined_img.resize((new_width, new_height))


    buffered = io.BytesIO()
    combined_img.save(buffered, format="PNG")
    processed_image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return jsonify({
        'result': 'Image processed successfully',
        'processed_image': f'data:image/png;base64,{processed_image_base64}'
    })