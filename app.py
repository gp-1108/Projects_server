from flask import Flask, render_template, jsonify
from datetime import datetime
from utils.api_funcs import seg_player, simulate_snake_game
from utils.logger import logger

app = Flask(__name__)

@app.route("/player-segmentation")
def player_segmentation():
    # Fetch project data based on project_id
    project_data = {
        "title": "Player Segmentation",
        "short_description": "Fine-tuning YOLOv8 for occluded players segmentation",
        "description": "This model was trained specifically for segmenting people in images. The final performances greatly improved when dealing with occluded bodies, as the base model was struggling with it. Have a look at the paper for more insights.",
        "technologies": ["Python", "Ultralytics", "Deep Learning"],
        "images": ["band_seg.jpg", "couple_seg.jpg"],
        "completion_date": "2023-08-10",
        "github_url": "https://github.com/gp-1108/CV_Sport_Project",
        "report": "https://github.com/gp-1108/CV_Sport_Project/blob/master/Report%20-%20Sport%20Scene%20Analysis.pdf"
    }
    return render_template("player_seg.html", project=project_data, current_year=datetime.now().year)

@app.route("/snake-game")
def snake_game():
    project_data = {
        "title": "Snake Game Simulation",
        "short_description": "Simulating a snake game using Reinforcement Learning",
        "description": "This project aims to simulate a snake game using Reinforcement Learning. The agent is trained using a hybrid approach, combining both DQN and Policy Gradient methods. The final model was able to achieve high scoring on the number of fruits, avoiding wall collisions.",
        "technologies": ["Python", "TensorFlow", "Reinforcement Learning"],
        "images": [],
        "completion_date": "2024-08-10",
        "github_url": "https://github.com/gp-1108/snake_rl.git",
        "report": "https://github.com/gp-1108/snake_rl/blob/main/Report%20RL%20-%20Snake.pdf"
    }

    return render_template("snake_game.html", project=project_data, current_year=datetime.now().year)


@app.route('/api/process-image', methods=['POST'])
def process_image():
    try:
        return seg_player()
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        })

@app.route("/api/simulate-snake-game", methods=['GET'])
def snake():
    try:
        return simulate_snake_game()
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        })

if __name__ == "__main__":
    logger.info("Starting the app...")
    try:
        app.run(
            ssl_context=("/certs/cert.pem", "/certs/key.pem"),
            host="0.0.0.0",
            port=5001,
            debug=True
        )
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")