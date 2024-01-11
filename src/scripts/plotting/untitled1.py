#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:51:17 2023

@author: elaine
"""
from scipy.stats import spearmanr
from sklearn.feature_selection import chi2
from pandas import *
import csv
import numpy as np
import pandas as pd


DIR =  "/Users/elaine/Desktop/TOMNET/tomnet-project/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS101_v1_commit_698004/prediction/Traj_dS101_Query_dS101_pred/"
#data = read_csv(DIR+"final_target_predictions.csv")
data = pd.read_csv(DIR+'final_target_predictions.csv', usecols= ['final_target_ground_truth_labels','final_target_predicted_labels'])
data['gtbin'] = data.final_target_ground_truth_labels.apply(lambda x: format(int(x), '010b'))
data['pbin'] = data.final_target_predicted_labels.apply(lambda x: format(int(x), '010b'))
data['gtbin_1'] = data['gtbin'].astype(str)
data['pbin_1'] = data['pbin'].astype(str)

data['gtbin1'] = data['gtbin_1'].str[0:1]
data['gtbin2'] = data['gtbin_1'].str[1:2]
data['gtbin3'] = data['gtbin_1'].str[2:3]
data['gtbin4'] = data['gtbin_1'].str[3:4]
data['gtbin5'] = data['gtbin_1'].str[4:5]
data['gtbin6'] = data['gtbin_1'].str[5:6]
data['gtbin7'] = data['gtbin_1'].str[6:7]
data['gtbin8'] = data['gtbin_1'].str[7:8]
data['gtbin9'] = data['gtbin_1'].str[8:9]
data['gtbin10'] = data['gtbin_1'].str[9:10]

data['pbin1'] = data['pbin_1'].str[0:1]
data['pbin2'] = data['pbin_1'].str[1:2]
data['pbin3'] = data['pbin_1'].str[2:3]
data['pbin4'] = data['pbin_1'].str[3:4]
data['pbin5'] = data['pbin_1'].str[4:5]
data['pbin6'] = data['pbin_1'].str[5:6]
data['pbin7'] = data['pbin_1'].str[6:7]
data['pbin8'] = data['pbin_1'].str[7:8]
data['pbin9'] = data['pbin_1'].str[8:9]
data['pbin10'] = data['pbin_1'].str[9:10]

seperate_gtbin = data[['gtbin1','gtbin2','gtbin3','gtbin4','gtbin5','gtbin6','gtbin7','gtbin8','gtbin9','gtbin10']].to_numpy().astype(int)
seperate_pbin = data[['pbin1','pbin2','pbin3','pbin4','pbin5','pbin6','pbin7','pbin8','pbin9','pbin10']].to_numpy().astype(int)


#S,p = spearmanr(seperate_gtbin[0], seperate_pbin[0])

# for i in range (len(data)):   
#     S,p = spearmanr(seperate_gtbin[i], seperate_pbin[i])
#     data['spearmanr'][i] = S
#     data['pvalue'][i] = p
####################################################

set1_gt=[261,245,246,30,257,23,52,101,7,185]
set1_pred=[227,241,230,0,207,8,22,63,0,146]

set2_gt=[508,438,438,498,427,389,329,441,518,489]
set2_pred=[585,415,426,477,524,229,134,266,592,643]

set3_gt=[0,0,10,56,60,7,0,0,0,0]
set3_pred=[1,1,27,73,81,7,0,0,6,0]
S1,p1 = spearmanr(set1_gt, set1_pred)
S2,p2 = spearmanr(set2_gt, set2_pred)
S3,p3 = spearmanr(set3_gt, set3_pred)





