#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:01:47 2023

@author: elaine
"""
import scipy.stats as stats
from sklearn.feature_selection import chi2
from pandas import *
import csv


DIR =  "/Users/elaine/Desktop/TOMNET/tomnet-project/tomnet2/models/working_model/test_on_simulation_data/training_result/caches/cache_dS103_v1_commit_/prediction/Traj_dS103_Query_dS103_pred/"
data = read_csv(DIR+"final_sum_predictions.csv")
query = data['prediction'].tolist()
ground_truth = data['ground_truth'].tolist()


test3 = stats.wilcoxon(query,ground_truth)
print("test3:",test3)

# A = [58,67,41,85,52,39,55,69,33,70]
# B = [34,32,45,46,38,30,67,43,39,41]
# BA = stats.wilcoxon(A,B)
# print(BA)