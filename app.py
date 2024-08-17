from flask import Flask, render_template
from datetime import datetime
from api_funcs import seg_player

app = Flask(__name__)

@app.route("/project/player-segmentation")
def project():
    # Fetch project data based on project_id
    project_data = {
        "title": "Test tile",
        "short_description": "Test short description",
        "description": "Test description",
        "technologies": ["Python", "Flask", "HTML", "CSS", "JavaScript"],
        "images": ["band_seg.jpg", "couple_seg.jpg"],
        "completion_date": "2021-01-01",
        "github_url": "https://github.com/gp-1108/CV_Sport_Project",
        "additional_notes": "Test additional notes"
    }
    return render_template("project.html", project=project_data, current_year=datetime.now().year)

@app.route('/api/process-image', methods=['POST'])
def process_image():
    return seg_player()

if __name__ == "__main__":
    app.run(debug=True)