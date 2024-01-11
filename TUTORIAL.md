# ToMNet 2.0 Tutorial

## Dependencies 
Tomnet2 is implemented in python and tested with tensorflow 1.8. Please install this version of tensorflow first using the official documentation. Only Python versions 3.5, 3.6, 3.7, or 3.8 are compatible along with tensorflow 1.8. 

## Activate Environment
TO DO: Write up a section on how to download, install, and configure the environment so that the user can replicate on their local devices. 

Refer to the yml file for appropriate packages and their versions. Also include info on how much storage the environment requires to inform the user. Show how the user can set up targets so that if they run 【$ conda activate tomnet】, they are able to configure the environment. 

For more information on managing conda environments, please refer to this documentation.

Run the following code to activate environment: ??


## Create Training Data
TO DO: create a small example user data set to test performance (in the tomnet2/data/data_dynamic folder)

Running ToMnet 2.0 is a multistep process. In addition to a training model, we have provided data simulation code to create simulated training data.

To create new sets of simulation training data, please cd into the dynamic folder (via tomnet2/scripts/simulation_data_generator/dynamic) and run the following code:  $ python simulation_data_dynamic.py to generate new simulation maze grids. The data will be found in the toment2/data/data_dynamic folder. 

To make adjustments to the training data code, please follow the following steps:
- Adjustments to the training steps can be made in tomnet2/models/working_model/main_imports/class_model.py by adjusting the train_steps object. 
- Adjustments to training data usage can be made in tomnet2/models/working_model/main_imports/class_model.py by changing the path_ckpt and the path_train objects. 
- Other major adjustments can be made in tomnet2/scripts/simulation_data_generator/dynamic/simulation_data_dynamic.py 
- Be sure to change the name of the data set target when testing and training certain data. 

Pretrained results can be found in the toment2/working_model/testing_data folder


## Train and Test Model
Training: python main_model.py 
Constructing model to learning preferences

Testing: python preference_predictor.py
Giving set of new arrays, how it performs

TO DO, separation of training and testing 

To train the model, cd into tomnet2/models/working_models run the following code: 

```$ python main_model.py```


To test the preferences, cd into tomnet2/models/working_models and run the following code:

```$ python preference_predictor.py```

The output of this code will be a folder found in tomnet2/models/working_model/training_data_set_results/test_on_simulation_data/training_result/caches. The folder contains a predictions and training folder. There are two sets of predictions. 

Query Prediction: The model is trained and tested on different social structures but same mazes.

Prediction: The model is trained and tested on the same social structures but with different mazes. 

The sum predictions are the summed matrix of the prediction vectors used to compare ground truth and prediction. Outputs into Plot_tomnet2_predstates.ipynb uses the predictions from sum_predictions to plot a graphical representation.

TO DO: Insert infographic screenshots from Elaine’s defense presentation of output results and final graph representation, as well as a brief about how to interpret the results.