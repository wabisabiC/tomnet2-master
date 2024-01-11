#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generating social range

@author: elaine
""" 
import os
import numpy as np
import pandas as pd

FNAME = 'dS103'
MIN = -30
MAX  = 0
MEAN = -10
SD = 10

DIR_CSV_OUTPUT = os.getcwd()
for n in range(1):    
    social_score = []
    # Set the random seed for reproducibility
    np.random.seed(42)

    # Generate a random set of 20 integers approximately satisfying the conditions
    social_score = np.random.randint(MIN, MAX+1, size=20)

    # Adjust the mean to 0 & standard deviation to 1
    social_score = (social_score - np.mean(social_score)) / np.std(social_score)
 
    social_score = (social_score * SD) + MEAN
    
            
    social_score = np.insert(social_score,(0,5,10,15,20),0)
    social_score = social_score.reshape(5,5)
    social_score = social_score.astype(float)
    
    df_social_score = pd.DataFrame(data = {" ":["S","A","B","C","D"],\
                                                          "S":social_score[0],\
                                                          "A":social_score[1],\
                                                          "B":social_score[2],\
                                                          "C":social_score[3],\
                                                          "D":social_score[4]})
    try:
        output = os.path.join(DIR_CSV_OUTPUT,str(FNAME)+".csv")
        df_social_score.to_csv(output,index=False)
    except:print('error')
    #print(df_social_score)
    n+=1

