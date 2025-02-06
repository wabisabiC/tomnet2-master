# Created by Chih-Yi Chen on 2024-05-22
import tomnet as tom  # Importing the tomnet module

# Define constants for the social score generation
FNAME = 'testing'  # File name for the output CSV file
MIN = -30  # Minimum value for social score
MAX = 0  # Maximum value for social score
MEAN = -10  # Mean value for social score
SD = 10  # Standard deviation for social score

# Define constants for the simulation data generation
RANDOM_NUM_GOALS = False  # If True, the number of goals will vary across mazes
VERSION_NAME = 'testing'  # Version name used for output directory naming
STEP_TOTAL = 20  # Maximum steps in each maze
AGENT_NAME = "testing"  # Name of the agent, will be in the name of the output TXT file
SET_UP_MAZE_TOTAL = 1000  # Total number of mazes to set up
PRINT_FINAL_MAZE = False  # Flag to indicate whether to print the final maze

# Define constants for the TOMNet model
LIST_SUBJECTS = ["testing"]  # List of subject names, should correspond to VERSION_NAMEs
MODE = 'all'  # Mode of operation: 'all' for training and testing, 'train' for training only, 'test' for testing only

# Generate social score data
tom.generate_social_score(FNAME, MIN, MAX, MEAN, SD)

# Generate dynamic simulation data
tom.simulation_data_dynamic(FNAME, RANDOM_NUM_GOALS, VERSION_NAME, STEP_TOTAL, AGENT_NAME, SET_UP_MAZE_TOTAL, PRINT_FINAL_MAZE)

# Train and test the TOMNet model
tom.tomnet2(LIST_SUBJECTS, MODE)

# The results can be found in `src/models/working_model/test_on_simulation_data/training_result/caches/cache_dS103_v1_commit_/train/_train_test_and_validation_accuracy.csv` (the path can be changed by modifying `self.path_train` in `src/models/working_model/model/main_model.py`).
