from flask import Flask, render_template
from datetime import datetime
from api_funcs import seg_player

app = Flask(__name__)

@app.route("/player-segmentation")
def project():
    # Fetch project data based on project_id
    project_data = {
        "title": "Player Segmentation",
        "short_description": "Fine-tuning YOLOv8 for occluded players segmentation",
        "description": "This model was trained specifically for segmenting people in images. The final performances greatly improved when dealing with occluded bodies, as the base model was struggling with it. Have a look at the paper for more insights.",
        "technologies": ["Python", "Ultralytics", "Deep Learning"],
        "images": ["band_seg.jpg", "couple_seg.jpg"],
        "completion_date": "2023-08-10",
        "github_url": "https://github.com/gp-1108/CV_Sport_Project",
        "paper": "https://github.com/gp-1108/CV_Sport_Project/blob/master/Report%20-%20Sport%20Scene%20Analysis.pdf"
    }
    return render_template("player_seg.html", project=project_data, current_year=datetime.now().year)

@app.route('/api/process-image', methods=['POST'])
def process_image():
    return seg_player()

if __name__ == "__main__":
    app.run(
        ssl_context=("../cert.pem", "../key.pem"),
        host="0.0.0.0",
        port=5001,
        debug=True
    )