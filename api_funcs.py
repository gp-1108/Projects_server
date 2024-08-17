from flask import request, jsonify
import base64
import io
from PIL import Image
from ultralytics import YOLO

def seg_player():
    data = request.json
    image_data = data['image'].split(',')[1]  # Remove the "data:image/jpeg;base64," part
    image_bytes = base64.b64decode(image_data)
    
    # Process the image (this is a placeholder, replace with your actual processing logic)
    img = Image.open(io.BytesIO(image_bytes))

    # Making it smaller for faster processing
    W, H = img.size
    max_size = 300
    # Calculate the scaling factor
    scaling_factor = min(max_size / W, max_size / H)
    new_size = (int(W * scaling_factor), int(H * scaling_factor))
    img = img.resize(new_size)
    W, H = img.size

    # Load the model and process the image
    model = YOLO("./models/best.onnx", task="segment")
    result = model(img)[0]
    np_output = result.plot(
        boxes=False,
        color_mode="instance"
    )
    np_output = np_output[:, :, ::-1] # Convert BGR to RGB
    processed_img = Image.fromarray(np_output.astype('uint8'))
    buffered = io.BytesIO()
    processed_img.save(buffered, format="PNG")
    processed_image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return jsonify({
        'result': 'Image processed successfully',
        'processed_image': f'data:image/png;base64,{processed_image_base64}'
    })