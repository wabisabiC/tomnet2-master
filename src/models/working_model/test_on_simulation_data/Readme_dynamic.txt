#########################################
This folder contains details for each training version.
Data path:

------------------------------------------


Directory description:
-test_on_human_data
This folder contains analysis on human data.
See README in it for detail.

-temporary_testing_version
This folder contains temporary testing files.
The codes root from Edwinn's codes with step-by-step modification.
See README in it for detail.

#########################################
Future training session (by YS)

(1) Train the model with variable sequence lengths:
https://danijar.com/variable-sequence-lengths-in-tensorflow/
(2) Don't use dropout for preference inference.
(3) Reconsider the data format of 'data_preference_predictions'. Maybe I should try more combination?
(4)

#########################################
Finished training session (v1,commit )
Time: 2023/07/12
Author: Elaine
Output file name: /cache_dS103_v1_commit_
Info: train_10000


train: proportion_accuracy()
Matches: 7557/8000
Accuracy: 94.46%
62 vali batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS103_v1_commit_/train/model.ckpt-9999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!
60 batches finished!

vali: proportion_accuracy()
Matches: 848/992
Accuracy: 85.48%
62 test batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS103_v1_commit_/train/model.ckpt-9999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!
60 batches finished!

test: proportion_accuracy()
Matches: 861/992
Accuracy: 86.79%
---------------------
########################################
Finished training session (v1,commit )
Time: 2023/07/11
Author: Elaine
Output file name: /cache_dS102_v1_commit_
Info: train_10000


train: proportion_accuracy()
Matches: 978/8000
Accuracy: 12.22%
62 vali batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS102_v1_commit_/train/model.ckpt-9999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!
60 batches finished!

vali: proportion_accuracy()
Matches: 31/992
Accuracy: 3.12%
62 test batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS102_v1_commit_/train/model.ckpt-9999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!
60 batches finished!

test: proportion_accuracy()
Matches: 29/992
Accuracy: 2.92%

########################################
Finished training session (v1,commit )
Time: 2023/07/06
Author: Elaine
Output file name: /cache_dS101_v1_commit_
Info: train_10000


train: proportion_accuracy()
Matches: 4586/8000
Accuracy: 57.32%
62 vali batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS101_v1_commit_/train/model.ckpt-9999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!
60 batches finished!

vali: proportion_accuracy()
Matches: 419/992
Accuracy: 42.24%
62 test batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS101_v1_commit_/train/model.ckpt-9999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!
60 batches finished!

test: proportion_accuracy()
Matches: 450/992
Accuracy: 45.36%
------------------------------------

########################################
Finished training session (v1,commit 858b36)
Time: 2022/08/24
Author: Elaine
Output file name: /cache_dS0078_v1_commit_858b36
Info: train_10000_test_preference_predictor_with_another_1000_on_dS0078


train: proportion_accuracy()
Matches: 4174/8000
Accuracy: 52.18%
62 vali batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS0078_v1_commit_858b36/train/model.ckpt-9999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!
60 batches finished!

vali: proportion_accuracy()
Matches: 337/992
Accuracy: 33.97%
62 test batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS0078_v1_commit_858b36/train/model.ckpt-9999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!
60 batches finished!

test: proportion_accuracy()
Matches: 341/992
Accuracy: 34.38%

########################################
v1(previous training)
With dS005~dS104 social preference
based on this prediction requirement, I modified commented_preference_predictor.py code into commented_preference_predictor_query.py and also /tomnet2/scripts/simulation_data_generator/dynamic/simulation_data_dynamic.py
(commit )
########################################
Finished training session (v1,commit 603c34)
Time: 2022/06/22
Author: Elaine
Output file name: /cache_dS001_v1_commit_603c34
Info: train_9000_test_preference_predictor_with_another_1000


train: proportion_accuracy()
Matches: 2662/7200
Accuracy: 36.97%
56 vali batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS001_v1_commit_603c34/train/model.ckpt-8999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!

vali: proportion_accuracy()
Matches: 157/896
Accuracy: 17.52%
56 test batches in total...
Model restored from  /home/.bml/Data/Bank1/ToMNET/tomnet-project/tomnet2/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS001_v1_commit_603c34/train/model.ckpt-8999
0 batches finished!
10 batches finished!
20 batches finished!
30 batches finished!
40 batches finished!
50 batches finished!

test: proportion_accuracy()
Matches: 149/896
Accuracy: 16.63%
------------------------------------



########################################
Finished training session (v24, commit 014d79)[At working_model]
Time: 2020/01/15
Author: Elaine
Output file name: /cache_S003b_v24_commit_014d79
Info: file10000_tuning_batch16_train_step_10K_INIT_LR_10-4

(1) Follow v23 but train it with S003b data.
Note:
(1) The result is similar to v23.

(2)
accurary	mode
97.09%	train_proportion
75.91%	vali_proportion
75.3%	test_proportion


(3)
Traj_S003b_Query_S003b_subset96
avg_prediction_probability	ground_truth_label_count	prediction_count	accuracy_data_set
0.21	19	19	85.42
0.25	21	25	85.42
0.14	19	12	85.42
0.41	37	40	85.42

Traj_S003b_Query_Stest_subset96:
prediction_proportion	avg_prediction_probability	ground_truth_label_count	prediction_count
0.25	0.2	0	24
0.15	0.2	0	14
0	0.05	0	0
0.6	0.55	0	58
########################################

