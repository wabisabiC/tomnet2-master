#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 16:56:10 2023

@author: elaine
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


TARGET = 'cache_dS102_v1_commit_'  #"caches_folder_name"
DIR = os.getcwd()

RESULT_DIR = os.path.join(DIR,'../../models/working_model/test_on_simulation_data')

CACHES_DIR = os.path.join(RESULT_DIR,'training_result/caches',TARGET,'train')
FIGURES_DIR = os.path.join(RESULT_DIR,'training_result/figures')
error_csv = os.path.join(CACHES_DIR,'_error.csv')
error_figure = os.path.join(FIGURES_DIR,TARGET+'-1.png')

error = pd.read_csv(error_csv,header=0)
error = error.drop('Unnamed: 0',axis=1)


plt.plot(error["step"],error["train_error"],color='r',label='train_error')
plt.plot(error["step"],error["validation_error"],color='tab:cyan',label='validation_error')
plt.grid(True)
plt.title('Set 2 Performance',fontsize=20)

plt.xlabel("step",fontsize=15)
plt.ylabel("error",fontsize=15)
plt.legend(loc='lower left')
plt.savefig(error_figure,dpi=300)

plt.show()



