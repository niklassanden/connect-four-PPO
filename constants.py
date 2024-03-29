# Connect four rules
CONNECT_X = 4
BOARD_HEIGHT = 6
BOARD_WIDTH = 7

# Board
EMPTY = 0
YELLOW = 1
RED = 2

# Misc
TRAINING_EPOCHS = 1000000
SAVE_EVERY_X_EPOCHS = 10

# Agent
LEARNING_RATE = 0.001 #0.0001
NUM_TRAJECTORIES = 10 # 50
GAMMA = 0.95 #0.95
GAE_LAMBDA = 0.95 #0.95
BATCH_SIZE = 1024
SGD_EPOCHS = 50 # 50
PPO_CLIP_EPSILON = 0.1 # 0.2
ENTROPY_FACTOR = 0.01 # 0.005
PI_TO_V_IMPORTANCE_FACTOR = 0.5
MAX_KL_DIVERGENCE = 0.005

# PyTorch
import torch
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
