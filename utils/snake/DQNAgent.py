from .BaseAgent import BaseAgent
import numpy as np
import onnxruntime as ort

class DQNAgent(BaseAgent):
    """
    Deep Q-Network Agent class using ONNX for inference.
    Args:
        boards_sample (ndarray): Sample board(s) used to determine the input shape of the model.
        onnx_path (str): Path to the ONNX model.
        alpha (float, optional): Learning rate. Defaults to 0.1.
        gamma (float, optional): Discount factor. Defaults to 0.95.
        epsilon (float, optional): Exploration factor. Defaults to 1.0.
        decay (float, optional): Decay rate for epsilon. Defaults to 0.99.
    Attributes:
        alpha (float): Learning rate.
        gamma (float): Discount factor.
        epsilon (float): Exploration factor.
        decay (float): Decay rate for epsilon.
        input_shape (tuple): Shape of the input to the model.
        output_size (int): Number of possible actions.
        ort_session (onnxruntime.InferenceSession): ONNX runtime session for inference.
    Methods:
        get_actions(boards, exploration=True):
            Returns the actions to take for the given boards.
        get_action(board):
            Returns the action to take for the given board.
        learn(prev_boards, actions, rewards, next_boards):
            Updates the Q-values of the model based on the given data.
        load_model_weights(path):
            Loads the model weights from the given path
    Private Methods:
        _board_to_input(boards):
            Converts the boards to the input format expected by the model.
    """
    def __init__(self, boards_sample, onnx_path, alpha=0.1, gamma=0.95, epsilon=1.0, decay=0.99):
        """
        Initializes a DQNAgent object.

        Parameters:
        - boards_sample (ndarray): A sample of game boards used to determine the input shape of the model.
        - onnx_path (str): The path to the ONNX model.
        - alpha (float): The learning rate for the agent's Q-learning algorithm. Default is 0.1.
        - gamma (float): The discount factor for future rewards in the agent's Q-learning algorithm. Default is 0.95.
        - epsilon (float): The exploration rate for the agent's epsilon-greedy policy. Default is 1.0.
        - decay (float): The decay rate for the agent's exploration rate. Default is 0.99.
        """
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.decay = decay
        # Model parameters
        if boards_sample.ndim == 2:
            boards_sample = boards_sample[np.newaxis, :, :]
        self.input_shape = self._board_to_input(boards_sample).shape[1:]
        self.output_size = 5  # UP, DOWN, LEFT, RIGHT, NONE

        # Load ONNX model for inference
        self.ort_session = ort.InferenceSession(onnx_path)

    def get_actions(self, boards, exploration=True):
        """
        Returns the actions to be taken by the agent based on the given game boards.
        Parameters:
        - boards (ndarray): The game boards for which actions need to be determined.
        - exploration (bool): Flag indicating whether to perform exploration or not.
        Returns:
        - actions (ndarray): The actions to be taken by the agent.
        """
        self.epsilon = self.epsilon * self.decay
        self.epsilon = max(self.epsilon, 0.01)
        if boards.ndim == 2:
            boards = boards[np.newaxis, :, :]
        input = self._board_to_input(boards).astype(np.float32)

        if np.random.rand() <= self.epsilon and exploration:
            return np.random.randint(0, self.output_size, size=(boards.shape[0], 1))
        else:
            q_values = self._get_q_values(input)
            return [[action] for action in np.argmax(q_values, axis=1)]

    def get_action(self, board):
        """
        Get the action to take based on the given board state.
        Parameters:
        - board: numpy.ndarray
            The board state.
        Returns:
        - numpy.ndarray
            The action to take.
        """
        if board.ndim == 2:
            board = board[np.newaxis, :, :]
        input = self._board_to_input(board).astype(np.float32)
        
        q_values = self._get_q_values(input)
        return np.argmax(q_values, axis=1)[:, np.newaxis]

    def _board_to_input(self, boards):
        """
        Converts the given boards into categorical input for the DQN agent.

        Parameters:
        - boards: The input boards to be converted.

        Returns:
        - The categorical input for the DQN agent, with the first channel removed.

        """
        return np.eye(5)[boards.astype(int)][..., 1:]

    def _get_q_values(self, input):
        """
        Get the Q-values from the ONNX model for the given input.
        
        Parameters:
        - input: The input data to the model.
        
        Returns:
        - Q-values predicted by the model.
        """
        input_name = self.ort_session.get_inputs()[0].name
        output_name = self.ort_session.get_outputs()[0].name
        outputs = self.ort_session.run([output_name], {input_name: input})
        return outputs[0]

    def load_model_weights(self, path):
        """
        Load the ONNX model weights from the given path.

        Parameters:
        - path (str): The path to the ONNX model file.

        Returns:
        - None
        """
        self.ort_session = ort.InferenceSession(path)
