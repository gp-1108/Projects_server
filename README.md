<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="20%" alt="<code>❯ REPLACE-ME</code>-logo">
</p>
<p align="center">
    <h1 align="center">Interact with my projects!</h1>
</p>
<p align="center">
    <em>Engage with Intelligent Interactivity!</em>
</p>
<p align="center">
	<!-- Shields.io badges disabled, using skill icons. --></p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=html,md,py">
	</a></p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
- [🎗 License](#-license)

---

## 📍 Overview

The project is a Python-based web application designed to engage users through interactive demos, including an image processing tool and a simulation of the classic Snake game. Built on Flask and utilizing advanced machine learning models, it showcases player segmentation and provides APIs for seamless image analysis and game interactions. The integration of Docker enhances the applications scalability and portability, while a responsive design ensures a user-friendly experience. Ultimately, this project offers a dynamic platform that blends entertainment with technology, enhancing user engagement through intelligent functionalities and real-time interaction.

---

## 👾 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project utilizes a Flask-based web application architecture, featuring Docker for containerization and ONNX models for machine learning inference, ensuring portability and seamless integration of components. |
| 🔩 | **Code Quality**  | The codebase adheres to Python best practices, incorporates modular design principles, and employs a consistent style. Function and variable names are descriptive, enhancing readability and maintainability. |
| 📄 | **Documentation** | Documentation includes detailed comments within the code and external resources, particularly in `README.md`, explaining key functionalities and setup instructions, aiding new contributors. |
| 🔌 | **Integrations**  | Key integrations include Flask for web interactions, ONNX for machine learning model inference, and Docker for deployment, enabling a scalable and versatile application architecture. |
| 🧩 | **Modularity**    | The codebase is highly modular, with distinct components handling specific functionalities (e.g., image processing, game simulation), promoting reusability and easy maintenance of the application. |
| ⚡️  | **Performance**   | The application is optimized for efficiency, utilizing ONNX models and Python libraries to ensure fast image processing and game simulation, with low resource utilization in a containerized environment. |
| 📦 | **Dependencies**  | Key dependencies include Flask, ONNX, OpenCV, Pillow, and NumPy, providing essential libraries for web functionality, image processing, and machine learning capabilities. |

---

## 📂 Repository Structure

```sh
└── /
    ├── Dockerfile
    ├── README.md
    ├── REAMDE-auto.md
    ├── app.py
    ├── logs
    │   └── my_app.log
    ├── models
    │   ├── best.onnx
    │   └── hybrid_model.onnx
    ├── requirements.txt
    ├── static
    │   ├── css
    │   ├── images
    │   ├── js
    ├── templates
    │   ├── player_seg.html
    │   └── snake_game.html
    ├── test.ipynb
    └── utils
        ├── __init__.py
        ├── api_funcs.py
        ├── logger.py
        ├── snake
        └── yoloseg
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [Dockerfile](Dockerfile) | Facilitates the deployment of a Python-based web application by defining the environment and dependencies required for operation. It sets up a Flask server, configures necessary packages for image processing, and ensures smooth execution of the application within a Docker container, enhancing portability and scalability within the overall architecture. |
| [app.py](app.py) | Facilitates user interaction through a Flask web application, serving detailed project information on player segmentation and a snake game simulation. Additionally, it exposes APIs for image processing and game simulation, ensuring seamless integration with the overarching architecture while enhancing user engagement and functionality. |
| [requirements.txt](requirements.txt) | Defines essential dependencies for the application, facilitating the integration of key libraries and frameworks such as Flask for web functionality and ONNX for model inference. Ensures a robust environment to support the project’s architecture, which centers on web-based interactions and machine learning capabilities. |


</details>

<details closed><summary>templates</summary>

| File | Summary |
| --- | --- |
| [player_seg.html](templates/player_seg.html) | Facilitates an interactive image processing demo on a project portfolio site, allowing users to upload images for processing. Showcases project details, images, and relevant resources while enhancing user experience with a responsive design and Bootstrap integration, aligning with the overall architecture of the repository. |
| [snake_game.html](templates/snake_game.html) | Creates an interactive Snake Game demo interface, showcasing project details alongside a visually appealing layout. The inclusion of simulation controls and project imagery enhances user engagement, seamlessly integrating within the repositorys architecture to provide a dynamic, informative experience for visitors exploring the project portfolio. |

</details>

<details closed><summary>models</summary>

| File | Summary |
| --- | --- |
| [best.onnx](models/best.onnx) | Facilitating advanced machine learning capabilities, the best.onnx model serves as a primary machine learning artifact within the repository. Its integration enhances the applications performance by providing state-of-the-art predictions, contributing significantly to the overall architecture dedicated to delivering a seamless user experience through intelligent features. |
| [hybrid_model.onnx](models/hybrid_model.onnx) | Houses a hybrid model designed to integrate multiple machine learning techniques, enhancing the repositorys capability to perform complex tasks. This model serves as a crucial component in the architecture, facilitating efficient data processing and inference in applications tied to image recognition and segmentation. |

</details>

<details closed><summary>utils</summary>

| File | Summary |
| --- | --- |
| [api_funcs.py](utils/api_funcs.py) | Facilitates image processing and game simulation within the application. It leverages YOLOSeg for image segmentation and the Snake game environment for simulating game actions, enhancing user interaction by providing processed images and game states as JSON responses, integral to the repositorys interactive features. |
| [logger.py](utils/logger.py) | Enhances the applications logging capabilities by establishing a structured logging system that rotates log files daily, retains logs for 30 days, and captures execution details of functions. This facilitates efficient monitoring and debugging, contributing to the overall reliability and maintainability of the repositorys architecture. |

</details>

<details closed><summary>utils.yoloseg</summary>

| File | Summary |
| --- | --- |
| [YOLOSeg.py](utils/yoloseg/YOLOSeg.py) | Facilitates advanced object segmentation by leveraging a YOLO model. Key features include image preprocessing, inference execution, and output processing to yield bounding boxes and mask maps. Integrates seamlessly into the repositorys architecture, enhancing functionality for image analysis and object detection tasks. |
| [utils.py](utils/yoloseg/utils.py) | Facilitates object detection and visualization within the repositorys architecture by defining essential utility functions. It enhances model performance through non-maximum suppression, bounding box transformations, and drawing functionality, ultimately supporting the integration of visual outputs in applications such as video surveillance and automated scene understanding. |

</details>

<details closed><summary>utils.snake</summary>

| File | Summary |
| --- | --- |
| [SnakeEnv.py](utils/snake/SnakeEnv.py) | Establishes a foundational environment for a multi-board Snake game, defining board states, rewards, and movement logic. Enables the simulation of game actions, such as eating fruits and colliding with walls, while supporting various game configurations to enhance the user experience within the broader repository architecture. |
| [HybridAgent.py](utils/snake/HybridAgent.py) | HybridAgent integrates baseline and DQN strategies to enhance gameplay in the repositorys snake game project. By dynamically selecting actions based on board state and avoiding self-collisions and wall hits, it improves decision-making for game agents, contributing significantly to the overall architecture of intelligent gameplay. |
| [BaselineAgent.py](utils/snake/BaselineAgent.py) | Defines a BaselineAgent that utilizes a decision-making mechanism based on the current game state in the repositorys Snake game architecture. It optimally determines actions for multiple game boards, prioritizing safe moves while navigating towards objectives, thereby enhancing gameplay dynamics and user experience. |
| [BaseAgent.py](utils/snake/BaseAgent.py) | Facilitates the creation of game agents by providing a foundational structure with essential constants and methods. Serves as a blueprint for subclasses to implement specific behaviors and actions, thereby enabling dynamic interaction with the game environment, critical for the overall gameplay experience within the repositorys architecture. |
| [DQNAgent.py](utils/snake/DQNAgent.py) | Enables a Deep Q-Network (DQN) agent for decision-making in gaming environments by leveraging ONNX models for inference. Critical features include action selection, Q-value updates, and input transformation, facilitating intelligent gameplay and adaptive learning inherent to the repositorys overall architecture focused on reinforcement learning. |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `version 3.10.4`

### 📦 Installation

Build the project from source:

1. Clone the  repository:
```sh
❯ git clone .
```

2. Navigate to the project directory:
```sh
❯ cd snake_rl
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

1. Run the application:
```sh
❯ python3 app.py
```

2. Visit `https://localhost:5001` in your browser to interact with the application.


---

## 🎗 License

This project is protected under the [APACHE 2.0](https://choosealicense.com/licenses/apache-2.0/) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/apache-2.0/) file.

---
