from flask import request, jsonify
import base64
import io
from PIL import Image
from utils.yoloseg import YOLOSeg
import cv2
import numpy as np
from utils.snake import SnakeEnv, HybridAgent
from utils.logger import log_function

@log_function
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

@log_function
def simulate_snake_game():
    # Get the number of actions from query parameters
    num_actions = int(request.args.get('num_actions', 10))

    if not (0 < num_actions <= 100):
        num_actions = 10

    # Create the environment
    env = SnakeEnv(1, 7)
    hyb = HybridAgent(env.boards, "models/hybrid_model.onnx")

    actions = []

    for _ in range(num_actions):
        action = hyb.get_actions(env.boards)
        actions.append(int(action[0][0]))
        env.move(action)

    # Convert the board state to a list of lists
    board = env.boards[0].astype(int).tolist()
    board = [[int(cell) for cell in row] for row in board]

    response = {
        'board': board,
        'actions': actions
    }
    return jsonify(response)