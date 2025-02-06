import tensorflow as tf
import argparse
from .model.main_model import Model

def tomnet2(LIST_SUBJECTS=["dS103"],MODE='all'):
    """
    modified by Chih-Yi Chen on 2024-05-22
    Train and test the TOMNet model.

    Parameters:
    LIST_SUBJECTS (list): List of subject names to iterate through.
    MODE (str): Specifies the mode of operation. Default is 'all', which trains and tests the model. Other options include 'train' for training only and 'test' for testing only.

    Results can be found in:
    src/models/working_model/test_on_simulation_data/training_result/caches/cache_<LIST_SUBJECTS>_v1_commit_/train/_train_test_and_validation_accuracy.csv (the path can be changed by modifying self.path_train in src/models/working_model/model/main_model.py).
    """
    # --------------------------------------------------------
    # Constants
    # --------------------------------------------------------
    # LIST_SUBJECTS = ["S0" + str(i) for i in ["35","50","51","52"]]
    #LIST_SUBJECTS = ["dS103"]

    # LIST_SUBJECTS = ["S0" + str(i) for i in ["24","33","35","50","51","52"]]

    # --------------------------------------------------------
    # Iterate through the subject list
    # --------------------------------------------------------
    for subj_index, subj_name in enumerate(LIST_SUBJECTS):
        print("\n================================= \n"+
        "Start working on "+ subj_name+'\n'+
        "================================= \n")

        # reseting the graph is necessary for running the script via spyder or other
        # ipython intepreter
        tf.reset_default_graph()
        parser = argparse.ArgumentParser()

        # TODO: implement the human/simulation arg into cli
        """
        parser.add_argument('--data_type', type=str, default='human', help='Type of testing data: human or simulation')
        """
        parser.add_argument('--mode', type=str, default='all', help='all: train and test, train: only train, test: only test')
        parser.add_argument('--shuffle', type=str, default=False, help='shuffle the data for more random result')
        parser.add_argument('--subj_name',type = str,default=subj_name) # the subject name
        args = parser.parse_args()
        model = Model(args)
        # pdb.set_trace()
        if args.mode == 'train' or args.mode == 'all':
            model.train()
        if args.mode == 'test' or args.mode == 'all':
            model.test()

        print("------------------------------------")
        print("Congratultions! You have reached the end of the script.")
        print("------------------------------------")

