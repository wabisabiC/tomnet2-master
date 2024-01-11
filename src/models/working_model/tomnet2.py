from model.main_model import Model


if __name__ == "__main__":
  # --------------------------------------------------------
  # Constants
  # --------------------------------------------------------
  # LIST_SUBJECTS = ["S0" + str(i) for i in ["35","50","51","52"]]
  LIST_SUBJECTS = ["dS103"]

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

